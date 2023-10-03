#!/usr/bin/env python3

# Title: HikeCalculator
# Name: Daoning Cui
# Date: 09/26/2023
# Description: This is Hike Calculator.

# Import modules

# Define functions


# Define main function
def print_title():
    print ("Hike Calculator: ")
    print("")
    pass

# Converts miles to feet
def convert_to_feet(miles):
    feet = miles * 5280 
    return feet
    pass
    
    


def main():
    print_title()
    miles = float(input("Enter # of miles walked: "))
    feet = int(convert_to_feet(miles))
    print("The # of feet walked: ", feet)
    
      

    
    pass

if __name__ == "__main__":
    main()




