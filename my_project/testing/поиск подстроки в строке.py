str_where = "hello world" #исходная строка
str_find_value = " wor"         # подстрока, которую ищем
index_where = 0
index_find_value = 0
len_where = len(str_where)
len_find_value = len(str_find_value)

while (index_where <= len_where - len_find_value and 
        index_find_value < len_find_value):
        if str_where[index_where + index_find_value] == str_find_value[index_find_value]:
            index_find_value +=1
        else:
            index_where +=1
            index_find_value = 0

print(f"'{str_where}'")
print(f"'{str_find_value}'")

        
if index_find_value == len_find_value:
    print(f"Такая подстрока есть, ее начало здесь: {index_where}")
else:
    print("Такой подстроки в исходной строке нет")


        

