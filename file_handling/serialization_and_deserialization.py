# serialization 
import json

d = {"name": "ajay", "age": 23, "gender": "male"}

with open("demo.json", "w") as f:
    json.dump(d, f, indent=4)


# deserialization
import json

with open("demo.json", "r") as f:
    d = json.load(f)
    print(d)
    print(type(d))
