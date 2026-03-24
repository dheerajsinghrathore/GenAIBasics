from langchain_core.prompts import ChatPromptTemplate


prompt=ChatPromptTemplate.from_messages([
    ("system","You are a helpful assistant"),
    ("human","Explain {topic} in simple terms")]
)
message=prompt.format_messages(topic="Polymorphism")
print(message)
