from typing import TypedDict
from langgraph.graph import StateGraph

#Step 1: Define the state and action types
class State(TypedDict):
    msg: str
    count: int

#step 2: Create the state graph/Nodes
def greet(state):
    print('Calling greet')
    return {'msg': 'Hello, World!', 'count': 0}

def add_name(state):
    print('Calling add_name')
    return {'msg': state['msg']+" Dheeraj", 'count': state['count'] + 1}

def loop_check(state):
    if state['count'] < 3:
        print('Looping back to add_name')
        return 'loop'
    return 'end'

#Step 3: Create the state graph and add nodes
builder = StateGraph()