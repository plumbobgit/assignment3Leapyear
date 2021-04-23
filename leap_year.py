"""
Brandon Plumbo
Leap Year Calculator

Run the program and you will be prompted to enter a year, enter this year and press ENTER
the program will output whether or not the input year is a leap year.
"""

year = input("Enter a year: ")  # takes user input of a year as a string and assigns it to the year variable

if (int(year) % 4) == 0:  # checks that the integer input of a year divides evenly by 4
    if (int(year) % 100) == 0:  # checks the divisible evenly by 100 condition
        if (int(year) % 400) == 0:  # checks the divisible evenly by 400 condition
            print('\n', year, " is a leap year!")
        else:
            print('\n', year, " is not a leap year.")
    else:
        print('\n', year, " is a leap year!")
else:
    print('\n', year, " is not a leap year.")
