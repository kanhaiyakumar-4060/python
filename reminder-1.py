n=int(input("Enter a num:"))
rev=0
while n!=0:
    rev=n%10
    rev=rev*n//10
print(rev)