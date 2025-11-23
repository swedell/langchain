import os
from typing import List
from dotenv import load_dotenv
from langchain_classic import hub# sharing prompts, agents created by community
from langchain_classic.agents import AgentExecutor #runtime - make the calls or executor
from langchain_classic.agents.react.agent import create_react_agent #built-in langchain chain - runnable object - recievs tools+ prompt(react)(resoning agent)
from langchain_tavily import TavilySearch
from langchain_classic.agents.react.agent import create_react_agent
from langchain_ollama import ChatOllama

load_dotenv()


# llm = ChatOpenAI(model="llama3.2:1b")
llm = ChatOllama(model="granite3-moe:1b")
tools = [TavilySearch()]
react_prompt = hub.pull("hwchase17/react")
agent = create_react_agent(llm=llm,tools=tools,prompt=react_prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True,handle_parsing_errors=True)
chain = agent_executor

def main():
    print("Hello from langchain-course!")
    
    result = chain.invoke({"input": "search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details"})
    print(result)

if __name__ == "__main__":
    main()
