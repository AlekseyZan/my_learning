import random
from time import time
n = 40000
start = time()
arr = list()
for i in range(n):
    number = random.randint(1,100)
    arr.append(number)

to_search = random.randint(1,100)
answer = -1
end = time()
time1 = (end - start)
#///////////////////////////
start1 = time()

arr.sort() #список должен быть обязательно отсортирован
first = 0
last = n-1
while first <=last and answer == -1:
    middle_index = (first + last) // 2
    if arr[middle_index] == to_search: #середина между левой и правой границей списка
        answer = middle_index
    else:
        if arr[middle_index]> to_search:
            last = middle_index - 1
        else:
            first = middle_index +1

end1 = time()
time2 = (end1 - start1)


#//////////////////////////

print(arr)
print("------------")
print(to_search)
print("-----------")
print(f"Время выполнения алгоритма: {time1}")
print(time2)

if answer != -1:
    print(f"Элемент в списке был,его индекс: {answer}")
else:
    print("Элемента в списке не было")