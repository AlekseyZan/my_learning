# объявление функции
def get_month(language, number):
    months_ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    months_en = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    for i in range(number):
        if language=='ru':
            return months_ru[number-1]
        else:
            return months_en[number-1]
        
# считываем данные
lan = input()
num = int(input())

# вызываем функцию
print(get_month(lan, num))
