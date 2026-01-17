import json
# convert a python list of dict to json and saving it in file
messages=[
          {"role":"user","content":"What is list in Python ?"},
          {"role":"assistant","content":"list is a mutable data type in Python"}
          ]
with open("data.json","w") as file_obj:
    json.dump(messages,file_obj)