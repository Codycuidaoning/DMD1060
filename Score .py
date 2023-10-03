#! usr/bin/env python3

#Title

print("Enter Three Test Scores ")
print()
print("=======================")

#Input collect

score1 = int(input("Enter Test Score:  "))
score2 = int(input("Enter Test Score:  "))
score3 = int(input("Enter Test Score:  "))

total_score = score1 + score2 +score3

average_score = round(total_score/3)

#Display

print("=======================")
print()
print("Your scores: ", score1, score2, score3,
    "\nThe Total Score: ", total_score, 
    "\nThe Average Score: ", average_score)
print()
print("Bye!")
