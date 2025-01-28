# 1. Convert the following dictionary into JSON format.
# Student_data = {"name": "David", "age":13,"marks":87}

import json
Student_data = {"name": "David", "age":13,"marks":87}
print(type(Student_data))
data = json.dumps(Student_data)
print(data)
print(type(data))


