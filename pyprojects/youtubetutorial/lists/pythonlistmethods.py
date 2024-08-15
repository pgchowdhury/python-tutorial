"""
    Author: Prosenjit Ghosh Chowdhury
    Date: 14-Aug-2024
"""

# get all methods from list
# i = 0
# for method in dir(list):
#     if '__'not in method:
#         i += 1
#         print(f'# {i}. {method}')
#         print()

# 1. append
fruit = ["apple", "mango", "orange"]
print("Orignal List", fruit)
fruit.append("peers")
print("after append", fruit)

# 2. clear
fruit = ["apple", "mango", "orange"]
print("Original list", fruit)
fruit.clear()
#del fruit[:]
print("after clear", fruit) 

# 3. copy
a = ["apple", "mango","banana", "orange"]
b = a.copy()
a[0] = "litchi"
print('a', a)
print('b', b)

# deepcopy()
import copy
c = [["apple", "mango"],["banana", "orange"]]
d = copy.deepcopy(c)
c[0][0] = "litchi"
print('c', c)
print('d', d)

# 4. count
fruit = ["apple", "mango", "orange", "apple", "lichi", "mango", "mango"]
print(fruit.count("mango"))

# 5. extend
a = [1, 3, 4, 5]
b = [7, 8, 9]
a.extend(b)
#a.append(b)
print(a)

# 6. index
fruit = ["apple", "mango", "orange"]
print(fruit.index("mango"))

# 7. insert
fruit = ["apple", "mango", "orange"]
fruit.insert(1, "strwaberry")
print(fruit)

# 8. pop
fruit = ["apple", "mango", "orange", "lichi", "strawbeery"]
#fruit.pop()
fruit.pop(1)
print(fruit)

# 9. remove
fruit = ["apple", "mango", "orange", "lichi", "strawbeery"]
fruit.remove("orange")
print(fruit)

# 10. reverse
fruit = ["apple", "mango", "orange", "lichi", "strawbeery"]
#fruit.reverse()
reversed_list = fruit[::-1]
print(reversed_list)
print(fruit)

# 11. sort
fruit = ["apple", "mango", "orange", "lichi", "strawbeery"]
#fruit.sort(reverse=False, key=len)
fruit_sorted = sorted(fruit, reverse=True, key=len)
print(fruit)
print(fruit_sorted)