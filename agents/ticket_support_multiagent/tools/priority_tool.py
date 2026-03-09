
from langchain.tools import tool
from agents.priority_agent import priority_agent

@tool
def detect_priority(ticket: str):
    """Determine ticket priority."""
    result = priority_agent.invoke(
        {"messages":[{"role":"user","content":ticket}]}
    )
    return result["messages"][-1].content
