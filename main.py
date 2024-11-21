import getpass
import os

from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4")

from langchain_core.messages import HumanMessage

response = model.invoke([HumanMessage(content="hi!")])
print(response.content)
