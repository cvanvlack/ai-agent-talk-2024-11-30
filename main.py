from dotenv import load_dotenv
from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver
from tavily import TavilyClient
from langchain_openai import ChatOpenAI
from agent_state import AgentState

from nodes import plan_node, generation_node, reflection_node, research_plan_node, research_critique_node, should_continue

# Load the environment variables
load_dotenv()

tavily = TavilyClient()

model = ChatOpenAI(model="gpt-4o-mini")
memory = MemorySaver()

builder = StateGraph(AgentState)
initial_state: AgentState = {
    "task": "what is the difference between langchain and langsmith", 
    "plan": None,
    "draft": None,
    "critique": None,
    "content": [],
    "max_revisions": 2, 
    "revision_number": 1,
}

builder.add_node("planner", lambda state: plan_node(state, model))
builder.add_node("research_plan", lambda state: research_plan_node(state, model, tavily))
builder.add_node("generate", lambda state: generation_node(state, model))
builder.add_node("reflect", lambda state: reflection_node(state, model))
builder.add_node("research_critique", lambda state: research_critique_node(state, model, tavily))

builder.add_conditional_edges(
    "generate", 
    should_continue, 
    {END: END, "reflect": "reflect"}
)

builder.set_entry_point("planner")
builder.add_edge("planner", "research_plan")
builder.add_edge("research_plan", "generate")

builder.add_edge("reflect", "research_critique")
builder.add_edge("research_critique", "generate")

graph = builder.compile(checkpointer=memory)

thread = {"configurable": {"thread_id": "1"}}
   

for s in graph.stream(initial_state, thread):
    print(s)
