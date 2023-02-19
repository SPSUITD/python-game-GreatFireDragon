# modules
import arcade
# files
import GameView
from Card.__init__ import Card
from static.constants import *
from GeneralModule import cursor_coordinates

class InstructionView(arcade.View):
    def __init__(self):
        super().__init__()
        self.window.set_mouse_visible(False)
        self.cursor_sprite = arcade.Sprite("images/HANDS_CURSOR_1.png", 1)

    def on_show_view(self):
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)
        arcade.set_viewport(0, self.window.width, 0, self.window.height)    #if scrolling game

    def on_draw(self):
        self.clear()
        arcade.draw_text("Instructions Screen", self.window.width / 2, self.window.height / 2, arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Click to advance", self.window.width / 2, self.window.height / 2-75, arcade.color.WHITE, font_size=20, anchor_x="center")
        self.cursor_sprite.draw()   # должен быть последним!


    def on_mouse_press(self, x, y, button, modifiers):
        # КУРСОР
        self.cursor_sprite = arcade.Sprite("images/HANDS_CURSOR_3.png", 1)
        cursor_coordinates(self, x, y)


        game_view = GameView.GameView()
        game_view.setup()
        self.window.show_view(game_view)

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        self.cursor_sprite = arcade.Sprite("images/HANDS_CURSOR_1.png", 1)
        cursor_coordinates(self, x, y)

    def on_mouse_motion(self, x, y, dx, dy):
        cursor_coordinates(self, x, y)

    def on_mouse_enter(self, x, y):
        self.cursor_sprite = arcade.Sprite("images/HANDS_CURSOR_1.png", 1)
        cursor_coordinates(self, x, y)
