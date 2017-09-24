#Python Program to Create a List of Tuples with the First
#Element as the Number and Second Element as the Square of the Number
def square(list):
    for i in list:
        return i*i
n1 = int(input("enter no of elements:= "))
list1 = []
for i in range(n1):
    list1.append(float(input("enter number")))
list2 = [(x,x**2) for x in list1]
print("new list is: ", list2)
                 


