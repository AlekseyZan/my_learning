arr = list()
n= len(arr)
max_elem = arr[0]
for i in range(n):
    if arr[i] > max_elem:
        max_elem = arr[i]


#kolichestvo deistvii 2+2+2n+4n == 4+6n (n-длина списка)
#сложность O(n)