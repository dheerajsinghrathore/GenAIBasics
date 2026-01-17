import json
# convert a python dict tp json

person={"name":"Sachin","age":45}
json_str=json.dumps(person)
print(json_str)