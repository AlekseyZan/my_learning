from datetime import datetime
start = datetime.now()

def fibonacci(n):
    if n<=2:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

end = datetime.now()
td = end - start
n = 25
print(fibonacci(n))
print(td)
