number=int(input("enter a number "))
n=int(input("enter bit position"))


if number & (1<<(n-1)):
    print("/nSET")

else:
    print("/nNOT SET")