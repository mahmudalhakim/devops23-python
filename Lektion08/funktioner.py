# Funktioner och moduler i Python

from lib import utils
import math

# Anropa en funktion (call / invoke)
print("Summan är :", utils.addera(1, 2))

utils.greet()
utils.greet("Mahmud")
utils.greet("Lisa", "Svensson")

print('Minsta talet är:', utils.minimum([10, 2, 5, 50]))

print(utils.MAX_NUM)

# Anropa en funktion/variabel som finns i standardmodulen math
print(math.pi)
print(math.pow(2, 5))


