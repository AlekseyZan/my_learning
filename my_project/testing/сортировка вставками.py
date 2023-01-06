import random
n = 5 # количество элементов списка
arr = list()
for i in range(n):
    number = random.randint(1,100)
    arr.append(number)
print("Not sorted:")
print(arr)
print("---------")

for i in range(n):
    val = arr[i]
    j = i-1
    if j<0:
        continue
    while val < arr[j] and j>=0:
        arr[j+1] = arr[j]
        j -=1
    arr[j+1] = val
print("sorted:")
print(arr)
