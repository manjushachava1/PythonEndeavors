#Program 3

#Take a list and print out the numbers less than 5
#Extras:
# 1. Write program in one line of code
# 2. Ask the user for a number and return a list that contains elements that are smaller than that number given by the user.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

#Extra 1
for element in a:
    if element < 5:
        b.append(element)
print(b)

#Extra 2
num = int(input("Enter a random number: "))
for element in a:
    if element < num:
        b.append(element)
print(b)