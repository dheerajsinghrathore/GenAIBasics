from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
llm=ChatOpenAI(model="gpt-4o-mini")

prompt=ChatPromptTemplate.from_messages([
    ("system","You are a helpful assistant"),
    ("human","Explain {topic} in simple terms")]
)
message=prompt.format_messages(topic="Polymorphism")
response=llm.invoke(message)
print(response.content)