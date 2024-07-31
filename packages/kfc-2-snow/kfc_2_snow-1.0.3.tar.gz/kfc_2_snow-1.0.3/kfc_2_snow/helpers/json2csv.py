import json
import csv

# Read JSON data from file
with open('flat.json', 'r') as json_file:
    data = json.load(json_file)

# Define the CSV file name
csv_file = 'output.csv'

# Write data to CSV file
with open(csv_file, 'w', newline='') as csvfile:
    fieldnames = data.keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow(data)