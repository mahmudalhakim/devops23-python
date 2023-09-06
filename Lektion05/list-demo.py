deltagare = ["Lina", "Gunilla", "Erik", "Carl"]
i = 0
while i < len(deltagare):
    print("Välkommen " + deltagare[i])
    deltagare.remove(deltagare[i])

deltagare = ["Lina", "Gunilla", "Erik", "Carl"]
for namn in deltagare:
  print(f"Välkommen {namn}")