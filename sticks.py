import os
from pickup_pvp_updated import *


def main():
    turn_counter = 1
    pvp = PvPGame()
    # pve = AIGame()
    # pve.run_game() <---Not quite working, but it's so close!

    pvp.run_game()


if __name__ == '__main__':
    main()
