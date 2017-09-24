#Python Program to Swap the First and Last Value of a List
li = []
n = int(input("How many numbers to be added in list = "))
for i in range(n):    
    li.append(input("enter number "))
print("original list is :", li)
temp1 = li[0]
li[0] = li[n-1]
li[n-1] = temp1
print("modified list is :", li)
