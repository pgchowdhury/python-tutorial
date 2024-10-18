"""
    Author: Prosenjit Ghosh Chowdhury
    Date: 13-Oct-2024
"""
### Read content from one file and write it into another file and read it from there ###
with open("filesio/test_1.txt", "r") as fr:
    with open("filesio/test_write1.txt", "w+") as fw:
        for line in fr:
            fw.write(line)
        fw.seek(0)
        print(fw.read())
        
            
### How to check file size, creation date in Python? How to rename file in Python? ###
from datetime import datetime
def format_datetime(date_time):
    f_date_time = datetime.fromtimestamp(date_time).strftime('%Y-%m-%d %H:%M:%S')
    return f_date_time
import os  
print(os.path.getsize("filesio/test_1.txt"))
creation_date = os.path.getctime("filesio/test_1.txt")
modification_date = os.path.getmtime("filesio/test_1.txt")
print("file creation date", format_datetime(creation_date))
print("file modification date", format_datetime(modification_date))
os.rename("filesio/test_1.txt", "filesio/test_2.txt")


### Count number of characters in a text file ###
with open("filesio/test_1.txt", "r") as fr:
    text_str = fr.read()
    print(f'The text file has {len(text_str)} characters')
    
    
### Count number of lines in the text file ###
with open("filesio/test_1.txt") as fr:
    text_lst = fr.readlines()
    print(text_lst)
    print(f'The text file has {len(text_lst)} lines.')
    
    
### Count number of words in a text file ###
with open("filesio/test_1.txt") as fr:
    text_str = fr.read()
    text_lst = text_str.split(' ')
    print(text_lst)
    print(f'The text file has {len(text_lst)} words.')


### Count to number of alphabets, digits, Special Characters and Spaces in a text file ###
with open("filesio/test_1.txt") as fr:
    text_str = fr.read()
    alphabets, digits, sc, space = 0, 0, 0, 0
    for ch in text_str:
        if ch.isalpha():
            alphabets += 1
        elif ch.isdecimal():
            digits += 1
        elif ch.isspace():
            space += 1
        else:
            sc += 1
    print(f'Alphabets: {alphabets} Digits: {digits} Spaces: {space} Special Ch: {sc}')


### Count the number of volwels and consonants in a file ###
v_lst = ['a', 'e', 'i', 'o', 'u']
vo, co = 0, 0
with open("filesio/test_1.txt") as fr:
    text_str = fr.read()
    for ch in text_str:
        if ch in v_lst:
            vo += 1
        elif ch.isalpha():
            co += 1
    print(f'Vowels: {vo}  Consonents: {co}')

            
