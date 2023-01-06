text = input().split()
k = 26
for i in text:
    for j in range(len(text)):
        if text[j].isalpha():
            index = ord(i)-k
            if index<97:
                index = 122-(96-index)
                print(chr(index),sep='')
