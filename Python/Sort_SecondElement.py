#Python Program to Sort the List According to the Second Element in Sublist
sampleList = [['Sourav',100],['Sachin',80],['Dravid',70],['Sehwag',10]]
print("Original List is : ", sampleList)
sorted_list = sorted(sampleList, key=lambda x: x[1])
print("Sorted List is : ", sorted_list)
