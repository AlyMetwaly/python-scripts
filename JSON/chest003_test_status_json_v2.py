import json 
import itertools
  
  
# the file to be converted to  
# json format 
filename = 'REPORT/chest003_test_status.txt'
  
# dictionary where the lines from 
# text will be stored 
dict1 = {} 
dict1["regressiontestcases"] = []
  
# creating dictionary 
with open(filename) as fh:
    for line in itertools.islice(fh, 2, None, None):
        #print(line)
        # split each line into the needed word
        dict1["regressiontestcases"].append({
            "name" : line.split()[0],
            "result" : line.split()[2].upper()
        })
        #print(dict1)

out_file = open("REPORT/chest003_test_status.json", "w")
json.dump(dict1, out_file, indent = 4, sort_keys = False)
#out_file.write(",\n")
out_file.close()