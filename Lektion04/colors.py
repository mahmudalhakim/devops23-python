import os

ui_width = 50

while True:
    print(ui_width * '*')
    print('FÄRG-GISSAREN 2.0'.center(ui_width))
    print(ui_width * '-')
    print(':: REGLER ::'.center(ui_width))
    print('Gissa en färg!'.center(ui_width))
    print('Gissar du rätt färg'.center(ui_width))
    print('vinner du spelet!'.center(ui_width))
    print('-' * ui_width)

    # Antal försök
    times = 1

    color = input('Gissa färg > ').lower()

    while color != 'gul':
        print('Fel gissning , försök igen... ')
        times += 1
        color = input('Gissa färg > ').lower()

    print('-' * 23)
    print('Korrekt gissat efter', times, 'försök!')

    input('Tryck på Retur för att starta igen')

    # Rensa terminalfönstret
    if os.name == 'nt':
        os.system('cls')
        # print('Du kör Windows')
    elif os.name == 'posix':
        os.system('clear')
        # print('Du kör Mac eller Linux')
