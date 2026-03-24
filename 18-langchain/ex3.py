from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
def calculate_cost(input_tokens,output_tokens,model):
    prices={
            "gemini-2.5-flash":{"input":0.30,"output":2.5},
            "gemini-3-flash":{"input":0.50,"output":3.00}
            }
    price=prices.get(model)
    input_cost=(input_tokens*price.get("input"))/1000000
    output_cost=(output_tokens*price.get("output"))/1000000
    return input_cost+output_cost
    
load_dotenv()
from langchain_community.callbacks import get_openai_callback
load_dotenv()
llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash")
response=llm.invoke("Where is Taj Mahal situated ?")
usage=response.usage_metadata
print("AI Reply:",response.content)
print("Input tokens:",usage.get("input_tokens"))
print("Output tokens:",usage.get("output_tokens"))
print("Total tokens:",usage.get("total_tokens"))
print("Total Cost(USD):",calculate_cost(usage.get("input_tokens"),usage.get("output_tokens"),"gemini-2.5-flash"))