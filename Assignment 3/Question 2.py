quantity=int(input("Enter the quantity purchased:"))
cost=quantity*100
if(cost>1000):
    cost=(cost*0.9)
else:
    cost=cost
print(f"Total cost of user is {cost}")