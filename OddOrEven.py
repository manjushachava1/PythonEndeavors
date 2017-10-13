#Program 2

# Check if user input is even or odd
# Extras:
# 1. Check if user input is a multiple of 4
# 2. Check if two user inputs are divisible by each other

number = int(input("Enter any number: "))
if number % 2 == 0:
    print(str(number) + " is an even number!")
# Extra 1
if number % 4 == 0:
    print(str(number) + " is also multiple of 4!")
else:
    print(str(number) + " is an odd number!")

# Extra 2
num = int(input("Enter a value for num: "))
check = int(input("Enter a value for check: "))

if num % check == 0:
    print(str(num) + " is divisible by " + str(check) + " and equals " + str(int(num / check)))
else:
    print(str(num) + " is NOT divisible by " + str(check))
