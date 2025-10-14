import os
from typing import List
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages  import HumanMessage # to invoke agents
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from pydantic import BaseModel, Field #give base class in order to describe structure(data parsing, serialisation) and field allows us to add metadata(descriptions- helps llm know what to put in that field)
from langchain_tavily import TavilySearch
load_dotenv()

class Source(BaseModel):
    """Schema for a source used by the agent"""
    url:str = Field(description="The url of the source")

class AgentResponse(BaseModel):
    """Schema for agent response"""
    answer:str = Field(description="The agent answer to the query")
    sources : List[Source] = Field(default_factory=list, description="List of sources used to generate the answer")
@tool
def search(query:str)-> str:
    """Search the customer database for records matching the query.

    Args:
        query: Search terms to look for
        limit: Maximum number of results to return
    """
    print(f"search{query}")
    return "weather in Tokyo is sunny"

# llm = ChatOpenAI(model="llama3.2:1b")
llm = ChatOllama(model="granite3-moe:1b")
tools = [TavilySearch()]
agent = create_agent(model=llm,tools=tools,response_format=AgentResponse)

def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages":HumanMessage(content="what is weather in tokyo")})
    print(result)

if __name__ == "__main__":
    main()
