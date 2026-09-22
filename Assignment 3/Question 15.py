cost=int(input("Enter the cost of bike:"))
if(cost>100000):
    print("Rod tax to be paid is 15%")
elif(cost<=100000 and cost>50000):
    print("Rod tax to be paid is 10%")
elif(cost<=50000):
    print("Rod tax to be paid is 5%")