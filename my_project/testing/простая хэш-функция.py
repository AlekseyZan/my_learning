def hash(num):
    snum = str(num)
    if len(snum) <= 4:
        if len(snum) < 4:
            snum = snum.rjust(4,"0")
        return snum

    result = ""
    for i in range(0,len(snum)-1,2):
       left = snum[i]
       right = snum[i+1]
       left = int(left)
       right = int(right)
       result += str(left+right)
    return hash(result)
