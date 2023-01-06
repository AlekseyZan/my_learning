from datetime import datetime
start = datetime.now()

def fact_r(n):
    if n <=1:
        return 1
    return n*fact_r(n-1)


n= 5
fact = fact_r(n)

end = datetime.now()
td = (end-start).total_seconds()*10**3
print(fact)
print(f'{td:.03f},ms')