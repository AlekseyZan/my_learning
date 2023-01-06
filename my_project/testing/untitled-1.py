def get_together_games(anfisa_games,alisa_games):
    together_games = (anfisa_games,alisa_games)

anfisa_games = [
    'Online-chess',
    'Города',
    'DOOM',
    'Крестики-нолики'
]
alisa_games = [
    'DOOM',
    'Online-chess',
    'Города',
    'GTA',
    'World of tanks'
]
# Вызовите функцию со списками игр в качестве параметров
together_games = (anfisa_games,alisa_games)
games_1 = set(anfisa_games)
games_2 = set(alisa_games)
together_games = games_1.intersection(games_2)
# Напечатайте итоговый перечень игр в цикле
for games in together_games:
    print("👾",*games)

    
 
