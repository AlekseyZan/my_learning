string = input().lower()
sp = []
count = 0
for i in string:
    if  i in sp:
        count+=1
        i+=1

print(count)
