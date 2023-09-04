# Exempel på try-except i Python
try:
    indata = input("Ange ett heltal:")
    tal = int(indata)
    kvadrat = tal * tal
    print(tal, "i kvadrat är", kvadrat)
except:
    print(indata , "är inte ett heltal")