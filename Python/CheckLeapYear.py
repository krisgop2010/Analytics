#Check if the entered year is Leap Year
def check_leap_year(year):
    if (year%4 == 0):
        if (year%100 == 0):
            if (year%400 == 0):
                return True
        else:
            return True
    return False;
year = int(input("enter year to be checked whether it is leap year or not:"))
ret_val = check_leap_year(year)
if (ret_val):
    print("Year %d is a leap year" %year)
else:
    print("Year %d is NOT a leap year" %year)
