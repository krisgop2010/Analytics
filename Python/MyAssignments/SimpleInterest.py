#Calculate simple interest
def calc_simple_inretest(P,R,T):
    interest = (P*R*T)/100
    print("Simple interest is = %.2f" %interest)
    
P = float(input("enter Principle: "))
R = float(input("enter rate of interest: "))
T = int(input("enter time in years: "))
calc_simple_inretest(P,R,T)
