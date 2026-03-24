from openai import OpenAI
from dotenv import load_dotenv
from datetime import datetime
import json
def get_open_ai_client():
    load_dotenv()
    client=OpenAI()
    return client

def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_weather(city):
    fake_data={
        "Delhi":"25 Sunny",
        "Mumbai":"30 Humid",
        "Banagalore":"35 Cloudy"
    }
    return fake_data.get(city,"Unknown weather conditions")


def model_planning(user_message):
    tools=[
       #tool1
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
        },
        #tool 2
        {
            "type":"function",
            "function":{
                "name":"get_weather",
                "description":"Get the current conditions for any city",
                "parameters":
                    {
                        "type":"object",
                        "properties":{
                            "city":{
                                "type":"string",
                                "description":"City name( ex: Delhi ,Mumbai)"
                                
                            }
                        },
                        "required":["city"]
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
    messages.append(message)
    for tool_call in message.tool_calls:
        function_name=tool_call.function.name
        print(f"Agent calling {function_name}")
        if function_name=="get_weather":
            args_json=tool_call.function.arguments 
            arg_dict=json.loads(args_json)
            result=get_weather(**arg_dict)
        elif function_name=="get_current_time":
            result=get_current_time() 
    
        messages.append({
           "role":"tool",
           "tool_call_id":tool_call.id,
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
