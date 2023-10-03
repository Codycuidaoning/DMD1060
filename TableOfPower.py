#! usr/bin/env python3

#Displat title

print("Table of Power")
print("")

#Getting inputs from user

while True:

    start = int(input("Start number: "))
    stop = int(input("Stop number: "))

    if start > stop:
        print("Start number must be less than stop number, try again")
        continue
    else:
        break

#print

print("Number\tSquared\tCubed")
print("======\t=======\t=====")
for number in range(start, stop + 1):
    print(number,"\t",number**2,"\t",number**3)

##print("Number\tSquared\tCubed")
##print("======\t=======\t=====")
##print(start,"\t", start**2,"\t", start**3)
