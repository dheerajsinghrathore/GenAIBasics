import json

#Read a json str and convert it into dict
with open("data.json","r") as file_obj:
    person=json.load(file_obj)

print(person)
print(type(person))