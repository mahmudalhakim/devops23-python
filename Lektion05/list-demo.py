deltagare = ["Lina", "Gunilla", "Erik", "Carl"]
i = 0
while i < len(deltagare):
    print("Välkommen " + deltagare[i])
    deltagare.remove(deltagare[i])

deltagare = ["Lina", "Gunilla", "Erik", "Carl"]
for namn in deltagare:
    print(f"Välkommen {namn}")

# Övning
# Skriv ut alla tal från 0 till 9 utan att använda while
myList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in myList:
    print(i)

for i in range(10):
    print(i)

till_9 = list(range(10))
for tal in till_9:
    print(tal)
