
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from dotenv import load_dotenv
load_dotenv()
llm = ChatGroq(model="llama-3.3-70b-versatile")

classification_agent = create_agent(
    model=llm,
    tools=[],
    system_prompt="""
You classify customer support tickets.

Return one word only:
billing
technical
product
general
"""
)
