import random
from datetime import datetime
start = datetime.now()


n = 500 # количество элементов списка
arr = list()
for i in range(n):
    number = random.randint(1,100)
    arr.append(number)
print("Not sorted:")
print(arr)
print("---------")

step = len(arr)//2
while step >0:
    for i in range(step,n,1):
        value = arr[i]
        current_index = i
        index_to_chek = current_index - step
        while current_index >0 and arr[index_to_chek]> value:
            arr[current_index] = arr[index_to_chek]
            current_index-=step
            index_to_chek -=step
        arr[current_index] = value
    step = step//2

end = datetime.now()
td = (end-start).total_seconds()*10**3


print("Sorted:")
print(arr)
print(f'{td:.03f},ms')