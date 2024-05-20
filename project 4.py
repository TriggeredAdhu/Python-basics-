# Project 4:
# Get a user defined integer list as input and append the even and odd numbers in the separate lists.

l1 = list(map(int, input("enter the list of numbers").split(",")))
print(l1)
listOdd = []
listEven = []
for num in l1:
    if num % 2 == 0:
        listEven.append(num)
    else:
        listOdd.append(num)

print("the odd numbers from the list are:", listOdd)
print("the even numbers from the list are:", listEven)
