"""
myBill = input("What was the bill?: ")
numberOfPeople = input("How many people?: ")
answer = float(myBill) / float(numberOfPeople)
print("You all owe: ", round(answer))
"""

print("-----------------------------")

myScore = input("Your score: ")
if int(myScore) > 99:
  print("Winner!")
else:
  print("Try again 😭")