# 4. Sort the following JSON keys and write them into a file. 

import json
Student_data = {"name": "David", "age":13, "marks":87}
f = open("demo.json","w")
data = json.dumps(Student_data,indent=4,sort_keys=True)
f.write(data)

print("The data has been added to the file")