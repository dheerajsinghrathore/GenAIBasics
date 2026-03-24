from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage

def load_environment():
    load_dotenv()

def initialize_llm():
    llm=ChatOpenAI(model="gpt-4o-mini")
    return llm
def start_chat(llm):
    print("\nAssistant ready")
    print("\nType exit to quit")
    conversation=[SystemMessage(content="You are a helpful AI assistant who answers questions clearly and politely")]
    while True:
        user_input=input("You:")
        if user_input.lower()=="exit":
            print("\nConversation end!")
            break
        conversation.append(HumanMessage(content=user_input))
        response=llm.invoke(conversation)
        print("AI Response:",response.content)
        print()
        conversation.append(AIMessage(content=response.content))
load_environment()
llm=initialize_llm()
start_chat(llm)