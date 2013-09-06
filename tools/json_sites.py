import json
import csv
import os, inspect

def csv_parser(csv_file):
    with open(csv_file) as f:
        reader = csv.reader(f)
        lists = []
        for row in reader:
            selected_rows = []
            for i in range(len(row)):
                selected_rows.append(row[i])
            lists.append(selected_rows)
        return lists[0],lists[1:]
         
def dict_maker(attrs, vals):
    dict = {}
    for i, att in enumerate(attrs):
        dict[att]= vals[i]
    return dict

# This gives us the path where the file is located
path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) 
# And a list of the files in the directory
files = os.listdir(path)

# This makes a list of the csv files in the directory
csv_files = []
for file in files:
    if file[-3:] == 'csv':
        csv_files.append(file)
print csv_files

for csv_file in csv_files:
    #CSV file we are using 
    # JSON name
    json_name = csv_file[:-4] + '.json'#'localcode_la.json'
    
    # Parse the CSV     
    attrs, vals_list= csv_parser(csv_file)
    # Create a list of dicts
    dict_list = []
    for vals in vals_list:
        dict_list.append(dict_maker(attrs, vals))
    
    # Write them into a JS file    
    f = open(json_name, 'w')
    f.write(json.dumps(dict_list))
    f.close()
