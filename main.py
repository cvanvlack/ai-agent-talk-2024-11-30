from dotenv import load_dotenv

from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from state import State
# Load the environment variables
load_dotenv()

graph_builder = StateGraph(State)

from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4")

def chatbot(state: State):
    return {"messages": [model.invoke(state["messages"])]}

# The first argument is the unique node name
# The second argument is the function or object that will be called whenever
# the node is used.
graph_builder.add_node("chatbot", chatbot)
