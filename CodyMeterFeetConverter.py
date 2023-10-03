#!/usr/bin/env python3

# Title: Meter to Feet or Reverse Calculator
# Name: Daoning Cui
# Date: 09/27/2023
# Description: This is a meter to feet calculator

# Import modules

# Define functions
# Display a welcoming message/title:
def print_title():
    print("Feet and Meter Converter")
    print("")
    print("")
    print("Conversion Menu: ")

def print_two_choices():
    print("a. Feet to Meters")
    print("b. Meter to Feet")
# Converting functions

def convert_to_meter(feet):
    meter = feet * 0.3048
    return meter
def convert_to_feet(meter):
    feet = meter / 0.3048
    return feet
    
# Define main function 
def main():
    print_title()
    print_two_choices()

    choice2 = "y"
    while choice2.lower() == "y":
        choice = input("Select a conversion (a/b): ")
        if choice.lower() == "a":
            feet = float(input("Enter feet: "))
            meter = round(convert_to_meter(feet), 2)
            print(meter, "maters")
                                
        else :
            meter = float(input("Enter meter: "))
            feet = int(convert_to_feet(meter))
            print(feet, "feet")
        choice2 = input("Would you like to continue?(y/n): ")
    print("Okay, bye.")
    
           
if __name__ == "__main__":
    main()




