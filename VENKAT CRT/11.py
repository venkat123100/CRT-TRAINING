n=int(input("enter the integer value"))
print(f"even numbers from 1 to {n}:")
for i in range(2,n+2,2):
               print(i) 

n=int(input("enter the integer value"))
print(f"even numbers from 1 to {n}:")
for i in range(n,0,-1):
    if(i%2==0):
               print(i)              