x = int(input("Enter the number = "))
x= str(x)
palindrome = x[::-1]
if x == palindrome:
    print(True)
else:
    print(False)