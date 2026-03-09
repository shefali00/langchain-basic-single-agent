from langchain.tools import tool
from agents.response_agent import response_agent

@tool
def create_response(ticket: str):
    """Create a response for the support ticket."""
    result = response_agent.invoke(
        {"messages":[{"role":"user","content":ticket}]}
    )
    return result["messages"][-1].content
