import csv
import urllib
from urllib.request import urlopen
from io import StringIO

data = urlopen("https://drive.google.com/uc?export=download&id=1iWJ9qHHz8kMCRhA0IUNgj2qODVdR5AVk").read().decode('ascii', 'ignore')

datafile = StringIO(data)

csvReader = csv.reader(datafile)

for row in csvReader:
        print(row)

