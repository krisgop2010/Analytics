#Python Program to Replace all Occurrences of ‘a’ with $ in a String
n = int(input("enter no of elements in the list"))
li = []
for i in range(n):
    li.append(str(input("enter word:=")))
print("list is:", li)
mod_li = [w.replace('a', '$') for w in li]
print("modified list is: ", mod_li)
