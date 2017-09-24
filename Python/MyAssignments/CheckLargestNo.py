#Python Program to Find the Largest Number in a List
li = []
n = int(input("How many numbers to be added in the list = "))
for i in range(n):    
    li.append(float(input("enter number ")))
print(li)
def check_largest_no():
    largest = li[0]
    for i in range(len(li)):
        if (li[i] > largest):
            largest = li[i]
    return largest
largest = check_largest_no()
print("largest number in the list is %s" %largest)
    
