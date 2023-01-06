import random
n = 5
arr = list()
for i in range(n):
    number = random.randint(0,100)
    arr.append(number)
for i in range(n):
    for j in range(n-1):
        left = arr[j]
        right = arr[j+1]
        if left>right:
            arr[j] = right
            arr[j+1] = left

print("No sorted")
print(arr)

