# объявление функции
def is_pangram(text):
    abc = "abcdefghijklmnopqrstuvwxyz"
    text = text.lower()
    count = 0
    for i in range(len(abc)):
        if abc[i] in text:
            count+=1
    if count==26:
        return True
    else:
        return False

# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))
