# modules
import arcade
import arcade.gui
import json
f = open("static/controls.json")
data = json.load(f)

from MainGame import MainGame
from Settings import Settings
from Rules import Rules
from static.constants import *
from GeneralModule import cursor_coordinates, define_cursor, draw_gradient_bg

from basicControls import on_mouse_basic_press, on_mouse_basic_release, on_mouse_basic_motion, on_mouse_basic_enter, on_mouse_basic_leave, on_key_basic_press, on_key_basic_release
    
width, height = arcade.window_commands.get_display_size()   # Window height and width


    
        
class QuitButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        print("quit button clicked")
        arcade.exit()

def create_buttons(self):
    self.v_box = arcade.gui.UIBoxLayout()

    start_button = arcade.gui.UIFlatButton(text="Start Game", width=BUTTON_WIDTH, style=MENU_STYLE)
    self.v_box.add(start_button.with_space_around(bottom=BUTTON_MARGIN))
    start_button.on_click = self.on_click_start

    rules_button = arcade.gui.UIFlatButton(text="Rules", width=BUTTON_WIDTH, style=MENU_STYLE)
    self.v_box.add(rules_button.with_space_around(bottom=BUTTON_MARGIN))
    rules_button.on_click = self.on_click_rules

    settings_button = arcade.gui.UIFlatButton(text="Settings", width=BUTTON_WIDTH, style=MENU_STYLE)
    self.v_box.add(settings_button.with_space_around(bottom=BUTTON_MARGIN))
    settings_button.on_click = self.on_click_settings

    quit_button = QuitButton(text="Quit", width=BUTTON_WIDTH, style=MENU_STYLE)
    self.v_box.add(quit_button.with_space_around(bottom=BUTTON_MARGIN))

    self.manager.add(
        arcade.gui.UIAnchorWidget(anchor_x="center_x", anchor_y="center_y", child=self.v_box)
        )

#  MENU -----------------------------------------------------------
class Menu(arcade.View):
    def __init__(self):
        super().__init__()

        self.rules = False
        self.settings = False

        # CURSOR
        self.window.set_mouse_visible(False)
        self.cursor_sprite = arcade.Sprite()
        define_cursor(self)

        #  MANAGER
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        arcade.set_background_color(BG_MENU)        # ATAVISM

        # GRADIENT BG
        draw_gradient_bg(self)

        # CREATE BUTTONS
        create_buttons(self)

        

    def on_click_start(self, event):
        self.manager.clear()
        view = MainGame()
        view.setup()
        self.window.show_view(view)

    def on_click_settings(self, event):
        self.v_box.clear()
        self.settings = True

    def on_click_rules(self, event):
        self.v_box.clear()
        self.rules = True
        self.v_box = arcade.gui.UIBoxLayout()

        get_back_button = arcade.gui.UIFlatButton(text="← Get Back", width=200, style=MENU_STYLE)
        self.v_box.add(get_back_button.with_space_around(bottom=20))
        get_back_button.on_click = self.on_click_get_back


        self.manager.add(
            arcade.gui.UIAnchorWidget(anchor_x="center_x", anchor_y="bottom", child=self.v_box)
            )


    def on_click_get_back(self, event):
        self.v_box.clear()
        self.rules = False
        create_buttons(self)



    def on_draw(self):
        self.clear()
        self.shapes.draw()          # Gradient BG

        if self.rules:
            left, screen_width, bottom, screen_height = self.window.get_viewport()
            arcade.draw_text("Congue inceptos orci quam mauris per vitae maecenas.",
                            screen_width // 2, screen_height // 2 + 60, font_name=FONT, font_size=SETTIGNS_FONT_SIZE, anchor_x="center")
            arcade.draw_text("Dapibus sociosqu tristique hymenaeos bibendum commodo",
                            screen_width // 2, screen_height // 2 + 20, font_name=FONT, font_size=SETTIGNS_FONT_SIZE, anchor_x="center")
            arcade.draw_text("semper nunc cum accumsan velit class commodo.",
                            screen_width // 2, screen_height // 2 - 20, font_name=FONT, font_size=SETTIGNS_FONT_SIZE, anchor_x="center")
            arcade.draw_text("Est mollis cum vulputate nulla ad Gravida in vivamus.",
                            screen_width // 2, screen_height // 2 - 60, font_name=FONT, font_size=SETTIGNS_FONT_SIZE, anchor_x="center")
        if self.settings:
            pass

        self.manager.draw()         # Buttons (menu)
        self.cursor_sprite.draw()   # должен быть последним!

   
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