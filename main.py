#  modules
import arcade
# files
from MainGame import MainGame
from static.constants import *



def main():
    window = MainGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()