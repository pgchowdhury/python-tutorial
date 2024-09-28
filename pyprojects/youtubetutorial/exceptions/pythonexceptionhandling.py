"""
    Author: Prosenjit Ghosh Chowdhury
    Date: 27-Sept-2024
"""
"""
    Types of Errors:
        1) Syntax Errors/Compile Time Error
        2) Logical Error
        3) Run Time Errors
"""

#### Program without exception handling ####
numerator = int(input("Please enter the numerator for division: "))
denominator = int(input("Please enter the denominator for division: "))
division = numerator/denominator
print("The result is", division)
print("Division is successful...")

print("The line of code is doing some sensitive calculation. So must execute...")


#### Program with generic Exception Handling ####
try:
    numerator = int(input("Please enter the numerator for division: "))
    denominator = int(input("Please enter the denominator for division: "))
    division = numerator/denominator
    print("The result is", division)
except Exception as e:
    print("Denominator can not be zero...", e)
else:
    print("Division is successful...")
    
print("The line of code is doing some sensitive calculation. So must execute...")


#### Program with Specific Multiple Exception Handling ####
try:
    numerator = int(input("Please enter the numerator for division: "))
    denominator = int(input("Please enter the numerator for division: "))
    division = numerator/denominator
    print("The result is", division)
    
except ZeroDivisionError as e:
    print("denominator can not be zero...", e)
except ValueError as e:
    print("Enter numbers only...", e)
except Exception as e:
    print("Some errors occurs...", e)
else:
    print("Division is successful...")
finally:
    print("close the resource")
    
print("The line of code is doing some sensitive calculation. So must execute...")


### Example Exception Handling with list or for loops ###
lst = [10, 20, 30]
try:
    num = lst[3]
except IndexError as e:
    print("Index does not exist", e)
else:
    print(num)
for index in range(4):
    try: 
        num = lst[index]
    except IndexError as e:
        print("Index does not exist", e)
    else:
        print(num)



#### More Example of Exception Handling ####
filename = "requirements.txt"
try:
    print("opening the file...")
    f = open(filename)
except FileNotFoundError as e:
   print(f"{filename} could not found! {e}")
else:
    text = f.read()
    print(text)
finally:
    f.close()
    print("closed the file")
    
print("The line of code is doing some important operation. So must execute...")


#### Nested exception handling ####
filename = "requirements.txt"
try:
    print("opening the file...")
    f = open(filename)
    try:
        text = f.read()
        print(text)
    except Exception as e:
        print(f"{filename} could not able to read! {e}")
    finally:
        f.close()
        print("closed the file...")
except FileNotFoundError as e:
    print(f"{filename} could not found! {e}")  
print("The line of code is doing some important operation. So must execute...")     


### Nested exception handling is not recommended as it makes exception handling more complex ###

#### Raising Exceptions in Python ####
# We have the option to throw an exception if certain conditions are met. It allows us to interrupt 
# the program based on our requirement. 
value = int(input("Enter value less than 10: "))
if value >= 10:
    raise ValueError("Please add number lower than 10..")
else:
    print("You Won the Bet!!!")


#### Debugging During Development With assert ####
# Python offers a specific exception type that you should only use when debugging your program during 
# development. This exception is the AssertionError. The AssertionError is special because you 
# shouldn’t ever raise it yourself using raise. Instead, you use the assert keyword to check whether 
# a condition is met and let Python raise the AssertionError if the condition isn’t met.
# In Production
number = 15
if number > 10:
    raise Exception(f"The number should not exceed 10. ({number=})")
print(number)
# In development for debuging
number = 15
assert (number < 10), f"The number should not exceed 10. ({number=})"
print(number)

"""
    Best Practices:
        1. Catch specific exceptions instead of generic Exception class to differentiate errors
        2. Print custom error messages from except blocks upon failures
        3. Use finally clause to execute sections of cleanup code reliably
        4. Define custom exception classes to match application scenarios
        5. Use try-except blocks only where needed.
            Don’t wrap your entire code in a massive try-except block; limit it to potential 
            error-prone sections.
            Don’t overuse try-except blocks in business logic to avoid hiding real issues
        6. Avoid using except: without specifying the exception type, as it can catch unintended errors.
        7. Use logging to record exceptions for later analysis.
"""

"""
    Advantage: Improved program reliability, Cleaner Code, Simplified error handling, easier debugging
    Disadvantage: Performance Overhead, Increased Code Complexity, Possible Security risks
Overall, the benefits of exception handling in Python outweigh the drawbacks, but it’s important to 
use it judiciously and carefully in order to maintain code quality and program reliability.
"""