# function to check if a year is a leap year
def leap_year(y):
    if y % 4 == 0:
        if y % 100 == 0 and y % 400 != 0:
            return 0
        else:
            return 1
    else:
        return 0

# function to get the number of days in a given month
def number_of_days(m, y):
    if m in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif m in [4, 6, 9, 11]:
        return 30
    elif m == 2:
        if leap_year(y) == 1:
            return 29
        else:
            return 28

# function to get the number of days passed in a given year
def days_passed(d, m, y):
    days = 0
    for i in range(1, m):
        days += number_of_days(i, y)
    days += d - 1
    return days

# get user input
day = int(input('Enter the day: '))
month = int(input('Enter the month: '))
year = int(input('Enter the year: '))

# display menu
print('Menu:')
print('1) Calculate the number of days in the given month.')
print('2) Calculate the number of days passed in the given year.')

# get user choice
choice = int(input('>'))

# display result
if choice == 1:
    print('Number of days in the given month is', number_of_days(month, year))
elif choice == 2:
    print('Number of days passed in the given year is', days_passed(day, month, year))