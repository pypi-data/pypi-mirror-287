from langchain_core.messages import SystemMessage
from langchain_openai import ChatOpenAI
from langchain_core.pydantic_v1 import BaseModel, Field
from typing import List, Optional, Type
from dotenv import load_dotenv
from langchain_core.prompts.prompt import PromptTemplate
from langgraph.prebuilt import ToolExecutor, ToolInvocation
from langchain_core.messages import HumanMessage, ToolMessage
from langgraph.graph import MessageGraph, END
from langgraph.checkpoint.aiosqlite import AsyncSqliteSaver
from langchain.tools import BaseTool
from langchain.callbacks.manager import (
    CallbackManagerForToolRun,
    AsyncCallbackManagerForToolRun,
)
import os
import json

# Load environment variables
load_dotenv(override=True)

from archive_retriever import ArchiveRetriever, QualityConfig

retriever = ArchiveRetriever(
    quality_config=QualityConfig(
        topic_generation_limit=5,
        topic_top_k=15,
        min_relevant_article_count_for_relevant_topic=3,
        min_relevant_topics=5,
        topic_limit=1,
        sub_topic_generation_limit=3,
        story_week_top_k=14,
        story_month_top_k=42,
        story_min_article_x_days=7,
        story_limit=10,
    )
)
# Define document prompt template
DEFAULT_DOCUMENT_PROMPT = PromptTemplate.from_template(
    template="{page_content}\n\nSource: {newspaper_file_path}"
)


# Define input schema for the custom tool
class RetrieverInput(BaseModel):
    full_query: str = Field(
        description="""When using search_local_press, create a complete sentence that captures the user's request about the local press archive in Bremerhaven (Nordsee Zeitung). Use the same language as the input. Examples:

"Finde Artikel über die Entwicklung des Hafens in Bremerhaven zwischen 1990 und 2000."
"Suche nach Berichten über lokale Kulturveranstaltungen in Bremerhaven im letzten Sommer."
"Informationen zur Umweltpolitik und Klimaschutzmaßnahmen in Bremerhaven in den letzten fünf Jahren."

This approach ensures context-aware, specific queries related to the local press in Bremerhaven."""
    )


# Create custom retriever tool for local press
class CustomLocalPressRetrieverTool(BaseTool):
    name = "search_local_press"
    description = """Searches and returns documents from the local press archive in Bremerhaven (Nordsee Zeitung). This tool is crucial for answering any factual questions, retrieving context-specific information, or verifying details about Bremerhaven and its surrounding areas. Always use this tool when asked about specific events, places, or facts related to Bremerhaven, even if you think you might know the answer. Input should be a coherent, context-aware sentence that captures the user's request.

Remember: When in doubt, use this tool to ensure accuracy and up-to-date information about Bremerhaven's local news and history."""
    args_schema: Type[BaseModel] = RetrieverInput
    return_direct: bool = True

    def _run(
        self, full_query: str, run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        """Use the tool."""
        results = retriever.retrieve(full_query)
        return "\n\n".join([doc.page_content[:100] for doc in results])

    async def _arun(
        self,
        full_query: str,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Use the tool asynchronously."""
        results = retriever.retrieve(full_query)
        docs = []
        for doc in results:
            doc.page_content = doc.page_content[:100]
            source = f"Source:\n{{'newspaper_unique_id': 'https://zeitkapsel.blob.core.windows.net/default/{doc.metadata['newspaper_unique_id']}.pdf'}}"
            docs.append(f"{doc.page_content}\n\n{source}")
        return "\n\n".join(docs)


# Create the custom tool
custom_tool = CustomLocalPressRetrieverTool()

tools = [custom_tool]
tool_executor = ToolExecutor(tools)

# Initialize LLM and chain
llm = ChatOpenAI(temperature=0, streaming=True, model="gpt-4")
llm_with_tool = llm.bind_tools(tools)

# System message template
template = """You are an assistant specialized in helping users find information from the local press archive in Bremerhaven (Nordsee Zeitung).

Your job is to gather information from the user about their query and use the 'search_local_press' tool to find relevant articles. When formulating the query for the tool, make sure to include:

- The main topic or subject of the query
- Any relevant time period
- Specific locations or geographical areas of interest within or around Bremerhaven
- Any additional keywords or phrases that might be helpful

If any information is missing or unclear, ask the user to clarify. Do not guess or assume any details.

Once you have enough information, use the 'search_local_press' tool to perform the search. After receiving the results, summarize the key points and provide relevant details to the user."""


async def get_messages_info(messages):
    return [SystemMessage(content=template)] + messages


chain = get_messages_info | llm_with_tool


# Helper function for determining if tool was called
def _is_tool_call(msg):
    return hasattr(msg, "additional_kwargs") and "tool_calls" in msg.additional_kwargs


# Function to process messages and execute tool if called
async def process_messages(messages):
    tool_call = None
    for m in messages:
        if _is_tool_call(m):
            tool_call = m.additional_kwargs["tool_calls"][0]
            arguments = json.loads(tool_call["function"]["arguments"])
            break

    if tool_call:
        print(f"\033[94mTool Call: {tool_call}\033[0m")
        action = ToolInvocation(
            tool=tool_call["function"]["name"], tool_input=arguments["full_query"]
        )
        response = await tool_executor.ainvoke(action)
        function_message = ToolMessage(
            content=str(response), name=action.tool, tool_call_id=tool_call["id"]
        )
        messages.append(function_message)

    return messages


from langchain_core.messages import AIMessage


# Define state logic
async def get_state(messages):
    if _is_tool_call(messages[-1]):
        return "process_tool"
    elif isinstance(messages[-1], AIMessage):
        return END
    return "user_input"


# Create the graph
memory = AsyncSqliteSaver.from_conn_string(":memory:")

nodes = {k: k for k in ["user_input", "process_tool", END]}
workflow = MessageGraph()
workflow.add_node("user_input", chain)
workflow.add_node("process_tool", process_messages)
workflow.add_conditional_edges("user_input", get_state, nodes)
workflow.add_conditional_edges("process_tool", get_state, nodes)
workflow.set_entry_point("user_input")
graph = workflow.compile(checkpointer=memory)

import uuid
import asyncio
from langchain_core.messages import HumanMessage


async def main():
    config = {"configurable": {"thread_id": str(uuid.uuid4())}}
    while True:
        user = input("User (q/Q to quit): ")
        if user in {"q", "Q"}:
            print("AI: Byebye")
            break
        async for output in graph.astream([HumanMessage(content=user)], config=config):
            if "__end__" in output:
                continue
            # astream() yields dictionaries with output keyed by node name
            for key, value in output.items():
                print(f"Output from node '{key}':")
                print("---")
                print(value)
            print("\n---\n")


if __name__ == "__main__":
    asyncio.run(main())
