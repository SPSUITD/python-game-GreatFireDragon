# modules
import arcade
# files
from Card.__init__ import Card
from static.constants import *
from GeneralModule import cursor_coordinates

class GameOverView(arcade.View):

    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("images/GameOver.jpg")
        self.window.set_mouse_visible(False)
        self.cursor_sprite = arcade.Sprite("images/HANDS_CURSOR_1.png", 1)

    def on_draw(self):
        self.clear()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.cursor_sprite.draw()   # должен быть последним!

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        import GameView
        game_view = GameView.GameView()
        game_view.setup()
        self.window.show_view(game_view)
    
    def on_mouse_motion(self, x, y, dx, dy):
        cursor_coordinates(self, x, y)

    def on_mouse_enter(self, x, y):
        print("mouse in _ instruction view")
        self.cursor_sprite = arcade.Sprite("images/HANDS_CURSOR_1.png", 1)
        cursor_coordinates(self, x, y)