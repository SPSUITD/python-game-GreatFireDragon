#  modules
import arcade
import json
f = open("static/controls.json")
data = json.load(f)
# files
from MainGame import MainGame
from Menu import Menu
from static.constants import *

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, fullscreen=data["fullscreen"])
    start_view = Menu()
    # start_view = MainGame()
    # start_view.setup()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()

