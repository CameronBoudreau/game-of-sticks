import os
from pickup_pvp import PvPGame
from pickup_ai_cb import AIGame


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def choose_game_type():
    choice = input("Would you like to play against another Player(1) or the AI(2)? \n")
    if choice != '1' and choice != '2':
        print("Enter 1 or 2.")
        return choose_game_type()
    return int(choice)


def main():
    clear()
    pvp = PvPGame()
    pve = AIGame()

    choice = choose_game_type()
    if choice == 1:
        pvp.run_game()
    else:
        pve.run_game()

if __name__ == '__main__':
    main()
