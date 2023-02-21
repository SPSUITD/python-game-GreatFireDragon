#  modules
import arcade
# files
from MainGame import MainGame
from Menu import Menu
from static.constants import *

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = Menu()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()

