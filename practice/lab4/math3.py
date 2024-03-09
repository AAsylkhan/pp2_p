import math
n=4
a=25
#The area of the polygon is: 625
cot = 1 / math.tan(math.pi/n)
A = n * a**2 *1/4*cot

print(A)