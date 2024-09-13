"""
    Author: Prosenjit Ghosh Chowdhury
    Date: 09-Sept-2024
"""

# get all methods from Dictionary
i = 0
for method in dir(dict):
    if '__'not in method:
        i += 1
        print(f'# {i}. {method}')
        print()


### 1. Keys Method -> dict.keys() ###
hdict: dict = {'Harry Potter': 'Gryffindor', 'Luna Lovegood': 'Ravenclaw', 'Draco Malfoy': 'Slytherin', 
 'Cedric Diggory': 'Hufflepuff'}
k = hdict.keys()
print(k)

### 2. Values Method -> dict.values() ###
hdict: dict = {'Harry Potter': 'Gryffindor', 'Luna Lovegood': 'Ravenclaw', 'Draco Malfoy': 'Slytherin', 
 'Cedric Diggory': 'Hufflepuff'}
v = hdict.values()
print(v)

### 3. Get Method -> dict.get("key") ###
hdict: dict = {'Harry Potter': 'Gryffindor', 'Luna Lovegood': 'Ravenclaw', 'Draco Malfoy': 'Slytherin', 
 'Cedric Diggory': 'Hufflepuff'}
#print(hdict['Harry Potter1'])
h = hdict.get('Harry Potter1', 'Not Available')
print(h)

### 4. setdefault Method -> x = dict.setdefault("key", "defaultvalue") ### 
hdict: dict = {'Harry Potter': 'Gryffindor', 'Luna Lovegood': 'Ravenclaw', 'Draco Malfoy': 'Slytherin', 
 'Cedric Diggory': 'Hufflepuff'}
sd: str = hdict.setdefault('Snape', 'Slytherin')
print(sd)
print(hdict)

### 5. Items Method -> dict.items() ### 
hdict: dict = {'Harry Potter': 'Gryffindor', 'Luna Lovegood': 'Ravenclaw', 'Draco Malfoy': 'Slytherin', 
 'Cedric Diggory': 'Hufflepuff'}
for key, val in hdict.items():
    print(key, "||", val)

### 6. Update Method -> dict.update(Iterable) ### 
hdict_ori: dict = {'Harry Potter': 'Gryffindor', 'Luna Lovegood': 'Ravenclaw', 'Draco Malfoy': 'Slytherin', 
 'Cedric Diggory': 'Hufflepuff'}
add_ch_1: dict = {"Albus Dumbledore": "Gryffindor", "Luna Lovegood": "Ravenclaw"}
hdict_ori.update(add_ch_1)
print(hdict_ori)

### 7. fromkeys Method -> thisdict = dict.fromkeys(listofkeys, "defaultvalue") ### 
name: list = ['a', 'e', 'i', 'o', 'u']
vowels: dict = dict.fromkeys(name, "vowel")
print(vowels)

### 8. copy Method -> x = dict.copy() ### 
dict_ori: dict = { 'x': [1, 2], 'y': [3, 4], 'z': [5, 6] }
dict_copy = dict_ori.copy()
dict_copy['x'][0] = 10
print(dict_ori)
print(dict_copy)
print(id(dict_ori), id(dict_copy))


### 9. popitem Method -> dict.popitem() ### 
hdict = {'Harry Potter': 'Gryffindor', 'Luna Lovegood': 'Ravenclaw', 'Draco Malfoy': 'Slytherin', 
 'Cedric Diggory': 'Hufflepuff'}
hdict.popitem()
print(hdict)


### 10. pop Method -> str = dict.pop(key) ### 
hdict = {'Harry Potter': 'Gryffindor', 'Luna Lovegood': 'Ravenclaw', 'Draco Malfoy': 'Slytherin', 
 'Cedric Diggory': 'Hufflepuff'}
p = hdict.pop('Luna Lovegood')
print(p)
print(hdict)


### 11. clear Method -> dict.clear() ### 
hdict = {'Harry Potter': 'Gryffindor', 'Luna Lovegood': 'Ravenclaw', 'Draco Malfoy': 'Slytherin', 
 'Cedric Diggory': 'Hufflepuff'}
hdict.clear()
print(hdict)