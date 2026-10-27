n = int(input("Enter The number :  "))
if (n >0 and (n&(n-1)) == 0):
    print(True)
else:
    print(False)