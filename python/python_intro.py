print("Hello World")

# this is a comment for a single line

''' if you want to write a large block of comments
'''
# line 1 command fn "/"
# line 2
# line 3


#variables
x= 10
y=10
result = int(x/y)
result = int(result)
print(result)

#"//" is divides

x=105
result=x//y
print(result)


min_val=min(1,10,50)
print(min_val)
raised = pow(2,3)
print(raised)
raised = 2**3
print(raised)


#if then statements
if x<0:
    print("x is negative")
   # x=10
elif x>0:
    print("x is postive")
else:
    print("x is 0")

start = 10
end = 100

#compound condictionals
if x>=start and x<=end:
    print("x is witin range")

if x<start or x>end:
    print('x not within range')



#while loops
counter = 0
while counter<5:
    print(counter)
    counter+=1 # instead of saying counter++ in java

#for loop
     # for(int i=0; i< 5; i++){ ---- java

for i in range(1,5,): # how to increase parameters. so how you go from "i" "j" "k" ---> up to but not including 5
    print(i, end = " ")
print()

#1st = list
list = [2,4,6,8]
for i in range(len(list)):
    print(list[i], end= " ")
print()

for val in list: # how to get access to elements in a range
    print(val)

for index, value in enumerate(list):
    print(index, value, end= " ")
print()

#Functions

def hello_world():
    print("Hello World!")
hello_world()

def hello(name):
    print("hello" + name)
    print("Hello", name)
hello("Bob")

def hello2(name = "Bob"):
    print("Hello " +name)
hello2()



#STRINGS

#len = length:

print('Python' * 7) #repetition operator 


