"""
    Author: Prosenjit Ghosh Chowdhury
    Date: 17-August-2024
"""
greet = "HELLO WORLD!"
print(greet)
greet = 'HELLO WORLD!'
print(greet)
car = "This is Prosenjit's Car"
print(car)
multiline_text = """Hello ! How are you? I am doing great..
Hope, you are doing well !! See you tomorrow ..
Bye, Take Care"""
print(multiline_text)

#### Test to find how python strings are stored in memory ####

print("greet", id(greet))
print(sys.getrefcount(greet))

greet2 = greet
print("greet2", id(greet2))
print(sys.getrefcount(greet))

greet3 = "HELLO WORLD!"
print("greet3", id(greet3))
print(sys.getrefcount(greet))

greet3 = "Hello Prosenjit"
print(greet3)
print("greet3", id(greet3))

### String Formatting ###
fname = "Prosenjit"
lname = "Ghosh Chowdhury"
fullname = "My name is " + fname + " " + lname + "."
fullname = f"My name is {fname} {lname}."
print(fullname)

### String Methods ###
print(fname)
print(dir(fname))
print(fname.upper())
print(fname.lower())
print(fname.lstrip())
l = fullname.split()
print(l)






# print(greet[0:5:1])
# print(greet[1:11:2])
# print(greet[:])
# print(greet[::-1])


















# greet = 'HELLO WORLD!'
# print(greet)
# car = "This is Prosenjit's Car"
# print(car)
# multiline_text = """Hello ! How are you? I am doing great..
# Hope, you are doing well !! See you tomorrow ..
# Bye, Take Care"""
# print(multiline_text)
