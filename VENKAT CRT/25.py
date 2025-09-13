cr=int(input('Enter the one coffee rate--'))
sr=int(input('Enter the snacks rate--'))
nc=int(input('Enter no.of.coffees ordered='))
ns=int(input('Enter no.of.snacks ordered='))
print(f'The amount for coffee={cr*nc}')
print(f'The amount for snacks={sr*ns}')
a=cr*nc
b=sr*ns
print('The Amount should paid along with 5% service charges is...')
print(a+b+((a+b)*0.05))
