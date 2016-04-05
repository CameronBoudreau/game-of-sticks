import os

class RunGame():

    # def __init__(self, stick_count):
    #     self.stick_count = stick_count

    def clear(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')


    def choose_stick_count(self):
        self.stick_count = input("How many sticks are there on the table initially?\n>")

        self.check = self.check_initial_stick_count(self.stick_count)
        print("Check: ", self.check)
        if not self.check:
            print("Unacceptable entry - please choose between 10-100 sticks.")
            return self.choose_stick_count()

        return int(self.stick_count)


    def check_initial_stick_count(self, stick_count):

        return self.stick_count.isnumeric() and int(self.stick_count) in range(10, 101)


    def get_pickup_amount(self, stick_count):
        if self.stick_count == 1:
            print("There is 1 stick left. You're so fucked...")
        self.pickup_amount = input("There are {} sticks left. How many would you like to take (1-3)?\n>".format(self.stick_count))

        if not self.acceptable_pickup_amount(self.pickup_amount):
            print("Unacceptable entry - please choose between 1-3 sticks")
            return self.get_pickup_amount(stick_count)

        return self.stick_count - int(self.pickup_amount)


    def acceptable_pickup_amount(self, pickup_amount):
        return self.pickup_amount.isnumeric() and int(self.pickup_amount) in range(1, 4)


    def check_loss(self, stick_count):

        if self.stick_count <= 0:
            return True

    def go_again(self):
        self.again = input("\nWould you like to go again? [y/N] \n")
        if self.again.lower() == 'y':
            return True

    def run_game(self):
        self.clear()
        self.stick_count = self.choose_stick_count()
        self.turn_counter = 1

        while True:
            self.clear()
            if self.turn_counter % 2 == 1:
                print("You're up player one!")
            else:
                print("You're up player two!")

            self.stick_count = self.get_pickup_amount(self.stick_count)

            if self.check_loss(self.stick_count):
                print("FAIL! Get your shit together. Do you even pick up sticks bro?")
                break

            self.turn_counter += 1

        if self.go_again():
            self.main()
        self.clear()
