# ai-agent-talk-2024-11-30
## Links

Tutorial
- [Langchain - Build an Agent](https://python.langchain.com/docs/tutorials/agents/)

References
- [Langchain - Chat models](https://python.langchain.com/docs/concepts/chat_models/)
- [Langchain - Tools](https://python.langchain.com/docs/concepts/tools/)
- [Langchain - Agents](https://python.langchain.com/docs/concepts/agents/)
- [Langgraph - Agent Architectures](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/)


## Steps to install

```
git clone https://github.com/cvanvlack/ai-agent-talk-2024-11-30.git
```
Install `pyenv`, it will automatically detect the correct Python version from the `.python-version` file. 

Create and activate a Python virtual environment:

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
We are using the Open AI models for this, but you can choose [any particular model](https://python.langchain.com/docs/tutorials/agents/#using-language-models) from the example. Make sure you have an Open AI API key set in your .env file
``` .env
# Set your openai api key like this
OPENAI_API_KEY=sk-...
```
