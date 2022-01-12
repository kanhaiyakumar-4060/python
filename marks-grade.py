marks=int(input("Enter your marks\n"))

if marks>=90:
    Grade="Ex"
elif marks>=80:
    Grade="A"
elif marks>=70:
    Grade="B"
elif marks>=60:
    Grade="C"
elif marks>=50:
    Grade="D"
else:
    Grade="F"

print("Your Grade is "+ Grade)
