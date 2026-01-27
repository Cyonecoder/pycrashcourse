for val in range (1,5):
    print(val)
for val in range (1,6):
    print(val)

numbers = list(range(1,6))
print(numbers)
even_numbers = list(range(2,11,2))
print(even_numbers)
squares = []
for value in range(1,11):
 
    squares.append(value**2)

print(squares)

digits=  list(range(1,11))
print(f'digit: {digits}')

print(min(digits))
print(max(digits))
print(sum(digits))


# small test 
for i in range (1,21):
    print(i)
    
for i in range(1,1_000_001):
    print(i)
one_million=list(range(1,1_000_001))

sum_one_million = sum(one_million)

print(sum_one_million)
print(min(one_million))
print(max(one_million))
odd_number = [val for val in range(1,21,2)]
for odd in odd_number:
    print(odd)
multiple_3 =[el for el  in range(3,31) if el%3==0 ]
for i in multiple_3:
    print(i)
    
tenth_cubes = [n**3 for n in range(1,11)]

for i in tenth_cubes:
    print(i)