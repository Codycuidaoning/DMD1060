#! usr/bin/env python3

#Title

print("Letter Grade Converter")
print()
#Difining variable
choice = "y"
#Data collection
while choice.lower() == "y":
    score = int(input("Enter test score: "))
    if score >= 88:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 67:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    print("Letter grade: ", grade)
    print()
    choice = (input("Continue?(y/n): "))
print ("Okay, Bye!")




