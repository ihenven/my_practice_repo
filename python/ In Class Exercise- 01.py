#LOOPS
#Exercise 1
counter = 0
for i in range(1,21):
    if i%3 == 0:
        print(i)


#Exercise 2
count = 1
sum_even = 0
while count<=50:
    if count%2 ==0:
        sum_even+= count
    count+=1
print(sum_even)

#Exercise 3
numbers = [5,8,2,15,10,3,7]
for num in numbers:
    if num>5:
        print(num, end = " ")

#Exercise w/ Running sum
list = [1,2,3,4,5]
list2 = [1,3,6,10,15]
   #lst = []
  #  lst2.append(lst[0])


#FUNCTIONS ----- #exercise 1 swap elements
def swap(list):
    list = [0,3,8,4,5]
    swap (list)
    print(list)


#String
hello = "hello"
for c in hello:
    print(c)


course= "Platform Computing"
plat = course[0:8] #---- need to give course a place order
comp = course[9:]
print(plat)
print(comp)