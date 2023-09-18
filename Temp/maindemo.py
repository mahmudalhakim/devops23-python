
def main():
    # Här börjar programmet
    print("Välkommen till mitt program!")

    # Gör något arbete
    result = add(3, 5)
    print("Resultatet är:", result)

def add(a, b):
    return a + b

# Kontrollera om programmet körs som ett fristående program, inte som en modul
if __name__ == "__main__":
    main()
