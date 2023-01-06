n = int(input())
k = int(input())
count = 0
for i in range(1,n+1):
    count = (count+k)%i
print(count+1)