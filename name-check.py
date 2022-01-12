#check wheather given string is anagram or not  --->  //codevita
#cat --> act , tac , cta , tac
name = input("Enter a first string : ") 
ana = input("Enter a second string : ")
res1 = ''.join(sorted(name))
print(res1)
res2 = ''.join(sorted(ana))
print(res2)
if res1 == res2 :
    print("Anagram")
else:
    print("Not Anagram")