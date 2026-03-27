from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.9)
prompt1 = ChatPromptTemplate.from_template("Explain {topic} in simple terms.")
prompt2 = ChatPromptTemplate.from_template("Convert this into bullet points: \n{input}")
chain = prompt1 | llm | prompt2 | llm
result = chain.invoke({"topic": "quantum computing"})
print(result.content)