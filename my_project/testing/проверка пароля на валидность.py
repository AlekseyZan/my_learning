# объявление функции
def is_password_good(password):
    count_digit = 0
    count_A = 0
    count_a = 0
    if len(password)<8:
        return False
    for i in password:
        if i in '0123456789':
            count_digit+=1
        if i.isupper():
            count_A+=1
        if i.islower():
            count_a+=1
    if count_digit>=1 and count_A>=1 and count_a>=1:
        return True
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))