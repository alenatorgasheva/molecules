# Project - study
#  Brownian molecular motion

# Developed by A.Torgasheva

from molecules import Molecules


lst_molecules = []
while True:
    print('1 - ADD MOLECULE\n'
          '2 - START\n'
          '3 - EXIT')
    choice = input()
    if choice == '1':
        print('-' * 100)
        x = input('X: ')
        y = input('Y: ')
        radius = input('Radius: ')
        color = input('Color: ')
        speed = input('Speed: ')
        molecule = Molecules(x, y, radius, color, speed)
        lst_molecules.append(molecule)
    if choice == '2':
        if lst_molecules:
            while True:
                Molecules.act()
                print('-' * 100)
                print('1 - CONTINUE\n'
                      '2 - TO MAIN MENU')
                choice = input()
                if choice == '2':
                    break
        else:
            print('NO MOLECULES')

    if choice == '3':
        break
    print('-' * 100)

print('-' * 100)
print('GOODBYE!')

