#Python Program to Find the 2nd Largest Number in a List
li = []
n = int(input("How many numbers to be added in the list = "))
for i in range(n):    
    li.append(float(input("enter number ")))
print(li)
def check_largest_no():
    largest1 = li[0]
    for i in range(len(li)):
        if (li[i] > largest1):
            largest1 = li[i]
    return largest1
largest1 = check_largest_no()
print("largest number in the list is %s" %largest1)
#remove the laregest from the list
li.remove(largest1)
# again call function to find the largest element of the modified list
largest2 = check_largest_no()
print("second largest number in the list is %s" %largest2)
