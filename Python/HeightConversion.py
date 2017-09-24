#Python Program to Read Height in Centimeters and then Convert the Height to Feet and Inches
cent = float(input("enter length in centimeters :="))
feet = int(cent/2.54)
inches = float(cent%2.54)
print("it is %d feet %.2f inches tall" %(feet,inches))
