import os
from time import sleep
import sys
import random


class AIGame():
    def __init__(self):
        self.ai_dict = {}
        self.ai_dict = self.create_ai_dict()

    def print_text(self, a_string, a_is_slow):
        if a_is_slow:
            for words in a_string + "\n":
                sys.stdout.write(words)
                sys.stdout.flush()
                sleep(.15)
        else:
            print(a_string)

    def clear(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def choose_stick_count(self):
        self.stick_count = input("How many sticks are there on the table initially?\n>")

        if not self.check_initial_stick_count(self.stick_count):
            print("Unacceptable entry - please choose between 10-100 sticks.")
            return self.choose_stick_count()

        return int(self.stick_count)

    def check_initial_stick_count(self, stick_count):
        return self.stick_count.isnumeric() and int(self.stick_count) in range(10, 101)

    def get_new_stick_count(self, stick_count):
        self.pickup_amount = self.get_pickup_amount(self.stick_count)

        if not self.acceptable_pickup_amount(self.pickup_amount):
            print("Unacceptable entry - please choose between 1-3 sticks")
            return self.get_pickup_amount(stick_count)

        return self.stick_count - int(self.pickup_amount)

    def get_pickup_amount(self, stick_count):
        if self.stick_count == 1:
            self.pickup_amount = input("There is 1 stick left. You're stuck...Go ahead and pick it up, loser.\n")
        else:
            self.pickup_amount = input("There are {} sticks left. How many would you like to take (1-3)?\n>".format(self.stick_count))

        return self.pickup_amount

    def acceptable_pickup_amount(self, pickup_amount):
        return self.pickup_amount.isnumeric() and int(self.pickup_amount) in range(1, 4)

    def check_loss(self, stick_count):
        if int(self.stick_count) <= 0:
            return True

    def turn_is_odd(self, turn_counter):
        return self.turn_counter % 2 == 1

    def print_loss(self, turn_counter):
        if self.turn_is_odd(self.turn_counter):
            print("FAIL! Get it together. Do you even pick up sticks bro?")
        else:
            print("You did it! You're smarter than a machine. Can't let them get cocky, can we?")

    def go_again(self):
        self.again = input("\nWould you like to go again? The AI will learn the more games you play with it. [y/N] \n")
        if self.again.lower() == 'y':
            return True

    def update_ai_dict(self, stick_count, turn_counter, ai_dict, ai_round_picks):
        if self.turn_is_odd(self.turn_counter):
            self.add_to_dict(self.ai_dict, self.ai_round_picks)
        else:
            self.remove_from_dict(self.ai_dict, self.ai_round_picks)

    def add_to_dict(self, ai_dict, ai_round_picks):
        for key in list(self.ai_round_picks.keys()):
            self.ai_dict[key].append(self.ai_round_picks[key])
        return self.ai_dict

    def remove_from_dict(self, ai_dict, ai_round_picks):
        for i in list(self.ai_round_picks.keys()):
            if len(self.ai_dict[i]) > 3 and self.ai_dict[i].count(3) > 1:
                self.ai_dict[i].remove(self.ai_round_picks[i])

    def create_ai_dict(self):
        for i in range(1, 100):
            self.ai_dict[i] = [1, 2, 3]
        return self.ai_dict

    def ai_gets_amount_to_pickup(self, ai_dict, turn_counter):
        if self.stick_count > 1:
            self.pickup = random.choice(self.ai_dict[self.turn_counter])
            return self.pickup
        else:
            return 1

    def run_game(self):
        self.clear()
        self.stick_count = self.choose_stick_count()
        self.turn_counter = 1

        self.ai_round_picks = {}

        while True:
            self.clear()
            print("\nStart of turn {}.\n".format(self.turn_counter))
            if self.turn_is_odd(self.turn_counter):
                print("You're up player one!")
                self.stick_count = self.get_new_stick_count(self.stick_count)
            else:

                print("Please wait while the computer figures out how best to destroy you.")
                self.print_text(".\n.\n.\n.\n.\n.\n.", True)

                self.pickup = self.ai_gets_amount_to_pickup(self.ai_dict, self.turn_counter)

                self.ai_round_picks[self.stick_count] = self.pickup

                self.stick_count = self.stick_count - self.pickup

            if self.check_loss(self.stick_count):
                self.print_loss(self.turn_counter)
                self.update_ai_dict(self.stick_count, self.turn_counter, self.ai_dict, self.ai_round_picks)
                break

            self.turn_counter += 1

        if self.go_again():
            self.run_game()
        self.clear()
