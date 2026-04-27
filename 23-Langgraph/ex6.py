from typing import TypedDict
from langchain_openai import ChatOpenAI
from langgraph.graph import END, START, StateGraph
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage

load_dotenv()

#Step 1: Define the state and action types
class State(TypedDict):
    topic: str
    poem: str
    feedback: str
    count: int

#step 2: Create LLM instance
llm = ChatOpenAI(model='gpt-3.5-turbo')

#step 3: Define the functions that will be used as nodes in the state graph
def writer_node(state):
    print('Calling writer node with attempt count:', {state['count']+1})
    prompt = llm.invoke(f'Write a poem about {state["topic"]}. It must be exacatly 4 lines long and should not contain the word "poem".')
    if (state['feedback']):
        prompt = llm.invoke([HumanMessage(content=state['feedback']), prompt])

    result = llm.invoke(HumanMessage(content=prompt))
    return {"poem": result.content, "count": state['count'] + 1}

def auditor_node(state):
    print('Calling auditor node')
    line_count = state['poem'].count('\n') + 1
    if line_count == 4 and 'poem' not in state['poem'].lower():
        feedback = "Looks good!"
    else:
        feedback = f"The poem should be exactly 4 lines long and should not contain the word 'poem'. Your poem was {line_count} lines long."
    return {"feedback": feedback.content}

def should_repeat(state):
    print('Calling should_repeat node')
    if state['feedback'] == "Looks good!":
        return END
    elif state['count'] >= 3:
        return END
    return 'repeat'

#Step 4: Create the state graph and add nodes
builder = StateGraph(State)

#step 5: Add nodes to the graph
builder.add_node('writer_node', writer_node)
builder.add_node('auditor_node', auditor_node)

#step 6: Define the edges between the nodes/ Entry and exit points
builder.add_edge(START, 'writer_node')
builder.add_edge('writer_node', 'auditor_node')

builder.add_conditional_edges('auditor_node', should_repeat, {
    'end': END,
    'repeat': 'writer_node',
})

#step 7: Compile the graph
graph = builder.compile()

#step 8: User input and execute the graph
topic = input("Enter a topic for the poem: ")

#step 9: Execute the graph with the initial state
result = graph.invoke({"topic": topic, "poem": "", "feedback": "", "count": 0})
print(result['poem'])