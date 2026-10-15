students={
    's1': {
        'name':'A',
        'python':65,
        'dbms': 55,
        'cn':45
    },
    's2':{
        'name':'B',
        'python':75,
        'dbms': 65,
        'cn':95
    },
    's3':{
        'name':'C',
        'python':85,
        'dbms': 25,            
        'cn':83
    },
    's4':{
        'name':'D',
        'python':82,
        'dbms': 35,
        'cn':86
    }
}
max=0
for s in students.values():
    total=s['python']+s['dbms']+s['cn']
    s['total']=total
    if total>max:
        max=total
        key=s

print(students)
print(f"Topper is {key['name']} and total marks is {max}")