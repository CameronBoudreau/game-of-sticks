import os
from pickup_pvp_updated import *
from pickup_ai_cb import *


def main():
    turn_counter = 1
    pvp = PvPGame()
    pve = AIGame()

    pve.run_game()
    # pvp.run_game()


if __name__ == '__main__':
    main()
