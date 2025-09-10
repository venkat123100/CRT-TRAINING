bill=float(input("enter the total bill amount:"))
if bill>1000:
    print("bill*10/100")
elif bill>500:
    print("bill*20/100")
else bill<=500:
     print(" no discount")    