import random
n = 5 # количество элементов списка
arr = list()
for i in range(n):
    number = random.randint(1,100)
    arr.append(number)
print("Not sorted:")
print(arr)
print("---------")

def quick_sort(arr):
    if len(arr) <=1:
        return arr

    index_of_strong_elem = random.randint(0,len(arr))
    strong_elem = arr[index_of_strong_elem]
    low = []
    mid = []
    high = []
    for elem in arr:
        if elem == strong_elem:
            mid.append(elem)
        elif elem < strong_elem:
            low.append(elem)
        else:
            high.append(elem)
    
    low = quick_sort(low)
    high = quick_sort(high)
    result = low + mid + high
    return result

arr = quick_sort(arr)

print("sorted:")
print(arr)
