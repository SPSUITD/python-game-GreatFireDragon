# modules
import arcade
import arcade.gui
from arcade.experimental.uislider import UISlider
import json

f = open("static/controls.json")
data = json.load(f)

from static.constants import *
from GeneralModule import get_back_button_create, define_cursor, draw_gradient_bg
from basicControls import on_mouse_basic_press, on_mouse_basic_release, on_mouse_basic_motion, on_mouse_basic_enter, on_mouse_basic_leave, on_key_basic_press, on_key_basic_release
 



class QuitButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        arcade.close_window()

def create_buttons(self):
    self.v_box = arcade.gui.UIBoxLayout()

    start_button = arcade.gui.UIFlatButton(text="Play again", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, style=MENU_STYLE)
    self.v_box.add(start_button.with_space_around(bottom=BUTTON_MARGIN))
    start_button.on_click = self.on_click_start

    get_back_button_create(self, button_text="Main menu")

    quit_button = QuitButton(text="Quit", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, style=MENU_STYLE)
    self.v_box.add(quit_button.with_space_around(bottom=BUTTON_MARGIN))

    self.manager.add(arcade.gui.UIAnchorWidget(anchor_x="center_x", anchor_y="bottom", child=self.v_box))

class EndScreen(arcade.View):
    def __init__(self):
        super().__init__()

        # CURSOR
        self.window.set_mouse_visible(False)
        self.cursor_sprite = arcade.Sprite()
        define_cursor(self)

        #  MANAGER
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # GRADIENT BG
        draw_gradient_bg(self)

        # CREATE BUTTONS
        create_buttons(self)

        # POINTS ANIMATION
        self.score = 0

        # SOUNDS
        if 0 < data["score"]:
            self.slot_machine = arcade.load_sound("sounds/slot_machine.wav")
            self.slot_machine_player = self.slot_machine.play()
            self.slot_machine.set_volume(data["volume"], self.slot_machine_player)
        

        

    def on_click_start(self, event):
        from MainGame import MainGame
        view = MainGame()
        view.setup()
        self.window.show_view(view)

    def on_click_get_back(self, event):
        from Menu import Menu
        view = Menu()
        self.window.show_view(view)


    def on_draw(self):
        self.clear()
        self.shapes.draw()          # Gradient BG

        arcade.draw_text("CONGRATULATIONS",
                         SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150*FS, font_name=("Kenney Future", "comic"), font_size=FONT_SIZE*2, anchor_x="center")
        highest_score = data["highest_score"]
        arcade.draw_text(f"You scored {self.score:02d}",
                         SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 70*FS, font_name=("Kenney Future", "comic"), font_size=FONT_SIZE*3, anchor_x="center")
        arcade.draw_text(f"Highest score is {highest_score}",
                         SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 0*FS, font_name=("Kenney Future", "comic"), font_size=FONT_SIZE*2, anchor_x="center")

        self.manager.draw()         # Buttons (menu) and slider
        self.cursor_sprite.draw()   # должен быть последним!

    def on_update(self, delta_time):
        if self.score < data["score"]:
            self.score += 1
            if self.slot_machine.is_complete(self.slot_machine_player):
                self.slot_machine_player = self.slot_machine.play()
                self.slot_machine.set_volume(data["volume"], self.slot_machine_player)
        else:
            self.slot_machine.stop(self.slot_machine_player)


    
    # CONTROLS -----------------------------------------------------
    def on_mouse_press(self, x, y, button, key_modifiers):
        on_mouse_basic_press(self, x, y, button, key_modifiers)

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        on_mouse_basic_release(self, x, y, button, modifiers)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        on_mouse_basic_motion(self, x, y, dx, dy)

    def on_mouse_enter(self, x, y):
        on_mouse_basic_enter(self, x, y)

    def on_mouse_leave(self, x, y):
        on_mouse_basic_leave(self, x, y)

    def on_key_press(self, symbol, modifiers):
        on_key_basic_press(self, symbol, modifiers)

    def on_key_release(self, symbol, modifiers):
       on_key_basic_release(self, symbol, modifiers)
    # CONTROLS -----------------------------------------------------