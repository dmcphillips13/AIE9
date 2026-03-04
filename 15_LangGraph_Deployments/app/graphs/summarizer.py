"""A tool-using agent graph with a post-response summarization node.

The graph:
- Calls a chat model bound to the tool belt.
- If the last message requested tool calls, routes to a ToolNode.
- Otherwise, routes to a summarizer node that condenses the response.
- If the summary is adequate, terminates; otherwise, loops back to the agent.
"""
from __future__ import annotations

from pydantic import BaseModel, Field

from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import AIMessage

from app.state import MessagesState
from app.models import get_chat_model
from app.tools import get_tool_belt


class SummaryResult(BaseModel):
    is_concise: bool = Field(description="Whether the summary is concise and complete")
    summary: str = Field(description="A concise summary of the response")


def _build_model_with_tools():
    """Return a chat model instance bound to the current tool belt."""
    model = get_chat_model()
    return model.bind_tools(get_tool_belt())


def call_model(state: MessagesState) -> dict:
    """Invoke the model with the accumulated messages and append its response."""
    model = _build_model_with_tools()
    messages = state["messages"]
    response = model.invoke(messages)
    return {"messages": [response]}


def route_to_action_or_summarizer(state: MessagesState):
    """Decide whether to execute tools or run the summarizer."""
    last_message = state["messages"][-1]
    if getattr(last_message, "tool_calls", None):
        return "action"
    return "summarizer"


_summarizer_prompt = ChatPromptTemplate.from_template(
    "Given an initial query and a final response, produce a concise summary "
    "that captures the key points. Also determine if the summary is concise "
    "and complete.\n\n"
    "Initial Query:\n{initial_query}\n\n"
    "Final Response:\n{final_response}"
)


def summarizer_node(state: MessagesState) -> dict:
    """Summarize the latest response relative to the initial query."""
    if len(state["messages"]) > 10:
        return {"messages": [AIMessage(content="SUMMARY:END")]}

    initial_query = state["messages"][0]
    final_response = state["messages"][-1]

    structured_model = get_chat_model(model_name="gpt-4.1-mini").with_structured_output(SummaryResult)
    result = (_summarizer_prompt | structured_model).invoke(
        {
            "initial_query": initial_query.content,
            "final_response": final_response.content,
        }
    )

    decision = "Y" if result.is_concise else "N"
    return {"messages": [AIMessage(content=f"SUMMARY:{decision}\n{result.summary}")]}


def summarizer_decision(state: MessagesState):
    """Terminate on adequate summary or loop otherwise; guard against infinite loops."""
    if any(getattr(m, "content", "") == "SUMMARY:END" for m in state["messages"][-1:]):
        return END

    last = state["messages"][-1]
    text = getattr(last, "content", "")
    if "SUMMARY:Y" in text:
        return "end"
    return "continue"


def build_graph():
    """Build an agent graph with an auxiliary summarization evaluation node."""
    graph = StateGraph(MessagesState)
    tool_node = ToolNode(get_tool_belt())
    graph.add_node("agent", call_model)
    graph.add_node("action", tool_node)
    graph.add_node("summarizer", summarizer_node)
    graph.add_edge(START, "agent")
    graph.add_conditional_edges(
        "agent",
        route_to_action_or_summarizer,
        {"action": "action", "summarizer": "summarizer"},
    )
    graph.add_conditional_edges(
        "summarizer",
        summarizer_decision,
        {"continue": "agent", "end": END, END: END},
    )
    graph.add_edge("action", "agent")
    return graph


graph = build_graph().compile()
