import json

student = [
    {"ID":1,"Name":"Deva","Age":20},
    {"ID":2,"Name":"Siva","Age":21},
    {"ID":3,"Name":"Kumar","Age":22},
    {"ID":4,"Name":"Fadhi","Age":22},
    {"ID":5,"Name":"Aber","Age":22},
]
with open("stdnt.json","w") as f:
    json.dump(student,f,indent=4)

with open("stdnt.json","r") as f:
    data=json.load(f)
    
for student in data:
        print(f"ID: {student['ID']}")
        print(f"Name: {student['Name']}")
        print(f"Age: {student['Age']}")