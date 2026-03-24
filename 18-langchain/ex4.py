from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
llm=ChatOpenAI(model="gpt-4o-mini")
for chunk in llm.stream("Explain Generative AI"):
    print(chunk.content,end="",flush=True)