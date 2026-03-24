from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.globals import set_llm_cache
from langchain_core.caches import InMemoryCache

load_dotenv()
set_llm_cache(InMemoryCache())
llm=ChatOpenAI(model="gpt-4o-mini")
response1=llm.invoke("Who is the President Of India")
print("AI Reply:",response1.content)
response2=llm.invoke("Who is the President Of India")
print("AI Reply:",response2.content)