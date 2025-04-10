name= input("Enter your name ")
print("Hello,", name)

try:
    num= int(input("Enter a number "))
    print("you entered", num)
    double = num*2
    print("doubled", double)
except:
    print("number was not entered.")

#how to open up a file in txt
with open("movies.txt") as file:
    for line in file:
        print(line.strip())     #line.strip removes the new line so when you run the code there isn't a space between each movie
with open("heights.txt") as file:
    for line in file:
        info=line.strip().split()
        info [2] = int(info[2])
        print(info)

""" 1. prompt user to enter a filename
    2. Open file and print each line with the line number
"""
filename = input("Enter a filename")
with open(filename) as file:
    count = 1
    for line in file:
        print(str(count)+". " + line.strip())
        count+=1

"""Bank account example
    instance date: account number, balance
    methods: deposit, withdraw
    the class will also include: _init_ and _str_ dunder methods

"""


