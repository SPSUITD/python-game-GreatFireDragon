import arcade
import arcade.gui

import json
f = open("controls.json")
data = json.load(f)
FS = data["FULLSCREEN_SCALE"]



# Главная информация
SCREEN_WIDTH = int(1024*FS)
SCREEN_HEIGHT = int(576*FS)
SCREEN_TITLE = "Fruit Catcher"
BG_MAINGAME = arcade.color.AMAZON
BG_MENU = arcade.color.DARK_BLUE_GRAY
FONT = "Kenney Blocks"
FONT_FUTURE = ("Kenney Future", "comic")


# Scaling
CURSOR_SCALE = 1*FS
BASKET_SCALE = 0.1*FS
FRUIT_SCALE = 0.4*FS

BUTTON_MARGIN = 20*FS
BUTTON_WIDTH = 200*FS
BUTTON_HEIGHT = 50*FS
FONT_SIZE = 18*FS
POWER_UP_SCALE = 0.2*FS
FRUIT_POP_SCALE = 0.3*FS

# PHISICS ENGINE
GRAVITY = 1500*FS
DEFAULT_DAMPING = 1.0

FRUIT_MAX_HORIZONTAL_SPEED = 1000*FS
FRUIT_MAX_VERTICAL_SPEED = 1600*FS
FRUIT_DAMPING = 0 #0.2
FRUIT_FRICTION = 0 #1.0
FRUIT_MASS = 10*FS
FRUIT_IMPULSE = 1320*FS
FRUIT_MOMENT_OF_ENERTIA = 5000*FS

# MENU
MENU_STYLE = {
    "font_size": 15*FS,
    "font_name": "Kenney Blocks",
    "font_color": arcade.color.RED,
    "bg_color": arcade.color.ALMOND,
    "border_color": arcade.color.BLOND,
    "border_width": 3*FS,


    "bg_color_pressed": arcade.color.RED,
    "border_color_pressed": arcade.color.RED, 
    "font_color_pressed": arcade.color.RED,
}

color1 = (215, 214, 165)
color2 = (219, 166, 123)
GRADIENT_POINTS = [(0, 0), (SCREEN_WIDTH, 0), (SCREEN_WIDTH, SCREEN_HEIGHT), (0, SCREEN_HEIGHT)]
GRADIENT_COLOR = (color1, color1, color2, color2)

# SETTINGS
SETTINGS_LABEL_STYLE = {
    "font_size": 15*FS,
    "font_name": "Kenney Blocks",
    "font_color": arcade.color.RED,
}
SETTINGS_SLIDER_STYLE = {
    "normal_bg":  arcade.color.NAVAJO_WHITE,
    "normal_border":  arcade.color.ALLOY_ORANGE,
    "normal_border_width": 1*FS,
    "normal_filled_bar":  arcade.color.BARBIE_PINK,
    "normal_unfilled_bar":  arcade.color.BLOND,

    # hovered
    "hovered_bg":  arcade.color.NAVAJO_WHITE,
    "hovered_border":  arcade.color.ORANGE_PEEL,
    "hovered_border_width": 2*FS,
    "hovered_filled_bar":  arcade.color.BARBIE_PINK,
    "hovered_unfilled_bar":  arcade.color.BLOND,

    # pressed
    "pressed_bg":  arcade.color.NAVAJO_WHITE,
    "pressed_border":  arcade.color.OPERA_MAUVE,
    "pressed_border_width": 3*FS,
    "pressed_filled_bar": arcade.color.BARBIE_PINK,
    "pressed_unfilled_bar":  arcade.color.BLOND
}

# SLIDER
SLIDER_HEIGHT = 50*FS


# OOB
OOB_START = -1000
OOB_OVER = -500


# GUI
TIMER_COLOR = arcade.color.ORANGE_PEEL
TIMER_ENDING_COLOR = arcade.color.ORANGE_RED
SCORE_COLOR = arcade.color.ORANGE_PEEL
SCORE_ADDED_COLOR = arcade.color.GREEN


