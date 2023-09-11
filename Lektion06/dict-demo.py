# Dictionary Demo

# Skapa en ny dictionary
person = {
    "name": "Mahmud Al Hakim",
    "age": 50
}

# Skriv ut objektet
print(person)

# Hämta ett element
print("Hej " + person['name'])
print("Du är " + str(person['age']) + " år gammal.")
print(F"Du är {person['age']} år gammal.")

# Referera till en nyckel dynamiskt
'''
attr = input("Ange attribut (nyckel) > ")

try:
    print(person[attr])
except KeyError as fel:
    print("Fel! Attributet existerar inte!")
    print("Du skrev: " + str(fel))
'''

# Ändra värdet
person['age'] = 51
print(person)

# Lägg till ny data (key-value-pair) / element
person["address"] = "Hemfridsvägen 17"
print(person)

# Ta bort element
del person['age']
print(person)

# Kopiera dict
temp = person  # FEL FEL FEL
person["temp"] = "temp"
print(temp)
print(person)
# temp och person pekar på samma objekt

person_copy = person.copy()
person_copy['temp2'] = "temp2"
print(person_copy)

del person_copy
# print(person_copy) # Visar ibland ett felmeddelande (WIRED)

# Iteration av dict
for key in person:
    print("Key:", key)
    print("Value:", person[key])

# Nästlande dict
person["address"] = {
    "gatuadress": "Hemfridsvägen 17",
    "ort": "Sollentuna",
    "postnummer": "192 67"
}

# Skriv ut adressen enligt svensk standard
print(person['address']['gatuadress'])
print(person['address']['postnummer'], (person['address']['ort']).upper())
