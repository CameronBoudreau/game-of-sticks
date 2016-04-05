import os
from pickup_pvp import *
#
# def clear():
#     if os.name == 'nt':
#         os.system('cls')
#     else:
#         os.system('clear')
#
#
# def choose_stick_count():
#     stick_count = input("How many sticks are there on the table initially?\n>")
#
#     check = check_initial_stick_count(stick_count)
#     print("Check: ", check)
#     if not check:
#         print("Unacceptable entry - please choose between 10-100 sticks.")
#         return choose_stick_count()
#
#     return int(stick_count)
#
#
# def check_initial_stick_count(stick_count):
#
#     return stick_count.isnumeric() and int(stick_count) in range(10, 101)
#
#
# def get_pickup_amount(stick_count):
#     if stick_count == 1:
#         print("There is 1 stick left. You're so fucked...")
#     else:
#         pickup_amount = input("There are {} sticks left. How many would you like to take (1-3)?\n>".format(stick_count))
#
#     if not acceptable_pickup_amount(pickup_amount):
#         print("Unacceptable entry - please choose between 1-3 sticks")
#         return get_pickup_amount(stick_count)
#
#     return stick_count - int(pickup_amount)
#
#
# def acceptable_pickup_amount(pickup_amount):
#     return pickup_amount.isnumeric() and int(pickup_amount) in range(1, 4)
#
#
# def check_loss(stick_count):
#
#     if stick_count <= 0:
#         return True
#
# def go_again():
#     again = input("\nWould you like to go again? [y/N] \n")
#     if again.lower() == 'y':
#         return True


def main():
    # stick_count = choose_stick_count()
    turn_counter = 1
    pvp = RunGame()

    pvp.run_game()
    # while True:
    #     clear()
    #     if turn_counter % 2 == 1:
    #         print("You're up player one!")
    #     else:
    #         print("You're up player two!")
    #
    #     stick_count = get_pickup_amount(stick_count)
    #
    #     if check_loss(stick_count):
    #         print("FAIL! Get your shit together. Do you even pick up sticks bro?")
    #         break
    #
    #     turn_counter += 1
    #
    # if go_again():
    #     main()
    # clear()

if __name__ == '__main__':
    main()
