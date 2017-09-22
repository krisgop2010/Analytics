#Python Program to Remove the Given Key from a Dictionary
d1 = {'key1':10,
      'key2':20,
      'key3':30,
      'key4':40}
k = input("enter the key to be deleted:=")
d1.pop(k,None)
print("the dict after delettion:",d1)
      
