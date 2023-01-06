import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
nosymbol = 'il1Lo0O'
chars = ''
quant_pass = int(input("Сколько генераций пароля вы хотите сделать?"))
len_pass = int(input("Укажите длину пароля:"))
digit_pass = input("Включать ли в пароль цифры? (y/n)")
lower_pass = input('Включать ли прописные буквы в пароль?(y/n)')
upper_pass = input('Включать ли заглавные буквы в пароль?(y/n)')
symbol_pass = input("ВКлючать в пароль специальные символы (!#$%&*+-=?@^_)?(y/n)")
nosymbol_pass = input('Исключать из пароля неоднозначные символы(il1Lo0O)?(y/n)')
#Настройка генерируемых паролей
if digit_pass.lower()=='y':
    chars+=digits
    if lower_pass.lower()=='y':
         chars+=lowercase_letters
    else:
        chars+=chars
        if upper_pass.lower()=='y':
             chars+=uppercase_letters
        else:
             chars+=chars
        if symbol_pass.lower()=='y':
                chars+=punctuation
        else:
                chars+=chars
                if nosymbol_pass.lower=='y':
                    for c in range(len(nosymbol)):
                        if nosymbol[c] in chars:
                            chars.remove(nosymbol[c])
                else:
                    chars+=nosymbol
                             
print(chars)
def generate_password(len_pass,chars):
    password = ""
    for i in range(len_pass):
        password.append(random.choice(chars))
        generate_password(len_pass,chars)
        for _ in range(quant_pass):
            generate_password(len_pass, chars)
    print(password)

    
