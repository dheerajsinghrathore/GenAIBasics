from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
llm=ChatOpenAI(model="gpt-4o-mini")
prompt=PromptTemplate.from_template("Write {adjective} summary of {topic} in {language}")
formatted_prompt=prompt.format(adjective="concise",topic="Java",language="English")
response=llm.invoke(formatted_prompt)
print(response.content)