def printUptoN(n):
    if n>1:
        printUptoN(n-1)
    print(n, end=" ")
n=int(input("Enter your number:"))


printUptoN(n)
