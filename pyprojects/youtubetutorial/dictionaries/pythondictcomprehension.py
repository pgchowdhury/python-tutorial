"""
    Author: Prosenjit Ghosh Chowdhury
    Date: 06-Sept-2024
"""
### Dictionary Comprehensions from one Iterable ###
## dict = {key: expression for iter var in iterable} ##
# create a dictionary from the below list where key will be fruit name and value 
# will be length (number of characters) of each fruit name
fruits = [ "apples", "pineapple", "blueberry", "pears"]
my_fruit_dict_for = {}
for word in fruits:
    my_fruit_dict_for[word] = len(word)
print(my_fruit_dict_for)
my_fruit_dict = { word: len(word) for word in fruits }
print(my_fruit_dict)

# create a dictionary from the below dictionary where value will be square of current value
## dict = { key: expression for (key,val) in iterable }
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(my_dict.items())
my_dict_square = {key: val**2 for key, val in my_dict.items()}
print(my_dict_square)

### Dictionary Comprehensions from two Iterables example two lists ###
## dict = {key: expression for (key,val) in zip(list1, list2)} ##
hp_chars = ['Harry Potter', 'Ron Weasley', 'Hermione Granger', 'James Potter', 'Snape', 
            'Albus Dumbledore', 'Luna Lovegood', 'Draco Malfoy', 'Cedric Diggory']
hp_chars_houses = ['Gryffindor', 'Gryffindor', 'Gryffindor', 'Gryffindor', 'Slytherin', 
                   'Gryffindor', 'Ravenclaw', 'Slytherin', 'Hufflepuff']
hp_dict = {chars: houses for chars, houses in zip(hp_chars, hp_chars_houses)}
print(hp_dict)

### Dictionary Comprehensions with If Condition ###
## dict = {key: expression for (key,val) in iterable if condition} ##
# Create dictionary with square of range on 20 for even numbers only
dict_square = { number: number**2 for number in range(1, 21) if number%2 == 0 } 
print(dict_square)


### Dictionary Comprehensions with multiple If Conditions ###
## dict = {key: expression for (key,val) in iterable if condition if condition} ##
# Create dictionary with square of range on 20 for even numbers only and number > 5
dict_square_5 = { number: number**2 for number in range(1, 21) if number%2 == 0 if number >5 } 
print(dict_square_5)


### Dictionary Comprehensions with If Else Conditions ###
## dict = { key: if/else for (key,val) in iterable} ##
cities = ["Kolkata", "New Delhi", "Shimla", "Dehradun"]
temp = [35, 40, 20, 22]
# create a dict where cities are key and values are hot when temp >30 else pleasant
dict_city_weather = {city: "Hot" if t >30 else "Pleasant" for (city, t) in zip(cities, temp)}
print(dict_city_weather) 


### Dictionary Comprehensions with function ###
## dict = { key: func(val) for (key, val) in iterable}
cities = ["Kolkata", "New Delhi", "Shimla", "Dehradun"]
temp = [35, 40, 20, 22]
def weather(temp):
    if temp > 30:
        return "Hot"
    else:
        return "Pleasant"
dict_city_w = {city: weather(t) for (city, t) in zip(cities, temp)}
print(dict_city_w)
