#lists
cart = ["apples", "bananas", "cherries"]
print(cart)

#cart.apppend is how you add.remove. and sort elements to the list
cart.append("donuts")
cart.append("eggs")
cart.append("flour")
print(cart)

if "cherry" in cart:
    cart.remove("cherry")
print(cart)

cart.pop(2) #pop is like FIFO first in first out, it removes the index
print(cart)
cart.pop()
print(cart)

cart.reverse()
print(cart)

cart.sort()
print(cart)
#append always adds it to the end of an index element
cart.append("bananas")
cart.append("grapes")
cart.append("oranges")
print(cart)

fruit_basket=cart[3:]
print(fruit_basket)
print(cart)


#new list
squares=[]
for i in range(1,11):
    squares.append(i*i)
print(squares)

#list comprehension
squares = [i*i for i in range(1,11)]
print(squares)

print(cart) 

b_items =[item for item in cart if item.startswith('b')]
print(b_items)

list =['1', '10', '190']
num_list=[int (x) for x in list]
print(num_list)

#create another list

inventory = [0]*len(cart) #have to give a default value
print(inventory)
inventory[0]=1
print(inventory)

# sets {}
empty = set()
nums_set={1,1,3,4}
nums_set.add(5)
nums_set.add(10)
print(nums_set)
list = [1,2,2,2,3,3,4]
unique=set(list)
print(unique)
print(unique)

st={4,10,3,7,8}
print(st)
sorted(st)
print(st)

#DICTIONARIES
fav_snacks= {}
fav_snacks={
    "kathleen": "tortilla chips",
    "ava": "chex mix",
    "emily":"buffalo chicken dip",
    "isa": "pretzels"
}
print(fav_snacks)
fav_snacks["lucas"]="chocolate"
print(fav_snacks)

for key in fav_snacks:
    print(f"{key}'s favorite snack is {fav_snacks[key]}")                     ##print(f)
    print(key+ "'s" + " favorite snack is "+fav_snacks[key]) 

for key,value in fav_snacks.item():
    print(key,value)
if "Bob" in fav_snacks:
    print("Bob's fav snack is " + fav_snacks["Bob"])
else:
    fav_snacks["Bob"] = "chips"

keys=fav_snacks,key() #this is a set
values=fav_snacks.values()  
print(keys)
print(values)

fav_snacks["Alice"] = ["chips", "nuts"]
print(fav_snacks)
