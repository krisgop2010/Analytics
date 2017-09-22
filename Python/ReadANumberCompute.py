#Python Program to Read a Number n and Compute n+nn+nnn
def calc(n):
    n = float(n)
    x = n + n*n + n*n*n
    x - float(x)
    print("calculated number is : %f" %x)
n = input("enter number: ")
calc(n)
