# modules
import arcade
import arcade.gui
from arcade.experimental.uislider import UISlider
import json
f = open("static/controls.json")
data = json.load(f)

# from Menu import Menu
import Menu
from static.constants import *
from GeneralModule import cursor_coordinates, define_cursor

from basicControls import on_mouse_basic_press, on_mouse_basic_release, on_mouse_basic_motion, on_mouse_basic_enter, on_mouse_basic_leave, on_key_basic_press, on_key_basic_release
    




def create_buttons(self):
    self.v_box = arcade.gui.UIBoxLayout()

    get_back_button = arcade.gui.UIFlatButton(text="← Get Back", width=200, style=MENU_STYLE)
    self.v_box.add(get_back_button.with_space_around(bottom=20))
    get_back_button.on_click = self.on_click_get_back




    ui_slider = UISlider(value=data["volume"]*100, width=SCREEN_WIDTH*0.9, height=50, style=SETTINGS_SLIDER_STYLE)
    label = arcade.gui.UILabel(text=f"{ui_slider.value:02.0f}", font_name=FONT, font_size=30, text_color=arcade.color.RED, style=SETTINGS_LABEL_STYLE)

    @ui_slider.event()
    def on_change(event: arcade.gui.UIOnChangeEvent):
        label.text = f"{ui_slider.value:02.0f}"
        label.fit_content()

        data["volume"] = ui_slider.value / 100
        with open("static/controls.json", "w") as jsonFile:
            json.dump(data, jsonFile)

    self.manager.add(arcade.gui.UIAnchorWidget(child=ui_slider))
    self.manager.add(arcade.gui.UIAnchorWidget(child=label, anchor_x="center_x", anchor_y="center_y", align_y=50))
    self.manager.add(arcade.gui.UIAnchorWidget(anchor_x="center_x", anchor_y="bottom", child=self.v_box))

#  MENU -----------------------------------------------------------
class Settings(arcade.View):
    def __init__(self):
        super().__init__()

        # CURSOR
        self.window.set_mouse_visible(False)
        self.cursor_sprite = arcade.Sprite()
        define_cursor(self)

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




    def on_click_get_back(self, event):
        self.manager.clear()
        view = Menu.Menu()
        view.manager.enable()
        self.window.show_view(view)


    def on_draw(self):
        self.clear()
        self.shapes.draw()          # Gradient BG 
        arcade.draw_text("Adjust the slider to change music volume: ",
                         SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100, font_name=FONT, font_size=SETTIGNS_FONT_SIZE, anchor_x="center")
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