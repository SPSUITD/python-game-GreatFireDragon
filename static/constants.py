import arcade
import arcade.gui

# Экран и название
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 576
SCREEN_TITLE = "Drag and Drop Cards"
BG_MAINGAME = arcade.color.AMAZON
BG_MENU = arcade.color.DARK_BLUE_GRAY

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

# SCENE
SCENE_MENU = 0
SCENE_GAME = 1
