#Python Program to Find the Union/Intersection of two Lists
list1 = []
list2 = []
list3 = []
n1 = int(input("enter no of elements for list1= "))
for i in range(n1):
    list1.append(input("enter number: "))
print("List1 is :", list1)
n2 = int(input("enter no of elements for list2= "))
for i in range(n2):
    list2.append(input("enter number: "))
print("List2 is :", list2)
list3 = set(list1) | set(list2)
print("Union of list1 and list3 is: ", list3)
list3 = set(list1) & set(list2)
print("Intersection of list1 and list3 is: ", list3)
