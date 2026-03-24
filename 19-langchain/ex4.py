from langchain_core.prompts import FewShotPromptTemplate,PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
llm=ChatOpenAI(model="gpt-4o-mini")

examples=[
        {"message":"I love this phone","emotion":"Positive"},
        {"message":"This product is awesome","emotion":"Positive"},
        {"message":"Your service is disgusting","emotion":"Negative"}
    ]
example_prompt=PromptTemplate.from_template("Message:{message}\nEmotion:{emotion}")
few_shot=FewShotPromptTemplate(
                                examples=examples,
                                example_prompt=example_prompt,
                                prefix="Classify the emotion of the following message",
                                suffix="Message:{input}\nEmotion:",
                                input_variables=["input"]
                                )
str=input("Type a sentence:")
prompt=few_shot.format(input=str)
response=llm.invoke(prompt)
print("Prompt",prompt)
print(response.content)