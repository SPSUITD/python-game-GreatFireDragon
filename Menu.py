# modules
import arcade
import arcade.gui
from arcade.experimental.uislider import UISlider
import json

f = open("controls.json")
data = json.load(f)

from MainGame import MainGame


from constants import *

from GeneralModule import cursor_coordinates, define_cursor, draw_gradient_bg, get_back_button_create
from basicControls import on_mouse_basic_press, on_mouse_basic_release, on_mouse_basic_motion, on_mouse_basic_enter, on_mouse_basic_leave, on_key_basic_press, on_key_basic_release
    
width, height = arcade.window_commands.get_display_size()   # Window height and width






        
class QuitButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        arcade.close_window()

def create_buttons(self):
    self.v_box = arcade.gui.UIBoxLayout()

    start_button = arcade.gui.UIFlatButton(text="Start Game", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, style=MENU_STYLE)
    self.v_box.add(start_button.with_space_around(bottom=BUTTON_MARGIN))
    start_button.on_click = self.on_click_start

    rules_button = arcade.gui.UIFlatButton(text="Rules", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, style=MENU_STYLE)
    self.v_box.add(rules_button.with_space_around(bottom=BUTTON_MARGIN))
    rules_button.on_click = self.on_click_rules

    controls_button = arcade.gui.UIFlatButton(text="Controls", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, style=MENU_STYLE)
    self.v_box.add(controls_button.with_space_around(bottom=BUTTON_MARGIN))
    controls_button.on_click = self.on_click_controles

    settings_button = arcade.gui.UIFlatButton(text="Settings", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, style=MENU_STYLE)
    self.v_box.add(settings_button.with_space_around(bottom=BUTTON_MARGIN))
    settings_button.on_click = self.on_click_settings

    quit_button = QuitButton(text="Quit", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, style=MENU_STYLE)
    self.v_box.add(quit_button.with_space_around(bottom=BUTTON_MARGIN))

    self.manager.add(arcade.gui.UIAnchorWidget(anchor_x="center_x", anchor_y="center_y", child=self.v_box))

#  MENU -----------------------------------------------------------
class Menu(arcade.View):
    def __init__(self):
        super().__init__()

        self.rules = False
        self.settings = False
        self.controls = False

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
        self.slider_widgets = []


        

    def on_click_start(self, event):
        self.manager.clear()
        view = MainGame()
        view.setup()
        self.window.show_view(view)

    def on_click_settings(self, event):
        self.v_box.clear()
        self.settings = True

        ui_slider = UISlider(value=data["volume"]*100, width=SCREEN_WIDTH*0.9, height=SLIDER_HEIGHT, style=SETTINGS_SLIDER_STYLE)
        label = arcade.gui.UILabel(text=f"{ui_slider.value:02.0f}", font_name=FONT, font_size=FONT_SIZE, text_color=arcade.color.RED, style=SETTINGS_LABEL_STYLE)

        @ui_slider.event()
        def on_change(event: arcade.gui.UIOnChangeEvent):
            label.text = f"{ui_slider.value:02.0f}"
            label.fit_content()

            data["volume"] = ui_slider.value / 100
            with open("controls.json", "w") as jsonFile:
                json.dump(data, jsonFile)

        # to clear slider afterwards
        self.slider_widgets.append(arcade.gui.UIAnchorWidget(child=ui_slider))
        self.slider_widgets.append(arcade.gui.UIAnchorWidget(child=label, anchor_x="center_x", anchor_y="center_y", align_y=50*FS))

        # Fullscreen button
        feelscreen_button = arcade.gui.UIFlatButton(text="fullscreen", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, style=MENU_STYLE)
        self.v_box.add(feelscreen_button.with_space_around(bottom=BUTTON_MARGIN))
        feelscreen_button.on_click = self.on_click_fullscreen

        get_back_button_create(self)

        # adding to gui manager
        self.slider_widgets.append(arcade.gui.UIAnchorWidget(anchor_x="center_x", anchor_y="bottom", child=self.v_box))
        for i in range(len(self.slider_widgets)):
            self.manager.add(self.slider_widgets[i])


        
        
    def on_click_fullscreen(self, event):
        self.window.set_fullscreen(not self.window.fullscreen)
        width, height = self.window.get_size()
        self.window.set_viewport(0, width, 0, height)
        

        data["fullscreen"] = self.window.fullscreen             # Также запись состояния в JSON
        data["FULLSCREEN_SCALE"] = width/SCREEN_WIDTH
        with open("controls.json", "w") as jsonFile:     # чтобы было удобно
            json.dump(data, jsonFile)

        # arcade.close_window()
        arcade.close_window()

    def on_click_rules(self, event):
        self.v_box.clear()
        self.rules = True
        get_back_button_create(self)
        self.manager.add(arcade.gui.UIAnchorWidget(anchor_x="center_x", anchor_y="bottom", child=self.v_box))

    def on_click_controles(self, event):
        self.v_box.clear()
        self.controls = True
        get_back_button_create(self)
        self.manager.add(arcade.gui.UIAnchorWidget(anchor_x="center_x", anchor_y="bottom", child=self.v_box))


    def on_click_get_back(self, event):
        self.v_box.clear()
        if len(self.slider_widgets)>0:
            for i in range(len(self.slider_widgets)):
                self.manager.remove(self.slider_widgets[i])
        self.rules = False
        self.settings = False
        self.controls = False
        create_buttons(self)


    def on_draw(self):
        self.clear()
        self.shapes.draw()          # Gradient BG

        if self.rules:
            left, screen_width, bottom, screen_height = self.window.get_viewport()
            arcade.draw_text("Catch fruits (left click) and bring them to the basket.\nBasket will not stay at one place!\nYour objective is to catch as much fruits as you can untill timer runs off.\nCatch power-ups for help!\nGood luck!",
                            screen_width // 2, screen_height // 2 + 20*FS, font_name=FONT_FUTURE, font_size=FONT_SIZE*1.3, anchor_x="center", anchor_y="center", multiline=True, width=SCREEN_WIDTH*0.9)
        if self.controls:
            left, screen_width, bottom, screen_height = self.window.get_viewport()
            arcade.draw_text("ESC — pause game\nArrow UP↑ — increase volume (+5%)\nArrow DOWN↓ — decrease volume (-5%)\n\n-------c-h-e-a-t-s-------\n\nshift + J — add fruits (can crash the game)\nshift + L — end game\nshift + K — add 10 points",
                            screen_width // 2, screen_height // 2 + 20*FS, font_name=FONT_FUTURE, font_size=FONT_SIZE*1.3, anchor_x="center", anchor_y="center", multiline=True, width=SCREEN_WIDTH*0.9)
        if self.settings:
            arcade.draw_text("Adjust the slider to change music volume: ",
                         SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100*FS, font_name=FONT, font_size=FONT_SIZE, anchor_x="center")
            arcade.draw_text("WARNING! If you press toggle fullscreen button, ",
                         SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 80*FS, font_name=FONT, font_size=FONT_SIZE, color=arcade.color.RED, anchor_x="center")
            arcade.draw_text("The programm will crash itself on purpose.",
                         SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 120*FS, font_name=FONT, font_size=FONT_SIZE, color=arcade.color.RED, anchor_x="center")

        self.manager.draw()         # Buttons (menu) and slider
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