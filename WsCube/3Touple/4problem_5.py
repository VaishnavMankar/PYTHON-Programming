# 5. Access the nested key marks from the following nested data
# """{"student":{
#       "grade":{
#         "name": "David",
#           "marks"0:{
#             "math":87, }
#          }
#     }"""
import json

student_data = """{
    "student": {
        "grade": {
            "name": "David",
            "marks": {
                "math": 87
            }
        }
    }
}"""

data = json.loads(student_data)
print(data["student"]["grade"]["marks"]["math"])
