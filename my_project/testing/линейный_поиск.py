import random

n = 40
arr = list()
for i in range(n):
    number = random.randint(1,100)
    arr.append(number)

to_search = random.randint(1,100)
answer = -1
#///////////////////////////
for i in range(n):
    if arr[i] == to_search:
        answer = i
        break



#//////////////////////////
if answer != -1:
    print(f"Элемент в списке был,его индекс: {answer}")
else:
    print("Элемента в списке не было")