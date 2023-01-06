# объявление функции
def compute_binom(n,k):
    from math import factorial
    if k>n:
        return 0
    else:  
        binom = factorial(n)/(factorial(k)*factorial(n-k))
        binom = int(binom)
    return binom
# считываем данные
n = int(input())
k = int(input())

# вызываем функцию
print(compute_binom(n, k))