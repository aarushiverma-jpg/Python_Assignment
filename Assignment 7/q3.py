student={
    'Name':'Aarushi Verma',
    'Branch':'CSE',
    'Age':21,
    'Marks':89
}

for key in student.keys():
    if key=='Age':
        print(f"{key} is found and the value is {student[key]}")
        break
else:
    print("Age is not present in dictionary")