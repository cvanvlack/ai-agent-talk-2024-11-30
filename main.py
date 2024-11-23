from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver


# Load the environment variables
load_dotenv()

#Set up the chat model
model = ChatOpenAI(model="gpt-4")

#Create the TavilySearch tools
search = TavilySearchResults(max_results=2)

# If we want, we can create other tools.
# Once we have all the tools we want, we can put them in a list that we will reference later.
tools = [search]

#Create a way to store the memory of the conversation
memory = MemorySaver()

#Create an agent that gets executed by giving it the chat model, the tools and the memory to the checkpointer
agent_executor = create_react_agent(model, tools, checkpointer=memory)

# In order for the memory to keep track, we need to give it a threadId so that it can separate out the conversations
config = {"configurable": {"thread_id": "abc123"}}

print("************** First Message ****************")
# We can then stream back the messages
for chunk in agent_executor.stream(
    {"messages": [HumanMessage(content="whats the weather in Kitchener, Ontario?")]}, config
):
    print(chunk)
    print("----")

print("************** Second Message ****************")
#We can then add a folloq up message where the previous context is already included
for chunk in agent_executor.stream(
    {"messages": [HumanMessage(content="What should I wear?")]}, config
):
    print(chunk)
    print("----")

