from typing import Text


a=input("Enter your character:")
b=a.count("")
if(b<10):
    print("your character is less than 10")
else:
    print("your character is greater than 10")