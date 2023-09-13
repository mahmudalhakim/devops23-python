"""
Övningsuppgift 12.6
Live demo: https://dva128demo.mdh.repl.co/#week5/alwaysnote
"""

import json
import os

# Läs listan från filen
with open('notes.json') as f:
    notes = json.loads(f.read())

while True:

    # Rensa terminalfönstret
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')

    # Rita UI
    print(".:  ALWAYSNOTE  :.")
    print("-- gold edition --")
    print("******************")
    for key in notes:
        print(key)
    print("------------------")
    print("view | view note")
    print("add  | add note")
    print("rm   | remove note")
    print("exit | exit program")
    print("------------------")

    # Visa prompt
    choice = input("menu > ")

    if choice == "view":
        key = input("title > ")
        try:
            print(notes[key])
        except KeyError:
            print("ERROR: Unknown note")

    elif choice == "add":
        key = input("titel > ")
        value = input("descr > ")
        notes[key] = value
        print("INFO: Note added")

    elif choice == "rm":
        key = input("title > ")
        try:
            del notes[key]
            print("INFO: Note deleted")
        except KeyError:
            print("ERROR: Unknown note")

    elif choice == "exit":
        # Spara listan i en fil i JSON-format
        print("Saving ...")
        with open('notes.json', 'w') as f:
            f.write(json.dumps(notes, ensure_ascii=False))

        exit()

    else:
        print("ERROR: Unknown command", choice)

    print("------------------")
    input("Press enter to continue...")