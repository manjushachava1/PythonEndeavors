# Program 4

# Check if user input is even or odd

a = range(2, 11)

number = int(input("Enter a random number: "))

for element in a:
    if number % element == 0:
        print(str(number) + " is divisible by " + str(element))