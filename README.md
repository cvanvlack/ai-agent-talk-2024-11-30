# ai-agent-talk-2024-11-30
## Links
Repo
```
git clone https://github.com/cvanvlack/ai-agent-talk-2024-11-30.git
```

Tutorial
- [Langchain Ecosystem](https://python.langchain.com/docs/introduction/)
- [Langchain - Build an Agent](https://python.langchain.com/docs/tutorials/agents/)

References
- [Langchain - Chat models](https://python.langchain.com/docs/concepts/chat_models/)
- [Langchain - Tools](https://python.langchain.com/docs/concepts/tools/)
- [Langchain - Agents](https://python.langchain.com/docs/concepts/agents/)
- [Langgraph - Agent Architectures](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/)


## Steps to install
(Recommended) Install `pyenv`, it will automatically detect the correct Python version from the `.python-version` file. 

(Required) Create and activate a Python virtual environment:
```
python -m venv .venv

# Activate virtual environment
# On Unix/macOS:
source .venv/bin/activate

# On Windows:
.venv\Scripts\activate
```
Then install requirements
```
pip install -r requirements.txt
```
## Services to Setup for this
You will need an API Key from the following services for this tutorial
- [Open AI](https://platform.openai.com/settings/organization/api-keys) - This is for the LLM. I would recommend setting up a [project](https://platform.openai.com/settings/organization/projects) for this and then having an API key that's specific to the project.
- [Tavily](https://tavily.com/) - This is a search engine that is tailored for agents.
- [Langsmith](https://smith.langchain.com/) - This is for observation of your agent calls. Technically not required for this demo, but the Langchain docs put it in, likely as a marketing vehicle.

We are using the Open AI models for this, but you can choose [any particular model](https://python.langchain.com/docs/tutorials/agents/#using-language-models) from the example. Make sure you have an Open AI API key set in your .env file. There's an included [.env.example](.env.example) to see the format.
``` .env
# Set your openai api key like this
OPENAI_API_KEY=sk-...
TAVILY_API_KEY=...
LANGCHAIN_API_KEY=...
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
LANGCHAIN_PROJECT=...
```
## Goals

- Talk about what an agent is
  - Agent Architectures
  - [Elements](https://www.linkedin.com/pulse/chapter-1-ai-agents-agentic-behavior-ashish-bhatia-qkjre/)
    - ![Agent Elements](https://media.licdn.com/dms/image/v2/D4E12AQHiM-RKsz3OMw/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1709866945773?e=1737590400&v=beta&t=92Pelod03wtCelRP9bdP7jMuXJGbBYIwGnt15j3k7P4)
  - [Researcher](https://docs.tavily.com/docs/gpt-researcher/introduction)
    - ![Research Agent](https://cowriter-images.s3.amazonaws.com/architecture.png)
- Talk about some of the specific concepts in agents
  - [Chat Models](https://python.langchain.com/docs/concepts/chat_models/)
  - [Tools](https://python.langchain.com/docs/concepts/tools/)
  - [Agents](https://python.langchain.com/docs/concepts/agents/)
  - [Memory](https://python.langchain.com/docs/tutorials/agents/#streaming-tokens)
- Non-Goals
  - Streaming output [messages](https://python.langchain.com/docs/tutorials/agents/#streaming-messages) or [tokens](https://python.langchain.com/docs/tutorials/agents/#streaming-tokens)
