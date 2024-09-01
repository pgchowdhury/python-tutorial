"""
    Author: Prosenjit Ghosh Chowdhury
    Date: 30-August-2024
"""
##### How to Create a Dictionary #####
# curly braces method
my_dict = {}
print(my_dict)
my_dict["India"] = "New Delhi"
my_dict["United States"] = "Washington DC"
print(my_dict)
my_dict_predifined_val = {"Tom": 30, "Harry": 32, "Bob": 29}
print(my_dict_predifined_val)
my_dict_predifined_val["Harry"] = 35
print(my_dict_predifined_val)

# dict() Constructor Method
# Create with keyword argument list
student_dict = dict(name="Alice", age=16, grade="A", subject="Economics")
print(student_dict)
# create with list of tuple
student_tup_dict = dict([("name", "Chris"), ("age", 18), ("grade", "A")])
print(student_tup_dict)
# using fromkeys() method
name = ['a', 'e', 'i', 'o', 'u']
vowels = dict.fromkeys(name)
print(vowels)

##### How to access items in a dictionary #####
student_dict = dict(name="Alice", age=16, grade="A", subject="Economics")
print(student_dict["name"])
print(student_dict["age"])
print(student_dict.get("grade"))
#print(student_dict["address"]) 
print(student_dict.get("address")) 
print(student_dict.get("address","Toronto, Canada")) 
print(student_dict)
student_dict_keys = student_dict.keys()
student_dict_values = student_dict.values()
print(student_dict_keys)
print(student_dict_values)


##### How to add items to a Dictionary #####
hp_dict = {"Harry Potter": "Gryffindor", "Ron Weasley": "Gryffindor", "Hermione Granger": "Gryffindor"}
print(hp_dict)
hp_dict["James Potter"] = "Gryffindor"
print(hp_dict)
hp_dict.update(Snape="Slytherin")
print(hp_dict)
# The update() method is useful whenever we want to merge dictionaries or add new key:value pairs 
# using an iterable like tuples or lists
add_ch_1 = {"Albus Dumbledore": "Gryffindor", "Luna Lovegood": "Ravenclaw"}
hp_dict.update(add_ch_1)
# Using list of list
add_ch_2 = [["Draco Malfoy", "Slytherin"], ["Cedric Diggory", "Hufflepuff"]]
hp_dict.update(add_ch_2)
print(hp_dict)

##### How to remove items from a dictionary #####
new_hp_dict = {'Harry Potter': 'Gryffindor', 'Ron Weasley': 'Gryffindor', 
               'Hermione Granger': 'Gryffindor', 'James Potter': 'Gryffindor', 'Snape': 'Slytherin', 
               'Albus Dumbledore': 'Gryffindor', 'Luna Lovegood': 'Ravenclaw', 
               'Draco Malfoy': 'Slytherin', 'Cedric Diggory': 'Hufflepuff'}
print(new_hp_dict)
# using del function
del new_hp_dict["Draco Malfoy"]
print(new_hp_dict)

# using pop() method
new_hp_dict.pop("Luna Lovegood")
print(new_hp_dict)

#### Iterate Over a Dictionary #####
hp_dict = {"Harry Potter": "Gryffindor", "Ron Weasley": "Gryffindor", "Hermione Granger": "Gryffindor"}
for character in hp_dict:
    print(character)
print("--------------")
for character, house in hp_dict.items():
    print(character, "||", house)