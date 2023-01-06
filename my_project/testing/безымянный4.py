direct = int(input('Выберите направление: шифрование - 1, дешифрование - 2 '))
move = int(input('Ввелите величину сдвига '))
ans = ''

eng_alph = 'abcdefghijklmnopqrstuvwxyz'
rus_alph = "абвгдежзийклмнопрстуфхцчшщъыьэюя"

def lang():
    lang = int(input('Выберите язык: русский - 1, английский - 2 '))
    if lang == 2:
        return eng_alph
    elif lang == 1:
        return rus_alph
    else:
        print('Введите цифру языка корректно')
        lang()


def code():
    alp = lang()
    text = input('Введите ваш текст: ')
    ans = ''
    if direct == 1:
        for i in range(len(text)):
            if text[i].isalpha():
                if text[i] == text[i].isupper():
                    ans += alp[(alp.find_value(text[i].lower())+move) % len(alp)].upper()
                else:
                    ans += alp[(alp.find_value(text[i])+move) % len(alp)]
            else:
                ans += text[i]
        print(ans)
    elif direct == 2:
        for i in range(len(text)):
            if text[i].isalpha():
                if text[i] == text[i].isupper():
                    ans += alp[(alp.find_value(text[i].lower())-move) % len(alp)].upper()
                else:
                    ans += alp[(alp.find_value(text[i])-move) % len(alp)]
            else:
                ans += text[i]
        print(ans)
    else:
        print('Введите направление корректно: ')
        code()

    
code()
