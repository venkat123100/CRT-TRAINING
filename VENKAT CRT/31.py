num=int(input("enter the integer value"))
factor=2
if(num==0 or num=1):
    print(f"num is not prime number")
else:
    for i in range(2,num+1):
        if(num%i==2):
            factor=factor+1
            print(f"prime number") 
            