"""
    Author: Prosenjit Ghosh Chowdhury
    Date: 19-Oct-2024
"""
# What is CSV?
# Read CSV file with Reader Method
# Write CSV file with Writer
# Read CSV file with Dictionary Method
# Write CSV file with Dictionary Method
# Write a Dictionary to a CSV file


import csv

# read a CSV file with reader method
with open("filesio/movies_quote.csv", "r") as rcsv:
    # csv.reader() is used to read the file, which returns an iterable reader object.
    csv_reader = csv.reader(rcsv, skipinitialspace=True, quoting=csv.QUOTE_ALL)
    print(csv_reader)
    
    # extracting field names through first row - next() function returns the next item from the iterator
    fields = next(csv_reader)
    print(fields)
    for line in csv_reader:
        print(line)

    
        
# read a csv file and print only 5 rows 
rows = []
with open("filesio/movies.csv", "r") as rcsv:
    csv_reader = csv.reader(rcsv)
    fields = next(csv_reader)    
    for line in csv_reader:
        rows.append(line)
print(fields)
print(len(rows))
for row in rows[5:10]:
    print(row)


# write a CSV file after read from another
with open("filesio/movies.csv", "r") as rcsv:
    csv_reader = csv.reader(rcsv)
        
    fields = next(csv_reader)
    with open("filesio/movies_2.csv", "w") as wcsv:
        csv_writer = csv.writer(wcsv)
        csv_writer.writerow(fields)
        count = 0
        # for line in csv_reader:
        #     count += 1
        #     csv_writer.writerow(line)
        #     if count==5:
        #         break
        csv_writer.writerows(csv_reader)
        


# Write a CSV file with tab delimited and rows between 5 to 10
rows = []
with open("filesio/movies.csv", "r") as rcsv:
    csv_reader = csv.reader(rcsv)
    # csv fields
    fields = next(csv_reader)
    for line in csv_reader:
        rows.append(line)
with open("filesio/movies_3.csv", "w") as wcsv:
    csv_writer = csv.writer(wcsv, delimiter=",")
    csv_writer.writerow(fields)
    for row in rows[5:10]:
        csv_writer.writerow(row)
    
 
# read csv file with dictionary method
with open("filesio/movies.csv", "r") as rcsv:
    csv_reader = csv.DictReader(rcsv)
    fields = next(csv_reader)
    print(fields)
    for line in csv_reader:
        print(line["Film"], line["Audience score %"])    



# Write CSV file with Dictionary method
rows = []
with open("filesio/movies.csv", "r") as rcsv:
    csv_reader = csv.DictReader(rcsv)
    fields = next(csv_reader)    
    for line in csv_reader:
        rows.append(line)
# writing now
with open("filesio/movies_dict.csv", "w") as wdcsv:
    csv_writer = csv.DictWriter(wdcsv, fieldnames=fields)
    # Write header
    csv_writer.writeheader()
    # csv_writer.writerows(rows)
    for row in rows[10:20]:
        csv_writer.writerow(row)


# Write a Dictionary to a CSV file
mydict = [{'Name': 'Prosenjit', 'Age': '40',
           'Computer-Language': "Java"},
          {'Name': 'Atreyee', 'Age': '15',
           'Computer-Language': "Java"},
          {'Name': 'Artrika', 'Age': '11',
           'Computer-Language': "Python"}]

# field names
fields = ['Name', 'Age', 'Computer-Language']

with open("filesio/my_dict.csv", "w") as wdcsv:
    csv_writer = csv.DictWriter(wdcsv, fieldnames=fields)
    csv_writer.writeheader()
    csv_writer.writerows(mydict)
