from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_classic.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()
llm=ChatOpenAI(model="gpt-4o-mini")
parser=JsonOutputParser()
fmt_inst=parser.get_format_instructions()
prompt=PromptTemplate.from_template(
    """Analyze this product review:\n{review}.
       {format_instructions}
    """
    )

chain=LLMChain(llm=llm,prompt=prompt)

response=chain.run({"review":"Amazing phone ! Battery lasts long, camera is outstanding","format_instructions":fmt_inst})
text=parser.parse(response)
print(text)