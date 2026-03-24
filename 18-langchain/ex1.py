from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_community.callbacks import get_openai_callback
load_dotenv()
llm=ChatOpenAI(model="gpt-4o-mini")
with get_openai_callback() as cb:
    response=llm.invoke("Where is Taj Mahal situated ?")
    print(response)
    print(response.content)
    print("Total Tokens:",cb.total_tokens)
    print("Prompt Tokens:",cb.prompt_tokens)
    print("Completion Tokens:",cb.completion_tokens)
    print("Total Cost(USD):",cb.total_cost)