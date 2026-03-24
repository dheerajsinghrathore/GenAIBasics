from openai import OpenAI
from dotenv import load_dotenv
from datetime import datetime

def get_open_ai_client():
    load_dotenv()
    client=OpenAI()
    return client

def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def model_planning(user_message):
    tools=[
        {
            "type":"function",
            "function":{
                "name":"get_current_time",
                "description":"Get the current system time",
                "parameters":
                    {
                        "type":"object",
                        "properties":{}
                    }
            }
        }
    
    ]
    messages=[
    {
        "role":"system",
        "content":"You are a helpful AI Agent"
    }
    ]
    messages.append({"role":"user","content":user_message})
    response=client.chat.completions.create(model="gpt-4o-mini",messages=messages,tools=tools)
    message=response.choices[0].message
    return messages,message

def process_response(messages,message):
    if not message.tool_calls:
        return message.content
    
    function_name=message.tool_calls[0].function.name
    if function_name=="get_current_time":
       result=get_current_time()
    messages.append(message)
    messages.append({
           "role":"tool",
           "tool_call_id":message.tool_calls[0].id,
           "content":result
       })
    sec_response=client.chat.completions.create(model="gpt-4o-mini",messages=messages)
    ai_reply=sec_response.choices[0].message.content
    return ai_reply
       
       
    

client=get_open_ai_client()
user_message=input("Type your question:")
messages,message=model_planning(user_message)
ai_reply=process_response(messages,message)
print("Agent:",ai_reply)
