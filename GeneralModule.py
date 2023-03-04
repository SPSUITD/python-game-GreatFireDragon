import arcade
import arcade.gui
from pyglet.math import Vec2
from static.constants import *
import json

width, height = arcade.window_commands.get_display_size()   # Window height and width

def cursor_coordinates(self, x, y):
    # if self.window.fullscreen:        
    #     x = ( x / width ) * SCREEN_WIDTH
    #     y = ( y / height ) * SCREEN_HEIGHT
    self.cursor_sprite.center_x = x
    self.cursor_sprite.center_y = y

def is_cursor_hover_fruit(self, x, y):
    fruits_at_cursor = arcade.get_sprites_at_point((x, y), self.fruit_list)
    cursor_N = 0
    if len(self.held_fruits) == 0:         # Если мы ничего не держим
        cursor_N = 1 if len(fruits_at_cursor) > 0 else 2 if self.mouse_is_pressed else 0
    else:
        cursor_N = 2

    self.cursor_sprite.set_texture(cursor_N)
    cursor_coordinates(self, x, y)

# В ситуации, когда мы кликнули на объект, который находистя позади 
# другого объекта. Мы хотим, чтобы кликнутый нами "активный" объект
# окахался наверху. Это приятнее для восприятия.
def pull_to_top(self, fruit: arcade.Sprite):
        self.fruit_list.remove(fruit)
        self.fruit_list.append(fruit)


def define_cursor(self):
    self.cursor_sprite.scale= CURSOR_SCALE
    for i in range(1,4):
        texture = arcade.load_texture(
                f"images/HANDS_CURSOR_{i}.png",
                x = 0, y = 0
            )
        self.cursor_sprite.append_texture(texture)
    self.cursor_sprite.set_texture(0)

def draw_gradient_bg(self):
    f = open("static/controls.json")
    data = json.load(f)
    FS = data["FULLSCREEN_SCALE"]

    self.shapes = arcade.ShapeElementList()
    gp = []
    for point in GRADIENT_POINTS:
        gp.append([x * FS for x in point])
    gp_list = gp[0], gp[1], gp[2], gp[3]
    rect = arcade.create_rectangle_filled_with_colors(gp_list, GRADIENT_COLOR)
    self.shapes.append(rect)

def get_back_button_create(self):
    get_back_button = arcade.gui.UIFlatButton(text="← Get Back", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, style=MENU_STYLE)
    self.v_box.add(get_back_button.with_space_around(bottom=BUTTON_MARGIN))
    get_back_button.on_click = self.on_click_get_back