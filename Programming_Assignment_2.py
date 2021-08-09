# Programmer: Nihil Rajendran
# Course: Cs701/GB-731, Dr. Rajeev
# Date: 08/08/21
# Programming Assignment: 2
#
# Asks user to input month and year
month = int(input("Enter month number: "))
year = int(input("Enter year number: "))
# Condition 1. Determines if year is divisible by 100 AND 400
if year % 100 == 0 and year % 400 == 0:
    if month == 2:
        print("Number of Days: ", 29)
    elif month % 2 == 0:
        print("Number of Days: ", 31)
    else:
        print("Number of Days: ", 30)
# Condition 2. Followed if condition 1 is false. Determines if year is not divisible by 100 AND is divisible by 4
elif year % 100 != 0 and year % 4 == 0:
    if month == 2:
        print("Number of Days: ", 29)
    elif month % 2 == 0:
        print("Number of Days: ", 31)
    else:
        print("Number of Days: ", 30)
# Condition 3. If first two conditions are false then it follows below algorithm.
else:
    if month == 2:
        print("Number of Days: ", 28)
    elif month % 2 == 0:
        print("Number of Days: ", 31)
    else:
        print("Number of Days: ", 30)