#Python Program to Put Even and Odd elements in a List into Two Different Lists
li = []
n = int(input("how many numbers in the list to be added = "))
for i in range(n):
    number = int(input("enter the number: "))
    li.append(number)
print("entered list is")    
print(li)
li_odd = []
li_even = []
for i in range(len(li)):
    if (li[i]%2 == 0):
        li_even.append(li[i])
    else:
        li_odd.append(li[i])
print("Even list is:= ")
print(li_even)
print("Odd list is:= ")
print(li_odd)
    
