from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain.agents import create_agent
from fastapi import FastAPI
from langserve import add_routes

load_dotenv()  # Load environment variables from .env file

search = GoogleSerperAPIWrapper()

llm = ChatGroq(model="openai/gpt-oss-20b")

tools = [search.run]
prompt = "your are a assistant and can search on google for user queries."

agent =create_agent(model = llm, tools = tools, system_prompt = prompt)

app = FastAPI(
    title="Chatbot API",
    
)

add_routes(
    app, 
    agent,
    path="/agent"
    )



# query = "who won ipl 2026?"
# response = agent.invoke(
#     {"messages": [{"role": "user", "content": query}]}
# )

# print(response["messages"][-1].content)
