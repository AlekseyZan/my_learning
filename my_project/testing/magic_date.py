# объявление функции
def is_magic(date):
    day,month,year = map(int,date.split('.'))
    if day*month==year%100:
        return True
    else:
        return False

# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))
