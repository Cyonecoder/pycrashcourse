invited_persons =['p1','p2','p3','p4']

for n in invited_persons:
    print(f'{n} You are invited to dinner  ')
    
    
    
print(f'{invited_persons[1]} cant make it to dinner')

invited_persons[1] ='replace 2'
for n in invited_persons:
    print(f'{n} You are invited to dinner  ') 
    
    
print("found a bigger table ")


invited_persons.insert(0,'h1')
invited_persons.insert(int(len(invited_persons)/2),'middle h-midle')
invited_persons.append('MO')


for n in invited_persons:
    print(f'{n} You are invited to dinner  ')
    
    
print('invite only two people for dinner.')

while len(invited_persons)>2:
    
    invited_persons.pop()
    
for n in invited_persons:
    print(f'{n} You are invited to dinner  ') 
    
del invited_persons[1]
del invited_persons[0]
print(invited_persons)