#Use of Lambda and Map function to square a list
input_list = []
n = int(input("How many numbers would you like to add in the list = "))
for i in range(n):    
    input_list.append(float(input("enter number ")))
print("Entered List is: ",input_list)
squared_list = list(map((lambda x:x**2), input_list))
print("Squared List is: f", squared_list)
