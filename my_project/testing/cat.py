m=list(map(int, input().split()))
r=int(input())

g=len(m)

for i in range(g):
    if m[i]==r:
        print(i+1)
        break
else:
    print("ErrorValue")
        
