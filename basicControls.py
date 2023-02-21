import arcade
from static.constants import *
from GeneralModule import cursor_coordinates, cursor_on_hover



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
        self.window.set_fullscreen(not self.window.fullscreen)
        data["fullscreen"] = self.window.fullscreen                    # Также запись состояния в JSON
        with open("static/controls.json", "w") as jsonFile:     # чтобы было удобно
            json.dump(data, jsonFile)
            
        self.set_viewport(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT)    # чтобы растянуть на весь экран

def on_key_release(self, symbol, modifiers):
    pass


