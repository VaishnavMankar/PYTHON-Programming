# 3. Pretty Print following JSON data.
import json
Student_data = {"name": "David", "age":13,"marks":87} 

data = json.dumps(Student_data,indent=4,separators=(",","="))
print(data)