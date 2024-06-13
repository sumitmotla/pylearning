# getting year input from the user
year = int(input("Enter the year : "))
# checking if the year is divisible by 4
if year % 4 == 0:
    # checking if the year is divisible by 100
    if year % 100 == 0:
        # checking if the year is divisible by 400
        if year % 400 == 0:
            print(year, "is a leap year.")
        #
        else:
            print(year, "is not a leap year.")
    else:
        print(year, "is a leap year.")
# if the year is not divisible by 4 then it is not a leap year
else:
    print(year, "is not a leap year.")
