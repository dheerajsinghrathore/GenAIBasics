from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
llm=ChatOpenAI(model="gpt-4o-mini",temperature=0.5,top_p=0.9,frequency_penalty=0.5)
response=llm.invoke("Where is Taj Mahal situated ?")
print(response.content)