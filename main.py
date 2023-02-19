#  modules
import arcade
# files
import GameView
from Card.__init__ import Card
from InstructionView.__init__ import InstructionView
from static.constants import *



def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = InstructionView()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()