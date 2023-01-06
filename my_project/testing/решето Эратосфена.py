# Алгоритм нахождения простых чисел
n= 100
arr = []
for i in range(n):
    arr.append(i)
arr[1] = 0    
#///////////////////////////////////
for i in range(n):
    if arr[i] !=0:
        j = i*2
        while j< n:
            arr[j] = 0
            j+=i

#///////////////////////////////////


for elem in arr:
    if elem != 0:
        print(elem,end=" ")