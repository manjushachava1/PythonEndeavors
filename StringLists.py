# Ask the user for a string and print out whether this string is a palindrome or not.

string = str(input("Enter a string: "))

if string[::-1] == string:
    print(string + " is a palindrome")
else:
    print(string + " is not a palindrome")


