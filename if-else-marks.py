sub1=int(input("Enter your subject 1:")) #40
sub2=int(input("Enter your subject 2:"))#95
sub3=int(input("Enter your subject 3:"))#20

if(sub1<33 or sub2<33 or sub3<33):
    print("you are fail because less than 33% in one subject")
elif(sub1+sub2+sub3)/3<40:
    print("you are fail because total percentage less than 40%")
else:
    print("congratulations! You are passed!")