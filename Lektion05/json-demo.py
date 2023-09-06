import json

attendants = ['Åsa', 'Kalle', 'Olivia', 'Johan']

# Spara listan i en fil i JSON-format
with open('data.json', 'w') as myFile:
    myFile.write(json.dumps(attendants))

# Läs listan från filen
with open('data.json') as f:
    data = json.loads(f.read())

# Indexering funkar :-)
print(data[0])
