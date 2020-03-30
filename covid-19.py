import csv
import urllib
from urllib.request import urlopen
from io import StringIO

fields = []
rows = []
    
data = urlopen("https://drive.google.com/uc?export=download&id=1iWJ9qHHz8kMCRhA0IUNgj2qODVdR5AVk").read().decode('ascii', 'ignore')

datafile = StringIO(data)

# creating a csv reader object 
csvreader = csv.reader(datafile)

# extracting field names through first row 
fields = csvreader.__next__()

# extracting each data row one by one 
for row in csvreader:
    rows.append(row)

# get total number of rows 
print("Total number of rows: %d"%(csvreader.line_num))

# printing the field names
print('Field names are:' + ', '.join(field for field in fields))

#  printing first 5 rows 
print('\nFirst 5 rows are:\n') 
for row in rows[:15]: 
    print('Row contains:' + ', '.join(col for col in row))

