import json
# Read a json str into python list of dict
with open("data.json","r") as file_obj:
    messages=json.load(file_obj)
print(messages)
print(type(messages))