str="helloeh"
d={}

for s in str:
    if s in d:
        d[s]+=1
    else:
        d[s]=1

for key in d.keys():
    if d[key]==1:
        print(f"First Non repeating letter is : {key}")
        break
else:
    print("All letter is repeating...")