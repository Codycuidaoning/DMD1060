#！usr/bin/env python3

#Create Title

print("Change Calculator")
print("")

choice = "y"

while choice.lower() == "y":
#Get input from the user

    cents = int(input("Enter number of cents (0-99): "))
    print("")

#Calculate number of quarters

    quarter = cents // 25
    cents = cents % 25 #remainder with mod
    print("Quarters:", quarter)
        
        

#Calculate number of dimes

    dimes = cents // 10
    cents = cents % 10
    print("Dimes:\t ", dimes)

#Calculate number of nickels

    nickles = cents // 5
    cents = cents %5
    print("Nickles: ", nickles)

#Calculate number of penny

    print("Pennies: ", cents)
    print("")
#asking for continue

    choice = input("Would you like to continue?(y/n): ")
    print("")
print("Okay, Bye")


