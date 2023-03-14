import math

def log2(x):
    return math.log2(x)

def H(list_of_p_values):
    h_of_x = 0
    for p in list_of_p_values:
        h_of_x += (p*log2(1/p))
    return h_of_x

my_list = [0.5, 0.125, 0.25]

print(H(my_list))
