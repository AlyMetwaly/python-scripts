import json 
import itertools
  
  
# the file to be converted to  
# json format 
filename = 'regression_report.txt'
  
# dictionary where the lines from 
# text will be stored 
dict1 = {"name","result"} 
  
# creating dictionary 
with open(filename) as fh:
    for line in itertools.islice(fh, 46, None):
        print(line)
        # reads each line and trims of extra the spaces  
        # and gives only the valid words 
        dict1[name] = line.strip().split(None, 1) 
        #print(dict1)
  
# creating json file 
# the JSON file is named as test1 
out_file = open("regression.json", "w") 
json.dump(dict1, out_file, indent = 4, sort_keys = False) 
out_file.close() 