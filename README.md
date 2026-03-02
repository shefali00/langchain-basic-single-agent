# LangChain Basic Agent

A minimal reference implementation of a **single AI agent** built using **LangChain**, **Groq LLM**, and **Tavily Search**.

This project demonstrates how a Large Language Model (LLM) can move beyond text generation and autonomously interact with external tools through an agent execution loop.

---

## Overview

This agent can:

- Understand user queries
- Reason using an LLM
- Decide when external information is required
- Automatically invoke tools
- Observe results and generate responses

LangChain manages the internal agent execution cycle.

---

## Architecture
User Query
↓
Agent
↓
LLM Reasoning (Groq)
↓
Tool Selection (Tavily Search)
↓
Observation
↓
Final Response


---

## LangChain Components Used

### Model
Groq LLM used for reasoning and decision-making.

### Tools
Tavily Search enables real-time web information retrieval.

### Agent
Acts as the decision-maker that determines whether to respond directly or invoke a tool.

### Executor
Runs the iterative execution loop:
Decide → Act → Observe → Repeat

## Project Structure
├── app.py
├── requirements.txt
├── .env.example
└── README.md


## Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/<your-username>/langchain-basic-agent.git
cd langchain-basic-agent

### 2. Install Dependencies
pip install -r requirements.txt

### 3. Configure Environment Variables
Create a .env file in the project root:
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key

### 4. Run the Agent
python app.py
