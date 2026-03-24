from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.globals import set_llm_cache
from langchain_community.cache import SQLiteCache

load_dotenv()
set_llm_cache(SQLiteCache(database_path="mydata.db"))
llm=ChatOpenAI(model="gpt-4o-mini")
response1=llm.invoke("Who is the President Of India")
print("AI Reply:",response1.content)
response2=llm.invoke("Who is the President Of India")
print("AI Reply:",response2.content)