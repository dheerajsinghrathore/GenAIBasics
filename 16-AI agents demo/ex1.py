from openai import OpenAI
from dotenv import load_dotenv
from datetime import datetime

def get_open_ai_client():
    load_dotenv()
    client=OpenAI()
    return client

def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


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
messages.append({"role":"user","content":"What is the current time?"})
client=get_open_ai_client()
response=client.chat.completions.create(model="gpt-4o-mini",messages=messages,tools=tools)
message=response.choices[0].message
if message.tool_calls:
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
       print("Agent:",ai_reply)
       
       
else:
    print("Agent:",message.content)