from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_classic.chains import LLMChain
from langchain_core.prompts import PromptTemplate

load_dotenv()
llm=ChatOpenAI(model="gpt-4o-mini")

prompt=PromptTemplate.from_template(
    """Act as a software consultant.
       Compare the {lang1} and {lang2} programming languages for the {proj} type project
    """)
chain=LLMChain(llm=llm,prompt=prompt)

lang1=input("Enter first lang name:")
lang2=input("Enter second lang name:")
proj=input("Enter project title name:")
response=chain.invoke({"lang1":lang1,"lang2":lang2,"proj":proj})
print(response["text"])