n=int(input("Enter your number"))
count=1
for i in range(1,n+1):
    for k in range(1,n-i+1):
        print(" ",end="")
    for j in range(1,i+1):
        print(i+j-1,end="")

    x=2*i-2
    for k in range(1,i):
        print(x,end="")
        x=x-1
    print("")