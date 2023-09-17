"""
Övningsuppgift 12.6
Live demo: https://dva128demo.mdh.repl.co/#week5/alwaysnote
"""
import json
import os

# Läs in listan från notes.json
'''
notes = {
    "Important": "Lite test och annat",
    "Notes from lecture": "Testar ... "
}
'''

'''
För att öppna en fil för både läsning och skrivning, 
och skapa filen om den inte finns med bibehållet befintligt innehåll, 
kan du använda läget "a+" (append och läs). 
'''
with open('notes.json', 'a+') as f:
    try:
        # Läs innehållet i filen (om det finns)
        f.seek(0)

        notes = json.loads(f.read())
    except:
        notes = {}

while True:

    # Rensa terminalfönstret
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    # Skapa UI
    print('.:  ALWAYSNOTE  :.')
    print('-- gold edition --')
    print('******************')

    # Visa title från notes
    for key in notes:
        print('-', key)

    print('------------------')
    print('view | view note')
    print('add  | add note')
    print('rm   | remove note')
    print('exit | exit program')

    option = input('menu > ')

    #  View
    if option == 'view':
        title = input('title > ')
        try:
            print(notes[title])
        except KeyError as e:
            print("ERROR: Unknown note:", e)

    # Add
    elif option == 'add':
        title = input('title > ')
        desc = input('desc > ')
        notes[title] = desc
        print('------------------')
        print('INFO: Note added')

    # Remove
    elif option == 'rm':
        title = input('title > ')
        # del notes[title]
        try:
            notes.pop(title)
            print('INFO: Note deleted')
        except KeyError as e:
            print("ERROR: Unknown note:", e)

    # Exit
    elif option == 'exit':
        print('Saving to notes.json ...')

        # Implementera lagring i ett icke-flyktigt minne
        with open('notes.json', 'w') as f:
            f.write(json.dumps(notes))

        print('Programmet stängdes!')
        break

    else:
        print('Ogiltigt kommando...')

    print('------------------')
    input('Press enter to continue...')
