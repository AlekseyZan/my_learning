from math import asin,cos,sqrt,pi,pow
x = float(input())

y = float(input())

# вычислить выражение, результат занести в переменную z        
a = asin(cos(x+(sqrt(3)/2)*pi))
b = 1.2*(sqrt(2-(cos(y)**2)))
c = pow(x,2)+pow(y,2)+1
z = (a+b)/c
print(round(z, 5))