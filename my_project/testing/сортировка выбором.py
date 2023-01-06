import random
n = 5 # количество элементов списка
arr = list()
for i in range(n):
    number = random.randint(1,100)
    arr.append(number)
print("Not sorted:")
print(arr)
print("---------")

for i in range(n-1):
   min_max_index = i
   for j in range(i+1,n, +1):
        if arr[j] < arr[min_max_index]:
            min_max_index = j
        temp = arr[i]
        arr[i] = arr[min_max_index]
        arr[min_max_index] = temp    
    





print("sorted:")
print(arr)