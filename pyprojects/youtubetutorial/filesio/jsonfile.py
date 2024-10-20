"""
    Author: Prosenjit Ghosh Chowdhury
    Date: 15-Oct-2024
"""
# What is JSON? Usage of JSON?
# Who uses JSON?
# Create a JSON file from Python object
# Load a JSON file to a Python Object
# Create a JSON string from Python object 
# Create a Python object from JSON string
"""
    JSON - Java Script Object Notation. 
    it’s  completely independent of JavaScript 
    It’s commonly used to transfer data. 
    XML or YAML also used for same purpose  
    It’s also friquently used by DB and API to store and transfer data. 
    It also used as config files. 
    It’s popular coz it easily read by human and and machine both
 """

### Create a JSON file from Python object ###
dict_students = {
    "studentinfo": [
        { "name": "Atreyee", "age": 15, "hobbies": ["Reading", "Singing"],
             "Computer Language": ["JAVA", "PYTHON", "GO"]
            },
        { "name": "Aritrika", "age": 10, "hobbies": ["Reading", "Dancing"],
             "Computer Language": ["JAVA", "PYTHON"]
            }
        ]
}

import json

with open("filesio/students.json", "w") as jw:
    json.dump(dict_students, jw, indent=2)



### Load a JSON file to a Python Object ###
with open("filesio/students.json", "r") as jr:
    stu_json_load = json.load(jr)
print(type(stu_json_load))
print(stu_json_load["studentinfo"][0])



### Create a JSON string from Python object ###
stu_json_str = json.dumps(dict_students, indent=2)
print(stu_json_str)
print(type(stu_json_str))


### Create a Python object from JSON string ###
obj_json_loads = json.loads(stu_json_str)
print(type(obj_json_loads))
print(obj_json_loads["studentinfo"][1])


