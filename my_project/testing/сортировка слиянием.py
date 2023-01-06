import random
n = 5 # количество элементов списка
arr = list()
for i in range(n):
    number = random.randint(1,100)
    arr.append(number)
print("Not sorted:")
print(arr)
print("---------")

def merge(arrl,arrr):
    sorted_arr = []
    current_left = 0
    current_right = 0
    lenl = len(arrl)
    lenr = len(arrr)
    for i in range(lenl+lenr):
        if current_left < lenl and current_right < lenr:
            if arrl[current_left]> arrr[current_right]:
                sorted_arr.append(arrl[current_left])
                current_left+=1
            else:
                sorted_arr.append(arrr[current_right])
                current_right+=1
        else:
            if current_left==lenl:
                for j in range(current_right,lenr):
                    sorted_arr.append(arrr[j])
            else:
                for j in range(current_left,lenl):
                    sorted_arr.append(arrl[j])
            break 
    return sorted_arr    


def merge_sort(arr):
    if len(arr)<= 1:
        return arr
    mid = len(arr)//2
    left_side = list()
    right_side = list()
    for i in range(0,mid):
        val = arr[i]
        left_side.append(val)
    for i in range(mid,len(arr)):
        val = arr[i]
        right_side.append(val)

    left_side = merge_sort(left_side)
    right_side = merge_sort(right_side)
    result = merge(left_side,right_side)
    return result

arr = merge_sort(arr)
print("Sorted:")
print(arr)
