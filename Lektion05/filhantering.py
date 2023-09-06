# Skapa en fil (w = write)
myFile = open('textfil.txt', 'w')

# Skriv till filen
myFile.write("Rad 1\n")
myFile.write("Rad 2\n")
myFile.write("Rad 3\n")

# Öppna och läs från en fil (r = read)
myFile = open('textfil.txt', 'r')
text = myFile.read()
print(text)

# Stäng filen
myFile.close()

# Öppna en fil med with (a+ = append och läs från filen)
with open('textfil.txt', 'a+') as myFile:
    myFile.write("Rad 4\n")
    myFile.seek(0) # Gå till filens första position
    text = myFile.read()

print(text)
