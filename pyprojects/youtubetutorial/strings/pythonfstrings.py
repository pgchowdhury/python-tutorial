"""
    Author: Prosenjit Ghosh Chowdhury
    Date: 23-August-2024
"""
# 3.6 release introduced formatted String literals, simple called f-String
# We use letter f or F to create a f-string - More readable, faster and versatile

# Basic Usages - variable interpolation - dynamic values in the text
# format String using Variable in String
name = "Prosenjit"
age = 40
my_str = f"My name is {name} and I am {age} years old."
print(my_str)

# Multiline String : for Structured text
multiline_text = f"""Hello ! How are you? I am doing great..
        Hope, you are doing well !! See you tomorrow ..
        Bye, Take Care"""
print(multiline_text)

# Advanced Usage - Dynamic Code Genration
operation = "multiply"
a = 10
b = 20
code = f"""
def dynamic_function(x, y):
    return x * y if '{operation}' == 'multiply' else x + y

result = dynamic_function({a}, {b})
result_str = 'the result is'
print(result_str, result)
"""
exec(code)

# Advanced Usage - Creating Command Line Tool
command = "ls"
path = "/Users/prosenjitghoshchowdhury"
options = "-la"
shell_command = f"{command} {path} {options}"
print(f"Executing: {shell_command}")

# Expressions Interplolation within F-Strings.Evaluate any expressions directly in curly braces
a = 10
b = 5
add = f"The sum of (a+b) is {a+b}."
print(add)

# Conditional Statement in F-String
number = 10
check_even = f'{number} is a {"Even" if (number%2)==0 else "Odd"} number'
print(check_even) 

# Call Functions - You can even call functions in F-String
def square(num):
    return num * num
sq = f"The Square of 7 is {square(7)}"
print(sq)

my_name = "Prosenjit"
print(f"My name is {my_name.upper()}")

# String Formatting with F-Strings alignment
name = "Prosenjit"
age = 40
str_normal = f"Name: {name} Age: {age}"
print(str_normal)
str_left_align = f"Name: {name:<20} Age: {age}"
print(str_left_align)
str_right_align = f"Name: {name:>20} Age: {age}"
print(str_right_align)
str_center_align = f"Name: {name:^20} Age: {age}"
print(str_center_align)

# Number Formatting in F-String
num = 1000000000
print(num)
formatted_number = f"Formatted: {num:,}"
print(formatted_number)

number = 123.456789

# number to 2 decimal places
format_float = f"Rounded: {number:.2f}"
print(format_float)

# number to the nearest integer
format_integer = f"Integer: {number:.0f}"
print(format_integer)

# Format the number as a percentage with no decimal places
format_percentage = f"Percentage: {number:.0%}"
print(format_percentage)

# scientific notation with 2 decimal places
format_scientific = f"Scientific: {number:.2e}"
print(format_scientific)

# general format with 4 significant digits
format_general = f"General: {number:.4g}"
print(format_general)

# using Date Time inside F-String
import datetime
today = datetime.datetime.today()
print(f"{today: %B %d %Y}")
print(f"{today: %b %d %Y}")
print(f"{today: %m %d %Y}")
print(f"{today: %B %d %Y %H %M %S %p}")
print(f"{today: %B %d %Y %I %M %S %p}")

# F-Strings in Logging
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
planet = "World"
logger.info(f"hello {planet}")