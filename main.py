from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_openai import ChatOpenAI

load_dotenv()



model = ChatOpenAI(model="gpt-4")
search = TavilySearchResults(max_results=2)
# If we want, we can create other tools.
# Once we have all the tools we want, we can put them in a list that we will reference later.
tools = [search]

from langgraph.prebuilt import create_react_agent
agent_executor = create_react_agent(model, tools)
response = agent_executor.invoke(
    {"messages": [HumanMessage(content="whats the weather in sf?")]}
)
print(response)
print(response["messages"])
