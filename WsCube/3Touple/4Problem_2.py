# 2. Access the value of age from the given data. 
# Student_data = {"name": "David", "age":13,"marks":87} 

import json
Student_data = """{"name": "David", "age":13,"marks":87}"""

data = json.loads(Student_data)
print(data["age"])

