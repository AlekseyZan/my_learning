friends = {
    'Серёга': 'Омск', 
    'Соня': 'Москва', 
    'Дима': 'Челябинск', 
    'Алина': 'Хабаровск', 
    'Егор': 'Пермь'
}

def is_anyone_in(collection, city):
    for friend in friends:
        if collection[friend] == city:
            print(f"В городе {collection[friend]} живет {friend}. Обязательно зайду в гости")
        else:
            print(f"В городе {collection[friend]} у меня есть друг,но мне туда не надо")
    
is_anyone_in(friends, 'Хабаровск')