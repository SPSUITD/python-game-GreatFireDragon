import arcade
import arcade.gui

# Главная информация
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 576
SCREEN_TITLE = "Drag and Drop Cards"
BG_MAINGAME = arcade.color.AMAZON
BG_MENU = arcade.color.DARK_BLUE_GRAY
FONT = "Kenney Blocks"

# Scaling
CARD_SCALE = 0.6

# MENU
MENU_STYLE = {
    "font_size": 15,
    "font_name": "Kenney Blocks",
    "font_color": arcade.color.RED,
    "bg_color": arcade.color.ALMOND,
    "border_color": arcade.color.BLOND,
    "border_width": 3,


    "bg_color_pressed": arcade.color.RED,
    "border_color_pressed": arcade.color.RED, 
    "font_color_pressed": arcade.color.RED,
}

color1 = (215, 214, 165)
color2 = (219, 166, 123)
GRADIENT_POINTS = (0, 0), (SCREEN_WIDTH, 0), (SCREEN_WIDTH, SCREEN_HEIGHT), (0, SCREEN_HEIGHT)
GRADIENT_COLOR = (color1, color1, color2, color2)

# SETTINGS
SETTIGNS_FONT_SIZE = 18

# SCENE
SCENE_MENU = 0
SCENE_GAME = 1
