from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch

# Load environment variables
load_dotenv()

# Initialize LLM (Groq)
model = ChatGroq(
    model="llama-3.3-70b-versatile"
)

# Define Tool
tools = [
    TavilySearch()
]

# Create Agent
agent = create_agent(
    model=model,
    tools=tools,
    system_prompt="You are a helpful AI agent."
)

# Run Agent
response = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": "Latest developments in AI agents"
        }
    ]
})

print(response)
