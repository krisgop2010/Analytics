#Python Program to Find all Numbers in a Range which are Perfect Squares
#and Sum of all Digits in the Number is Less than 10
low_range = int(input("enter lower range:"))
upr_range = int(input("enter upper range:"))
list_of_nos = list(range(low_range,upr_range))
print("input list is : ", list_of_nos)
import math
def is_perfect_square(num):
    return int(math.sqrt(num)) == math.sqrt(num)
def sumOfDigits(num):
    sum = 0
    while(num != 0):
        sum = sum + num%10
        num = num/10
    if (sum < 10):
        return True
li_sq_less_ten = []
li_sq_greater_ten = []
for x in list_of_nos:
    if (is_perfect_square(x)):
        if (sumOfDigits (x)):
            li_sq_less_ten.append(x)
        else:
            li_sq_greater_ten.append(x)
print("list of perfect square nos with sum less than 10 = ",li_sq_less_ten)
print("list of perfect square nos with sum greater than 10 = ",li_sq_greater_ten)
