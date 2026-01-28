# car = 'subaru'
# print("Is car == subaru ? I predict True.")
# print(car =='subaru')

# print("\nIs car == audi ? I predict false.")
# print(car=='audi')
# no need for 10 test come on 

a='aaaa'
a_bool= a == "aAaa"

print('aaaa' == "aaaaa")
a_lower = "aAAA".lower()
print(a==a_lower)

if len(a)>=10:
    print('greater')
if len(a)<10:
    print('lower')
    
if a_lower ==a and len(a)<=4 or  a_bool:
    print('yes')
else:
    print('no')
    
my_list= ["a","b","c",'d']

if "a" in my_list:
    print('exist')
if 'z' not in my_list:
    print('not exist ')
colors=['green','yellow','red']
allien_color ='blue'

if allien_color in colors and allien_color =='green':
    print('You earned 5 points')
elif allien_color in colors:
    print('You earned 10 points')
else:
    print('no Out put ')
    
    
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")