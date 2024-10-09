"""
    Author: Prosenjit Ghosh Chowdhury
    Date: 05-Oct-2024
"""
### r+ mode ###
with open("filesio/filer+.txt", "r+") as fr:
     text = fr.read()
     print(fr.tell())
     print(text)
     fr.seek(12)
     fr.write(" New Text")
     

try:
    with open("filesio/filer+.txt", "r+") as fr:
     text = fr.read()
     print(fr.tell())
     fr.write(" new text")
except FileNotFoundError as e:
    print("File not Exist.", e)
except Exception as e:
    print("Error came.", e)


lst = ["This will Overwrite 1\n", "This will Overwrite 2\n", "This will Overwrite 3\n"
       , "This will Overwrite 4"]
### w+ mode ###
with open("filesio/filew+.txt", "w+") as fw:
     print(fw.tell())
     #fw.write("This will Overwrite")
     fw.writelines(lst)
     print(fw.tell())
     fw.seek(0)
     text2 = fw.read()
     print(text2)


# ### a+ mode ###
with open("filesio/filea+.txt", "a+") as fa:
     print(fa.tell())
     fa.write(" This will append 3")
     print(fa.tell())
     fa.seek(0)
     text3 = fa.read()
     print(text3)