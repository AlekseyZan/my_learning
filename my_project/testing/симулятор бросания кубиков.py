from random import*
again = 'д'
while again.lower()=='д':
    print("Бросаем кубики...")
    print("Значения граней:")
    print(randint(1,6))
    print(randint(1,6))
    again = input('Бросить кубики еще раз?(д = да,н = нет)')
    
