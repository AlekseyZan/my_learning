# объявление функции
def number_to_words(num):
    list = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто', '']    
    for i in range(1,100):
        if 1<num<20:
            return list[num-1]
        if 20<num<100:
            list_1 = list[num // 10 + 17]
            list_1 =  ''.join(list[num // 10 + 17] + ' ' + list[num % 10 - 1]).rstrip() 
        return list_1

# считываем данные
n = int(input())

# вызываем функцию
print(number_to_words(n))
    
                   
        
             


