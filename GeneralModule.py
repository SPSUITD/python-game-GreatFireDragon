import arcade
import arcade.gui
import random
from pyglet.math import Vec2
from constants import *
import json

width, height = arcade.window_commands.get_display_size()   # Window height and width

# CURSOR FUNCTIONS
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


def define_cursor(self):
    self.cursor_sprite.scale= CURSOR_SCALE
    # self.cursor_sprite.center_x = SCREEN_WIDTH//2
    # self.cursor_sprite.center_y = SCREEN_HEIGHT//2
    for i in range(1,4):
        texture = arcade.load_texture(
                f"images/HANDS_CURSOR_{i}.png",
                x = 0, y = 0
            )
        self.cursor_sprite.append_texture(texture)
    self.cursor_sprite.set_texture(0)

# GUI functions
def draw_gradient_bg(self):
    f = open("controls.json")
    data = json.load(f)
    FS = data["FULLSCREEN_SCALE"]

    self.shapes = arcade.ShapeElementList()
    gp = []
    for point in GRADIENT_POINTS:
        gp.append([x * FS for x in point])
    gp_list = gp[0], gp[1], gp[2], gp[3]
    rect = arcade.create_rectangle_filled_with_colors(gp_list, GRADIENT_COLOR)
    self.shapes.append(rect)

def get_back_button_create(self, button_text="← Get Back"):
    get_back_button = arcade.gui.UIFlatButton(text=button_text, width=BUTTON_WIDTH, height=BUTTON_HEIGHT, style=MENU_STYLE)
    self.v_box.add(get_back_button.with_space_around(bottom=BUTTON_MARGIN))
    get_back_button.on_click = self.on_click_get_back


# RESPAWN FRUITS WHEN THEY OFF THE SCREEN (y)
def respawn_fruit(self, fruit):
    
    # self.physics_engine.remove_sprite(fruit)

    new_fruit_position = random.normalvariate(SCREEN_WIDTH/2, SCREEN_WIDTH/4)
    if new_fruit_position < 0:
        new_fruit_position = 0
    if new_fruit_position > SCREEN_WIDTH:
        new_fruit_position = SCREEN_WIDTH

    deviation = new_fruit_position - SCREEN_WIDTH/2
    try:
        self.physics_engine.set_position(fruit, (new_fruit_position, -100))
        self.physics_engine.set_velocity(fruit, (-deviation*1.4, FRUIT_IMPULSE))  
    except:
        pass


 # ADD FRUITS TO PHYSICS ENGINE
def add_fruit_to_physics_engine(self, fruit):
    self.physics_engine.add_sprite(fruit,
                                    friction=FRUIT_FRICTION,
                                    mass=FRUIT_MASS,
                                    moment_of_inertia = FRUIT_MOMENT_OF_ENERTIA,
                                    # moment=arcade.PymunkPhysicsEngine.MOMENT_INF,
                                    elasticity= 0.5,
                                    collision_type="fruit",
                                    max_horizontal_velocity=FRUIT_MAX_HORIZONTAL_SPEED,
                                    max_vertical_velocity=FRUIT_MAX_VERTICAL_SPEED)

    return fruit

# i → self.active_fruits[i]
def swap_fruit_index(self, i):
    try:
        random_index = random.randrange(0, len(self.fruit_list))
    
        self.physics_engine.remove_sprite(self.active_fruits[i])
        self.fruit_list.append(self.active_fruits[i])
        self.active_fruits.pop(i)
        
        self.active_fruits.append(self.fruit_list[random_index])
        self.fruit_list.pop(random_index)
        add_fruit_to_physics_engine(self, self.active_fruits[-1])

        respawn_fruit(self, self.active_fruits[-1])
    except:
        respawn_fruit(self, self.active_fruits[i])



def add_fruit(self):
    try:
        print("GM: Fruit added. Currently ", len(self.active_fruits), " active fruits!")
        random_index = random.randrange(0, len(self.fruit_list))
        self.active_fruits.append(self.fruit_list[random_index])
        add_fruit_to_physics_engine(self, self.active_fruits[-1])
        self.fruit_list.pop(random_index)
    except:
        print("GM: can't add fruit, out of stock ;)")

def teleport_basket(self):
    self.basket.center_x = random.randrange(int(SCREEN_WIDTH*0.1), int(SCREEN_WIDTH*0.9))
    self.basket.center_y = random.randrange(int(SCREEN_HEIGHT*0.1), int(SCREEN_HEIGHT*0.9))

# POWER-UPs
def add_power_up(self):
    random_index = random.randrange(0, len(self.power_up_list))
    self.active_power_ups.append(self.power_up_list[random_index])
    add_fruit_to_physics_engine(self, self.active_power_ups[-1])
    self.power_up_list.pop(random_index)
    respawn_fruit(self, self.active_power_ups[-1])
    print("GM: power-up added!")

    return random_index # This will become self.current_power_up

def big_basket(self):
    self.basket.scale = BASKET_SCALE*2
    self.fruit_pop.scale = FRUIT_POP_SCALE*2
def normal_basket(self):
    self.basket.scale = BASKET_SCALE
    self.fruit_pop.scale = FRUIT_POP_SCALE

def x2_fruits(self):
    for fruit in self.fruit_list:
        fruit.scale = FRUIT_SCALE*2
    for fruit in self.active_fruits:
        fruit.scale = FRUIT_SCALE*2
def normal_fruits(self):
    for fruit in self.fruit_list:
        fruit.scale = FRUIT_SCALE
    for fruit in self.active_fruits:
        fruit.scale = FRUIT_SCALE

def more_time(self):
    self.gui["timer"] += 15
