string=input("enter the string:")
alphabet,digit,specialchar=0,0,0
for ch in string:
    if(ch.isalpha):
        alphabet+1
    elif ch.isdigit():
        digit+1
    else:
        specialcharacter+1
        print(f"count of alphabeticcharacters is {alphabet}")
        print(f"count of digits is {digit}")
        print(f"count of specialcharacters is {specialcharacter}")
             
