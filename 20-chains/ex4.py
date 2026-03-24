from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_classic.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import CommaSeparatedListOutputParser

load_dotenv()
llm=ChatOpenAI(model="gpt-4o-mini")

prompt=PromptTemplate.from_template(
    "List top 5 {topic} separated by commas"
    )
parser=CommaSeparatedListOutputParser()
chain=LLMChain(llm=llm,prompt=prompt)

topic=input("Enter the topic for listing:")
response=chain.run({"topic":topic})
text=parser.parse(response)
print(text)