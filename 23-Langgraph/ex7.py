from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

class State(TypedDict):
    query: str
    decision: str
    tool_output: str
    final_answer: int

llm = ChatOpenAI(model='gpt-3.5-turbo')

def calculator(state):
    print('Calling calculator node')
    try:
        result = eval(state['query'])
        return {"tool_output": str(result)}
    except Exception as e:
        return {"tool_output": f"Error: {str(e)}"}
    
def decide_action(state):
    print('Calling decide_action node')
    prompt = f"""
Decide what to do for this query: {state['query']}
If it requires calculation, return "tool". 
If it can be answered directly, return "answer". 
"""
    response = llm.invoke(prompt).content.strip().lower()
    if "tool" in response:
        return {"decision": "tool"}
    else:
        return {"decision": "answer"}

def route(state):
    print('Calling route node')
    if state['decision'] == "tool":
        return "tool"
    else:
        return "answer"

def generate_answer(state):
    print('Calling generate_answer node')
    if state.get("tool_output"):
        return {"final_answer": state["tool_output"]}
    else:
        prompt = f"Answer the following question: {state['query']}"
        response = llm.invoke(prompt).content.strip()
        return {"final_answer": response}
    

builder = StateGraph(State)
builder.add_node('decide', decide_action)
builder.add_node('tool', calculator)
builder.add_node('answer', generate_answer)

builder.add_edge(START, 'decide')
builder.add_conditional_edges('decide', route, {
    'tool': 'tool',
    'answer': 'answer'
})

builder.add_edge('tool', 'answer')
builder.add_edge('answer', END)

graph = builder.compile()

topic = "Enter your query for calculation or direct answer: "

result = graph.execute({"query": topic, "decision": "", "tool_output": "", "final_answer": ""})

print("Final Answer:", result['final_answer'])