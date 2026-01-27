from copy import copy
players=['charles','martina','michael','florence','eli']
print(players[:3])
print(players[1:4])
print(players[2:])
print(players[-3:])

for i in players[:3]:
    print(i.title())
    

print(f'the first 3 elements of the lists are :{players[:3]}')

print(f'the first 3 elements of the middle of the lists are :{players[ (int(len(players)/2) -1):(int(len(players)/2) +2)]}')

print(f'the first 3 last elements of the lists are :{players[-3:]}')
pizzaz = ['margarita','peperoni','beefalo','marina']
firend_pizzaz = pizzaz[:]
pizzaz_cop = pizzaz.copy()
pizzaz.append('chickenz')
firend_pizzaz.append('4cheese')

print(pizzaz)
print(firend_pizzaz)
print(pizzaz_cop)