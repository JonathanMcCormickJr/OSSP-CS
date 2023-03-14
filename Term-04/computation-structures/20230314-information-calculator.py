import math

def log2(i):
    return math.log2(i)

def information_p(p):
    # This is for doing the math with a p-value
    return log2(1/p)

def information_nm(n, m):
    # This is for doing the math with n and m values instead
    return log2(n/m)

use_p_value = True

if use_p_value == True:
    p = float(input("p:"))
    print(information_p(p))
elif use_p_value == False:
    n = float(input("n:"))
    m = float(input("m:"))
    print(information_nm(n,m))
else:
    print("Error: unexpected value.")
