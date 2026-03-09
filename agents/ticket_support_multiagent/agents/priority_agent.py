
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from dotenv import load_dotenv
load_dotenv()
llm = ChatGroq(model="llama-3.3-70b-versatile")

priority_agent = create_agent(
    model=llm,
    tools=[],
    system_prompt="""
Determine ticket priority.

Return one word only:
high
medium
low
"""
)
