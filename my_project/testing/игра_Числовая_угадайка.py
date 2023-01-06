from random import*
num = randint(1,50)
total = 0
again = ['y','n','д','н']
welcome = print("Добро пожаловать в цифровую угадайку")
print("Введите число от 1 до 50")
def is_valid(text):
    return text.isdigit() and 0<int(text)<51
while True:
    text = input() 
    total+=1
    if is_valid(text):
        text = int(text)
    else:
        print("А может быть все-таки введем целое число от 1 до 50?")
        continue
    if text<num:
        
        print("Ваше число меньше загаданного,попробуйте еще разок")
    elif text>num:
        
        print("Ваше число больше загаданного,попробуйте еще разок")
    elif text==num:
        
        print("Вы угадали,за",total,"попыток,поздравляем!")
        break
again = input("Хотите сыграть еще раз?(д = да, н = нет)")
while again=="д" or again=='y':
    text = input()
else:
    print("До скорых встреч")
       