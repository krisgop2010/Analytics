#Python Program to Map Two Lists into a Dictionary
n = int(input("enter no of items in the list"))
list_keys = []
list_values = []
for i in range(n):
    list_keys.append(str(input("enter key")))
print("list of keys:=", list_keys)
for i in range(n):
    list_values.append(int(input("enter values")))
print("list of values:=", list_values)
print("dictionary created:=", dict(zip(list_keys,list_values)))
