import json
import csv

def csv_parser(csv_file,rows):
    with open(csv_file) as f:
        reader = csv.reader(f)
        list = []
        for row in reader:
            selected_rows = []
            for i in rows:
                selected_rows.append(row[i])
            list.append(selected_rows)
        return list[0],list[1:]
         
def dict_maker(attrs, vals):
    dict = {}
    for i, att in enumerate(attrs):
        dict[att]= vals[i]
    return dict

#CSV file we are using 
csv_file = 'localcode_la.csv'
# Rows we want to keep
rows = [0,1,11,12,13,14,15,16,17]
json_name = 'localcode_la.js'

# Parse the CSV     
attrs, vals_list= csv_parser(csv_file,rows)
# Create a list of dicts
dict_list = []
for vals in vals_list:
    dict_list.append(dict_maker(attrs, vals))

# Write them into a JS file    
f = open(json_name, 'w')
f.write(json.dumps(dict_list))
f.close()
