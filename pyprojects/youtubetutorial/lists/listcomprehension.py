"""
    Author: Prosenjit Ghosh Chowdhury
    Date: 08-Aug-2024
"""

# UC 1 - square the value of a list
numbers = [ 10, 20, 30, 40, 50, 60 ]
sq_numbers = []
for num in numbers:
    sq_numbers.append(num * num)
print(sq_numbers)

# Using list comprehension
# Syntax: variable = [ new item for item in List ]
sq_numbers_comp = [ num * num for num in numbers ]
print(sq_numbers_comp)




# UC 2: find the even numbers and add to a list from the range of numbers 1 to 50
ev_num = []
for num in range(1, 51):
    if (num % 2 == 0):
        ev_num.append(num)
print(ev_num)

# Using list comprehension
# Syntax: variable = [ new item for item in List if condition]
ev_num_comp = [ [num for num in range(1, 51) if (num%2 == 0) ]
print(ev_num_comp)




# UC 3: create a new list with even number and gretter then 10 and less than 50
numbers = [1, 3, 4, 10, 20, 223, 22, 42, 92, 64, 63, 5, 43, 42, 49]
new_num = []
for num in numbers:
    if (10 < num < 50):
        if (num % 2 == 0):
            new_num.append(num)
print(new_num)

# Using list comprhension
# Syntax: variable = [ new item for item in List if condition if condition ]
new_num_comp = [ num for num in numbers if (10 < num < 50) if (num % 2 ==0) ]
print(new_num_comp)




# UC 4: add the positive items price to a list and add 0 for negative ones
original_price = [ 5.26, 10.36, 9.34, -5.32, 2.34, -6.72, -9.0]
new_ori_list = []
for price in original_price:
    if (price > 0):
        new_ori_list.append(price)
    else: 
        new_ori_list.append(0)
print(new_ori_list)

# Using list comprehension
# Syntax: variable = [ new item if (condition) else other item for item in List ]
new_ori_list_comp = [ price if (price > 0) else 0 for price in original_price ]
print(new_ori_list_comp)




# UC 5 - create a flat new list from a nested list matrix
matrix = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]
flat_list = []
for lst in matrix:
    for num in lst:
        flat_list.append(num)
print(flat_list)

# Using list comprehension
# Syntax: variable = [ new item for list in matrix for item in list ]
flat_list_comp = [ num for lst in matrix for num in lst ]
print(flat_list_comp)




# UC 6: convert each item from a list in uppercase
animals = ["cat", "dog", "tiger", "lion", "deer", "monkey"]
up_animals = []

def upper_case(item):
    return item.upper()
    
for item in animals:
    up_animals.append(upper_case(item))
print(up_animals)

# Using list comprehension
# Syntax: variable = [ function(item) for item in list ]
up_animals_comp = [ upper_case(item) for item in animals ]
print(up_animals_comp)




# UC 7: Separate the word with Space which have uppercase letter
str = "HelloThisIsProsenjit"
str_comp = ''.join([ l if (l.islower()) else " " + l for l in str])[1:]
print(str_comp)