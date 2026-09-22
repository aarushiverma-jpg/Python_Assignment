name=input("Enter the name: ")
gender=input("Enter the gender: ")

item1=int(input("Enter the 1st itme quantity: "))
item2=int(input("Enter the 2nd itme quantity: "))
item3=int(input("Enter the 3rd itme quantity: "))
item4=int(input("Enter the 4th itme quantity: "))
item5=int(input("Enter the 5th itme quantity: "))
item6=int(input("Enter the 6th itme quantity: "))
item7=int(input("Enter the 7th itme quantity: "))
item8=int(input("Enter the 8th itme quantity: "))
item9=int(input("Enter the 9th itme quantity: "))
item10=int(input("Enter the 10th itme quantity: "))
carry_bag=input("Do you need carry bag:")

actual_item5=(50*item5) - (50*item5)*0.1
actual_item10=(100*item10) - (100*item10)*0.15

total_bill=(10*item1) + (20*item2) + (30*item3) + (40*item4) + actual_item5 + (60*item6) + (70*item7) + (80*item8) + (90*item9) + actual_item10

actual_bill=(10*item1) + (20*item2) + (30*item3) + (40*item4) + (50*item5) + (60*item6) + (70*item7) + (80*item8) + (90*item9) + (100*item10)

actual_item1=10*item1

if(item1>4):
    actual_item1=(10*item1)-(10*item1)*0.05
    total_bill-=actual_item1


gst=(total_bill*0.1)
total_bill= total_bill + gst
actual_bill=actual_bill+gst

if(carry_bag=="yes"):
    total_bill+=10
    actual_bill+=10


if(gender=="female"):
    gift="cadbury"
elif(gender=="male"):
    gift="laser wallet"
else:
    gift="No gift"

if(total_bill>10000):
    total_bill-=total_bill*0.15
elif(total_bill>=5000 and total_bill<=10000):
    total_bill-=total_bill*0.1

print("GENERATED BILL:")

print("\t\t\t\tD-Mart")
print(f"Name: {name}\t\t\t\t\t\t Date:14/09/2026")
print("-------------------------------------------------------------------------")
print("Item Name\tQuantity\tPrice\t\tTotal\t\tAfter-discount")
print(f"Item-1\t\t{item1}\t\t10\t\t{item1*10}\t\t{actual_item1}")
print(f"Item-2\t\t{item2}\t\t20\t\t{item2*20}\t\t{item2*20}")
print(f"Item-3\t\t{item3}\t\t30\t\t{item3*30}\t\t{item3*30}")
print(f"Item-4\t\t{item4}\t\t40\t\t{item4*40}\t\t{item4*40}")
print(f"Item-5\t\t{item5}\t\t50\t\t{item5*50}\t\t{actual_item5}")
print(f"Item-6\t\t{item6}\t\t60\t\t{item6*60}\t\t{item6*60}")
print(f"Item-7\t\t{item7}\t\t70\t\t{item7*70}\t\t{item7*70}")
print(f"Item-8\t\t{item8}\t\t80\t\t{item8*80}\t\t{item8*80}")
print(f"Item-9\t\t{item9}\t\t90\t\t{item9*90}\t\t{item9*90}")
print(f"Item-10\t\t{item10}\t\t100\t\t{item10*100}\t\t{actual_item10}")
print("-------------------------------------------------------------------------")
print("\t\t\t\t\t\tA.P\t\tD.P")
print(f"\t\t\t\t\t\t{actual_bill}\t\t{total_bill}")
print(f"Gift: {gift}\t\t\t\t\t0.00\t\t0.00\n")
print(f"Carry bag:{carry_bag}\t\t\t\t\t10.00\t\t10.00")
print(f"GST (10%) :\t\t\t\t\t{gst}\t\t{gst}")
print("-------------------------------------------------------------------------")
print(f"\t\t\t\t\t\t{actual_bill}\t\t{total_bill}\n")
print("\t\t\t\tThank You")
print("\t\t\t\t To Vist")
print("\t\t\t\t  D-Mart")