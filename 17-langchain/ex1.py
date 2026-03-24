from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.9)
response = llm.invoke("What year did the first man land on the moon?")
print(response.content)