from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_classic.chains import LLMChain
from langchain_core.prompts import PromptTemplate

load_dotenv()
llm=ChatOpenAI(model="gpt-4o-mini")

prompt=PromptTemplate.from_template("You are a professional chef. Give me a small recipe using{ingredient}")
chain=LLMChain(llm=llm,prompt=prompt)

ingredient=input("Enter ingerdient name:")
response=chain.invoke({"ingredient":ingredient})
print(response["text"])