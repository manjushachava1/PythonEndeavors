# Program 1

# Ask for user's name and age, then calculate the age of the user after 100 years
# Extras:
# 1. Ask user for another number "n" and print the previous message "n" times
# 2. Print the same line "n" times on different lines

name = input("Enter your name here: ")
age = int(input("Enter your age here: "))
age = str(100 - age)
string = "In 100 years " + name + ", you will be " + age + ". "
print(string)

# Extra 1
n = int(input("Enter any number: "))
print(n * string)

# Extra 2
n = int(input("Enter any number: "))
string1 = '\n' + string
print(n * string1)

