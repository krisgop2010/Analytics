#Python Program to Merge Two Lists and Sort it
list1 = []
list2 = []
n1 = int(input("How many numbers to be added in list1 = "))
for i in range(n1):    
    list1.append(float(input("enter number ")))
print("list1 is :", list1)
n2 = int(input("How many numbers to be added in list2 = "))
for i in range(n2):    
    list2.append(float(input("enter number ")))
print("list2 is :", list2)
merged_list = list1 + list2
print("merged list is: ", merged_list)
#sorted_merged_list = merged_list.sort()
print("sorted merged list is: ", sorted(merged_list))



