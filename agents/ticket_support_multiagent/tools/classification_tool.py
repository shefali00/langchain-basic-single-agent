
from langchain.tools import tool
from agents.classification_agent import classification_agent

@tool
def classify_ticket(ticket: str):
    """Classify the support ticket into one of the following categories:"""
    result = classification_agent.invoke(
        {"messages":[{"role":"user","content":ticket}]}
    )
    return result["messages"][-1].content
