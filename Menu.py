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
from GeneralModule import cursor_coordinates

from basicControls import on_mouse_basic_press, on_mouse_basic_release, on_mouse_basic_motion, on_mouse_basic_enter, on_mouse_basic_leave, on_key_basic_press, on_key_basic_release
    







    
        
class QuitButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        print("quit button clicked")
        arcade.exit()

def create_buttons(self):
    self.v_box = arcade.gui.UIBoxLayout()

    start_button = arcade.gui.UIFlatButton(text="Start Game", width=200, style=MENU_STYLE)
    self.v_box.add(start_button.with_space_around(bottom=20))
    start_button.on_click = self.on_click_start

    rules_button = arcade.gui.UIFlatButton(text="Rules", width=200, style=MENU_STYLE)
    self.v_box.add(rules_button.with_space_around(bottom=20))
    rules_button.on_click = self.on_click_rules

    settings_button = arcade.gui.UIFlatButton(text="Settings", width=200, style=MENU_STYLE)
    self.v_box.add(settings_button.with_space_around(bottom=20))
    settings_button.on_click = self.on_click_settings

    quit_button = QuitButton(text="Quit", width=200, style=MENU_STYLE)
    self.v_box.add(quit_button.with_space_around(bottom=20))

    self.manager.add(
        arcade.gui.UIAnchorWidget(anchor_x="center_x", anchor_y="center_y", child=self.v_box)
        )

#  MENU -----------------------------------------------------------
class Menu(arcade.View):
    def __init__(self):
        super().__init__()
        # width, height = self.window.get_size()
        # self.window.set_viewport(0, width, 0, height)

        # CURSOR
        self.window.set_mouse_visible(False)
        self.cursor_sprite = arcade.Sprite("images/HANDS_CURSOR_1.png", 1)

        #  MANAGER
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        arcade.set_background_color(BG_MENU)        # ATAVISM

        # GRADIENT BG
        self.shapes = arcade.ShapeElementList()
        rect = arcade.create_rectangle_filled_with_colors(GRADIENT_POINTS, GRADIENT_COLOR)
        self.shapes.append(rect)
        # GRADIENT BG

        create_buttons(self)
        

   

    def on_click_start(self, event):
        self.manager.clear()
        view = MainGame()
        view.setup()
        self.window.show_view(view)

    def on_click_settings(self, event):
        self.manager.clear()
        view = Settings()
        self.window.show_view(view)

    def on_click_rules(self, event):
        self.manager.clear()
        view = Rules()
        self.window.show_view(view)


    def on_draw(self):
        self.clear()
        self.shapes.draw()          # Gradient BG



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


        # if symbol == 65480:
        #     self.manager.clear()
        #     left, screen_width, bottom, screen_height = self.window.get_viewport()

        #     self.v_box = arcade.gui.UIBoxLayout()

        #     start_button = arcade.gui.UIFlatButton(text="Start Game", width=200, style=MENU_STYLE)
        #     self.v_box.add(start_button.with_space_around(bottom=20))
        #     start_button.on_click = self.on_click_start

        #     settings_button = arcade.gui.UIFlatButton(text="Settings", width=200, style=MENU_STYLE)
        #     self.v_box.add(settings_button.with_space_around(bottom=20))
        #     settings_button.on_click = self.on_click_settings

        #     quit_button = QuitButton(text="Quit", width=200, style=MENU_STYLE)
        #     self.v_box.add(quit_button.with_space_around(bottom=20))


            # self.manager.add(arcade.gui.UIAnchorWidget(anchor_x="center_x", anchor_y="center_y", child=self.v_box))
            # self.manager.add(arcade.gui.UILayout(300, 350, children=self.v_box))

            

    def on_key_release(self, symbol, modifiers):
       on_key_basic_release(self, symbol, modifiers)
    # CONTROLS -----------------------------------------------------