fotboll = [
    {
        'country': 'Russia',
        'points': 3
    },
    {
        'country': 'Brazil',
        'points': 7},
    {
        'country': 'Cameroon',
        'points': 1},
    {
        'country': 'Sweden',
        'points': 5
    }
]


def get_points(element):
    return element['points']


# Skapa en ny lista
fotboll = sorted(fotboll, key=get_points, reverse=True)
print(fotboll)

# Arbeta med samma lista
fotboll.sort(key=get_points, reverse=True)

print(fotboll)
