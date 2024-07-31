from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes
from langchain_core.runnables import chain, RunnablePassthrough, Runnable
import uuid
import copy
from .main import graph

app = FastAPI()


@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")


@chain
async def graph_chain(inputs, config):
    if (
        "thread_id" not in config["configurable"]
        or config["configurable"]["thread_id"] is None
    ):
        config["configurable"]["thread_id"] = str(uuid.uuid4())

    inputs_copy = copy.deepcopy(inputs)
    print("\033[34minputs:", inputs, "\033[0m")
    messages = inputs_copy.get("history", [])

    print("\033[34mmessages:", messages, "\033[0m")

    last_message = inputs_copy.get(
        "input", ""
    )  # Use the 'input' field instead of last message in history

    full_history = [*messages, last_message]

    full_response = ""
    async for event in graph.astream_events(full_history, version="v1"):
        kind = event["event"]
        if kind == "on_chat_model_stream":
            content = event["data"]["chunk"].content
            if content:
                full_response += content
        elif kind == "on_tool_start":
            print(
                f"\033[33mStarting tool: {event['name']} with inputs: {event['data'].get('input')}\033[0m"
            )
        elif kind == "on_tool_end":
            print(f"\033[33mDone tool: {event['name']}\033[0m")
            print(f"\033[33mTool output was: {event['data'].get('output')}\033[0m")

    yield full_response


server_runnable: Runnable = graph_chain | RunnablePassthrough()

add_routes(
    app,
    graph_chain,
    path="/chat",
    enable_feedback_endpoint=True,
    playground_type="chat",
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.server:app", host="0.0.0.0", port=8000, reload=True)
