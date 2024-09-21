"""
    Author: Prosenjit Ghosh Chowdhury
    Date: 20-Sept-2024
"""
### Creating Tuples ###
# Basic Syntax
my_tuple = (1, 2, 3)
print(my_tuple)
print(type(my_tuple))
print("--------------------")

my_tuple_float = (1.1, 2.3, 3.56)
print("Tuple with float elements:", my_tuple_float) 
print(type(my_tuple_float))
print("--------------------")

my_tuple_str = ("JAVA", "PYTHON", "GO")
print("Tuple with string elements:", my_tuple_str) 
print(type(my_tuple_str))
print("--------------------")

my_tuple_bool = (True, False, True)
print("Tuple with Boolean elements", my_tuple_bool) 
print(type(my_tuple_bool))
print("--------------------")

my_tuple_mix = (1, 1.1, "PYTHON", True)
print("Tuple with mix elements", my_tuple_mix)
print(type(my_tuple_mix))
print("--------------------")

# paranthesis is optional
my_tuple_wo_pa = 1, 2, 3
print(my_tuple_wo_pa)
print(type(my_tuple_wo_pa))
print("--------------------")

# Single Element Tuple
single_element_tuple = (1,)
print(single_element_tuple)
print(type(single_element_tuple))
print("--------------------")

# Empty Tuple
empty_tuple = ()
print(empty_tuple)
print("--------------------")

# tuple with duplicate values
my_tuple_dup = (1, 1, 1, 2, 2, 2)
print(my_tuple_dup)
print("--------------------")

# Create Tuple from tuple() funtion - constructor
my_tuple_con = tuple((1,2,3))
print(my_tuple_con)
print("--------------------")

### Create tuple from iterable like list or String using tuple() function
# create tuple from a list
my_list = [1,2,3,4]
my_tup = tuple(my_list)
print(my_tup)
print("--------------------")

# create tuple from String
my_str = "hello"
my_tu = tuple(my_str)
print(my_tu)
print("--------------------")


### Tuple Methods ###
print(dir(()))

# count method
my_tup_dup = (1, 2, 3, 3, 3, 2, 4, 1, 1)
print(my_tup_dup.count(3))
print(my_tup_dup.count(2))
print(my_tup_dup.count(1))

# index method
my_tuple = (1, 2, 3)
print(my_tuple.index(2))

# length of a tuple
my_tuple = (1, 2, 3, 4, 5)
print(len(my_tuple))

### Accessing a Tuple ###
my_tuple = (1, 2, 3)
# positive indexing
print(my_tuple[0])
print(my_tuple[1])
# negative indexing
print(my_tuple[-1])
print(my_tuple[-3])


### Slicing Tuple ###
my_tuple = (1, 2, 3, 4, 5, 6)
# Syntax - my_tuple[start:stop:step] 
# start->first index of slice  
# stop->Index where slice ends (exclusive) +1  
# step->step defines the increment between elements in the slice (optional)   
print(my_tuple[0:4:1])
print(my_tuple[0:4])
print(my_tuple[0:4:2])
print(my_tuple[0::1])
print(my_tuple[::1])
print(my_tuple[::-1])

### Tuple Unpacking ###
my_fav_langs = ("PYTHON", "JAVA", "Go")
lang1, lang2, lang3 = my_fav_langs
print(lang1, lang2, lang3)

lang, *rest = my_fav_langs
print(lang)
print(rest)

### How Tuple stores in Memory ###
mytuple = (1, 2, 3, 4)
mytuple_copy = mytuple
mytuple_same = (1, 2, 3, 4)
print(mytuple, id(mytuple))
print(mytuple_copy, id(mytuple_copy))
print(mytuple_same, id(mytuple_same))


### Why you use tuple instead of list? ###
lst = [1, 2, 3, 4, 5, 6, 7, 8]
tup = (1, 2, 3, 4, 5, 6, 7, 8)
import sys
print("Sample List Size:", sys.getsizeof(lst))
print("Sample Tuple Size:", sys.getsizeof(tup))

from timeit import timeit

print(timeit("(1, 2, 'Apify', 'Crawlee')", number=10_000_000))
print(timeit("[1, 2, 'Apify', 'Crawlee']", number=10_000_000))

### Loop Through a Tuple ###
my_tuple = (1, 2, 3)
for t in my_tuple:
    print(t)
    
for i in range(len(my_tuple)):
    print(my_tuple[i])
    
    
### in Operator in Tuple
my_tuple = (1, 2, 3, 4)
if 2 in my_tuple:
    print("number is present in tuple")
else:
    print("number is not present in tuple")

if 4 not in my_tuple:
    print("number is not present in tuple")
else:
    print("number is present in tuple")   
        

### Returning Tuples From Functions ###
#Functions can return multiple values in the form of a tuple. This is particularly useful 
#for functions that need to return more than one piece of data.
def get_info():
    name = "Prosenjit"
    age = 40
    profession = "Architect"
    return name, age, profession
result = get_info()
print(result)
print(type(result))


## Add Element to Tuple ###
# You can add an element or multiple elements to a tuple by using many ways, 
# for example, using the + operator, * unpacking

# Add two Tuples with + operator
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = tuple1 + tuple2
print("tuple3:", tuple3)

# Multiply a tuple
tuple1 = (1, 2, 3)
multi_tuple = tuple1 * 5
print("multi_tuple:", multi_tuple)

# add tuple using list.append() with one element
tuples = (1, 2, 3, 4)
list1 = list(tuples)
print(list1)
list1.append(5)
print(list1)
result = tuple(list1)
print(result)

# Using tuple concatenation
tuples = (1, 2, 3, 4)
tuples2 = tuples + (5,)
print(tuples2)
tuples3 = (0,) + tuples2
print(tuples3)

# add to tuple with unpacking
tuples = (1, 2, 3, 4)
tuples = (*tuples, 5)
print(tuples)

# Use reassignment(+=) operator
tuples = ('Python', 'Java')
tuples += ('Panadas',)
# tuples = tuples + ('Panadas',)
print(tuples)











