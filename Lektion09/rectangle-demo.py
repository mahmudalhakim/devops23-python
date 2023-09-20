# En klass som beskriver en rektangel
from random import randint


class Rectangle:

    def __init__(self, height, width):
        # Privata attribut
        self.__height = height
        self.__width = width

    # Getters & Setters
    def get_height(self):
        return self.__height

    def get_width(self):
        return self.__width

    def set_height(self, height):
        if height > 0:
            self.__height = height
        else:
            print("Felaktig höjd!")

    def set_width(self, width):
        if width > 0:
            self.__width = width
        else:
            print("Felaktig bredd!")

    # Metoder
    def area(self):
        return self.get_height() * self.get_width()

    def omkrets(self):
        return (self.get_height() + self.get_width()) * 2


# Skapa objekt av klassen Rectangle
r1 = Rectangle(1, 2)
print(r1.get_height())
print(r1.get_width())

# Ändra attribut
r1.set_width(-5)
r1.set_height(10)

print("----- r1 -----")
print("Bredd:", r1.get_width())
print("Längd", r1.get_height())

print("Area:", r1.area())
print("Omkrets:", r1.omkrets())

print("----- r2 -----")
r2 = Rectangle(2, 3)
r2.set_width(10)
r2.set_height(10)
print("Area:", r2.area())
print("Omkrets:", r2.omkrets())
print("----------------------")

# Lista av objekt
r_lista = [
    Rectangle(1, 2),
    Rectangle(3, 4),
    Rectangle(5, 6)
]


def get_area_sum(r_lista):
    summa = 0
    for r in r_lista:
        summa += r.area()
    return summa


print("Summa av alla areor:", get_area_sum(r_lista))

print("---   1000 rektanglar   ---")

# Skapa en tom lista
slump_lista = []

# Skapa en iteration som loopar 1000 gånger
for i in range(1000):
    # Skapa en instans av Rectangle
    slump_lista.append(Rectangle(randint(1,10), randint(1,10)))

print(get_area_sum(slump_lista))


