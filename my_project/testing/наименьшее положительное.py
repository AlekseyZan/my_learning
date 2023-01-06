m= list(map(int,input().split()))
sp = []
for i in range(len(m)):
    if m[i]<=0:
        continue
    else:
        sp.append(m[i])
if len(sp)==0:
    print("Empty")
if len(sp)>0:
    print(min(sp))
        

        
