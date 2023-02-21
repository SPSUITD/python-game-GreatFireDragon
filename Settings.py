# modules
import arcade
import arcade.gui
import json
f = open("static/controls.json")
data = json.load(f)

from MainGame import MainGame
from static.constants import *
from GeneralModule import cursor_coordinates






    
class SettingsButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        print("settings button clicked")
        # arcade.exit()
        
class QuitButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        print("quit button clicked")
        arcade.exit()

#  MENU -----------------------------------------------------------
class Menu(arcade.View):
    def __init__(self):
        super().__init__()

        # CURSOR
        self.window.set_mouse_visible(False)
        self.cursor_sprite = arcade.Sprite("images/HANDS_CURSOR_1.png", 1)

        #  MANAGER
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        arcade.set_background_color(BG_MENU)

        # Buttons
        self.v_box = arcade.gui.UIBoxLayout()

        start_button = arcade.gui.UIFlatButton(text="Start Game", width=200, style=MENU_STYLE)
        self.v_box.add(start_button.with_space_around(bottom=20))

        settings_button = SettingsButton(text="Settings", width=200, style=MENU_STYLE)
        self.v_box.add(settings_button.with_space_around(bottom=20))
        start_button.on_click = self.on_click_start

        quit_button = QuitButton(text="Quit", width=200, style=MENU_STYLE)
        self.v_box.add(quit_button.with_space_around(bottom=20))

        self.manager.add(
            arcade.gui.UIAnchorWidget(anchor_x="center_x", anchor_y="center_y", child=self.v_box)
            )

    def on_click_start(self, event):
        self.manager.clear()
        game_view = MainGame()
        game_view.setup()
        self.window.show_view(game_view)


    def on_draw(self):
        self.clear()
        self.manager.draw()
        self.cursor_sprite.draw()   # должен быть последним!



    def on_mouse_press(self, x, y, button, key_modifiers):
        # ВЗЯТЬ ОБЪЕКТ
        # cards = arcade.get_sprites_at_point((x, y), self.card_list)

        if button == arcade.MOUSE_BUTTON_LEFT:
            pass
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            pass
        else:
            pass


        # КУРСОР
        self.cursor_sprite = arcade.Sprite("images/HANDS_CURSOR_3.png", 1)
        cursor_coordinates(self, x, y)

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        # ПЕРЕМЕЩЕНИЕ ОБъЕКТОВ
        # if len(self.held_cards) == 0:
        #     pass
        # else:
        #     # SNAP to MATS
        #     pass

        self.cursor_sprite = arcade.Sprite("images/HANDS_CURSOR_1.png", 1)
        cursor_coordinates(self, x, y)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        # ПЕРЕМЕЩЕНИЕ ОБъЕКТОВ
        # if len(self.held_cards) > 0:
        #     for card in self.held_cards:
        #         card.center_x += dx
        #         card.center_y += dy
        # else:
        #     cursor_on_hover(self, x, y)

        # КУРСОР
        cursor_coordinates(self, x, y)

    def on_mouse_enter(self, x, y):
        self.cursor_sprite = arcade.Sprite("images/HANDS_CURSOR_1.png", 1)
        cursor_coordinates(self, x, y)

    def on_mouse_leave(self, x, y):
        # IMPLEMENT PAUSE
        pass

    def on_key_press(self, symbol, modifiers):
        # f11 для смены режима fullscreen
        if symbol == 65480:
            self.set_fullscreen(not self.fullscreen)
            data["fullscreen"] = self.fullscreen                    # Также запись состояния в JSON
            with open("static/controls.json", "w") as jsonFile:     # чтобы было удобно
                json.dump(data, jsonFile)
                
            self.set_viewport(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT)    # чтобы растянуть на весь экран

    def on_key_release(self, symbol, modifiers):
        pass



