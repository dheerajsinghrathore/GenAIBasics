from langchain_core.prompts import FewShotChatMessagePromptTemplate,ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
llm=ChatOpenAI(model="gpt-4o-mini")

examples=[
        {"input":"Hello friend","output":"Hola amigo"},
        {"input":"My name is Sachin","output":"Mi nombre es Sachin"},
        
    ]
example_prompt=ChatPromptTemplate.from_messages([
            ("human","{input}"),
            ("ai","{output}")]
            )
few_shot_prompt=FewShotChatMessagePromptTemplate(
                examples=examples,
                example_prompt=example_prompt
            )
final_prompt=ChatPromptTemplate.from_messages([
                ("system","You translate English To Spanish"),
                few_shot_prompt,
                ("human","{input}")]
        )
user_input=input("Type a sentence in English:")
message=final_prompt.format(input=user_input)
response=llm.invoke(message)
print(response.content)
