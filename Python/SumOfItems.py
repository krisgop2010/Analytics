#Python Program to Sum/multiply All the Items in a Dictionary
d1 = {'key1':10,
       'key2':20,
       'key3':3,
       'key4':4}
print("sum of values:=", sum(d1.values()))

multi_result = 1
for i in d1:
    multi_result = multi_result*d1[i]
print("multiplication of values:=", multi_result)
