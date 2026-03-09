
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from dotenv import load_dotenv
load_dotenv()
llm = ChatGroq(model="llama-3.3-70b-versatile")


response_agent = create_agent(
    model=llm,
    tools=[],
    system_prompt="""
Generate a professional customer support response.
"""
)
