ones=0
zeros=0

n=int(input("enter a number "))
while(n):
    if (n&1==1):
        ones+=1

    else:
        zeros+=1

    n>>=1
print("no of ones is {}and no of zeros is {}".format(ones,zeros))



