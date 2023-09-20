# Övningsuppgift 14.5

teams = {
    'Brazil':
        {'wins': 2, 'draws': 1, 'losses': 0, 'goals_for': 5, 'goals_against': 1},
    'Serbia':
        {'wins': 1, 'draws': 0, 'losses': 2, 'goals_for': 2, 'goals_against': 4},
    'Switzerland':
        {'wins': 1, 'draws': 2, 'losses': 0, 'goals_for': 5, 'goals_against': 4},
    'Costa Rica':
        {'wins': 0, 'draws': 1, 'losses': 2, 'goals_for': 2, 'goals_against': 5}
}


# Konstruera en funktion make_list(dict)
# som omvandlar matchresultat från dictionary
# (likt formatet i variabeln teams)
# till en lista

def make_list(dictinary):
    # Algoritm för att lösa problemet
    # 1. Skapa en tom lista
    new_lista = []

    # 2. Iterera över dictionary
    for country in dictinary:
        # 2.1 Skapa ett nytt dictionary
        country_dict = {
            'country': country,
            'wins': teams[country]['wins'],
            'draws': teams[country]['draws'],
            'losses': teams[country]['losses'],
            'goals_for': teams[country]['goals_for'],
            'goals_against': teams[country]['goals_against']
        }
        # 2.2 lägg den nya dictionary i listan
        new_lista.append(country_dict)

    # 3. returnera listan (spara listan)
    return new_lista


# Anropa funktionen
my_list = make_list(teams)

# Extra övning
# Summera alla wins
summa = 0
for country in my_list:
    summa += country['wins']

print("Summan av alla wins:", summa)


# En funktion som skriver ut en tabell i terminalen
def print_table(lista):
    print('-'*50)
    print('| # |', 'Nation'.ljust(11), '| W | GD |' )
    print('-'*50)
    num = 1
    for i in lista:
        gd = str(i['goals_for']-i['goals_against']).rjust(2)
        c = i['country'].ljust(11)
        w = i['wins']
        num += 1
        print(f"""| {num} | {c} | {w} | {gd} |""")


print_table(my_list)
