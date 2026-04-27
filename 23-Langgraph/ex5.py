from typing import TypedDict
from langchain_openai import ChatOpenAI
from langgraph.graph import END, START, StateGraph
from dotenv import load_dotenv

load_dotenv()

#Step 1: Define the state and action types
class State(TypedDict):
    user_input: str
    response_str: str

#step 2: Create LLM 

llm = ChatOpenAI(model='gpt-3.5-turbo')

#step 3: Define the functions that will be used as nodes in the state graph
def generate_greeting(state):
    print('Calling generate_greeting node')
    result = llm.invoke('Generate a greeting message for the user.')
    return {"response_str": result.content}

#Step 4: Create the state graph and add nodes
builder = StateGraph()

#step 5: Add nodes to the graph
builder.add_node('generate_greeting', generate_greeting)

#step 6: Define the edges between the nodes/ Entry and exit points
builder.add_edge(START, 'generate_greeting')
builder.add_edge('generate_greeting', END)
#step 7: Compile the graph
graph = builder.compile()

#step 8: User input and execute the graph
name = input("What is your name? ")

#step 9: Execute the graph with the initial state
result = graph.invoke({"user_input": name, "response_str": ""})
print(result['response_str'])