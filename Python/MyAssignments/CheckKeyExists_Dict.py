#Python Program to Concatenate Two Dictionaries Into One
No_Of_Students = {'School1': 1000,
                  'School2': 2000,
                  'School3': 3000,
                  'School4': 4000}
entered_key = str(input("enter the key to check if it is exists: "))
if (entered_key in No_Of_Students):
    print("Key Exists")
else:
    print("Key does not exist")
