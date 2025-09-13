weeklist=[]
while (True):
    print('week list menu')
    for i in range (1,8):
      day=int(input(f'Enter your Enter {i}day amount='))
      weeklist.append(day)
      print(f'{day} is added to the list')
      
    break
        
print("The finalized list is",weeklist)
print("The total amount for the week is",sum(weeklist))
print("The maximum amount of the week is",max(weeklist))