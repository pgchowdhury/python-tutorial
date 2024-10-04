"""
    Author: Prosenjit Ghosh Chowdhury
    Date: 02-Oct-2024
"""
# File Types: Text Files: .txt, .doc. .log etc  Binary Files: .mov, .mp4, .jpeg, .png etc.
### Files I/O Operations in Python ###
# read, write, rename, delete, directories operations etc.


### Open --> Read --> Close ###
### open(file_name, mode) ###
f = open("filesio/files_smalltext.txt", "r")
# File Current Postions - fileobject.tell()
print("Current Position",f.tell())
# Read a file - fileobject.read([count])
text = f.read()
print(text)
# File Current Postions - fileobject.tell()
print("Current Position",f.tell())
# Change the Current Postion - fileobject.seek(offset, whence)
f.seek(48)
# File Current Postions - fileobject.tell()
print("Current Position",f.tell())
print(f.read())
# File Current Postions - fileobject.tell()
print("Current Position",f.tell())
# Close a file
f.close()

f = open("filesio/files_smalltext.txt", "r")
text = f.readlines()
print(type(text))
print(text)
f.close()


### It is good practice to use the with keyword when dealing with file objects. The advantage is that 
# the file is properly closed after its suite finishes, even if an exception is raised at some point. ###
with open("filesio/files_1.txt", "r") as f:
    read_data = f.read()
    print(read_data)
    
print(f.closed)


### Write to a file ###
fw = open("filesio/filew_3.txt", "w")
fw.write("Hello, how are you?")
print(fw.closed)
fw.close()
print(fw.closed)

### Write to a file using with method ###
with open("filesio/filew_3.txt", "w") as fw2:
    fw2.write("I am doing great")
print(fw2.closed)


### Append to a file ###
fa = open("filesio/filew_4.txt", "a")
fa.write("Hello, how are you? ")
fa.write("I am doing great. ")
fa.close()


# # ### Append to a file using with method ###
with open("filesio/filew_4.txt", "a") as fa2:
    fa2.write("The weather is great today..")


### Read a Binary file - a image ###
with open("filesio/test.jpg", "rb") as fb:
    imageb = fb.read()
    print(imageb)
