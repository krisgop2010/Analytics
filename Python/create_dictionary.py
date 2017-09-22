#Python Program to Generate a Dictionary that
#Contains Numbers (between 1 and n) in the Form (x,x*x)
n = int(input("Enter No of elements:= "))
d1 = dict()
for i in range(1,n+1):
    d1[i]=i*i
print("dictionary is: ",d1)
