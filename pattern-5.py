n=int(input("Enter your number"))
count=0
for i in range(1,n+1):
    for k in range(1,n-i+1):
        print(" ",end="")
    for j in range(1,i+1):
        count=count+1
        print(count,end=" ")
    print("")