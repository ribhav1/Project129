import csv
import string
import pandas as pd

dataset1 = []
dataset2 = []

with open('E:/ClassProjects/Normal/Project129/venv/brightest_stars.csv', 'r', encoding = 'utf8') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset1.append(row)

with open('E:/ClassProjects/Normal/Project129/venv/brown_dwarf_stars.csv', 'r', encoding = 'utf8') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset2.append(row)

headers_1 = dataset1[0]
planet_data_1 = dataset1[1:]

headers_2 = dataset2[0]
planet_data_2 = dataset2[1:]

headers = ['name', 'distance', 'mass', 'radius', 'star']
planet_data = []

# Merging data
for i in planet_data_1:
    planet_data.append(i)

for i in planet_data_2:
    planet_data.append(i)

# Deleting all empty lists in nested list
planet_data = [x for x in planet_data if x]

with open('total_stars.csv', 'w', encoding = 'utf8') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)

df = pd.read_csv('total_stars.csv', header=0)
