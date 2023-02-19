# modules
import arcade
# files
import main
from logic.__init__ import *
from Card.__init__ import *
from static.constants import *

class InstructionView(arcade.View):

    def on_show_view(self):
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)
        arcade.set_viewport(0, self.window.width, 0, self.window.height)    #if scrolling game

    def on_draw(self):
        self.clear()
        arcade.draw_text("Instructions Screen", self.window.width / 2, self.window.height / 2, arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Click to advance", self.window.width / 2, self.window.height / 2-75, arcade.color.WHITE, font_size=20, anchor_x="center")
    
    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, start the game. """
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)