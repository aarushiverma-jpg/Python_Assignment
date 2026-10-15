student={
    'Name':'Aarushi Verma',
    'Branch':'CSE',
    'Age':21,
    'Marks':89
}

print("Before poping")
print(student)
print("After poping")

key_exist=student.pop('Branc',0)

if  key_exist:
    print(student)
else:
    print("Key not found..")
    print(student)