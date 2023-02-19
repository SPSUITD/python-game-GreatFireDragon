#  modules
import arcade
# files
from logic.__init__ import *
from Card.__init__ import *
from InstructionView.__init__ import *
from static.constants import *



def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = InstructionView()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()