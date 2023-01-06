fib1 = fib2 = 1
n = 15
for i in range(2,n):
    summa = fib2 + fib1
    fib1 = fib2
    fib2 = summa
    print(summa,end=" ")
