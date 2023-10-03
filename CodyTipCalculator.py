#! usr/bin/env python3

#Title
print("Tip Calculator")
print()

#Data collecting
cost = float(input("Cost of the meal: "))

print()
print("15%")
print("Tip Amount: ", cost * .15)
print("Total Amount: ", round(cost * .15 + cost, 2))

print()
print("20%")
print("Tip Amount: ", cost * .2)
print("Tip Amount: ", round(cost * .2 + cost, 2))

print()
print("25%")
print("Tip Amount: ", cost * .25)
print("Tip Amount: ", round(cost * .25 + cost, 2))
