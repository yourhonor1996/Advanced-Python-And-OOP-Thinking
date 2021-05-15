from math import gcd, ceil, tan, radians, floor, atan, sin, pi
def my_func(x):
    return gcd( ceil(pow(x, 5/3) + tan(radians(x))) , floor(pow(pi, 2 + atan(sin(radians(x))**2))))
    
print(my_func(int(input())))