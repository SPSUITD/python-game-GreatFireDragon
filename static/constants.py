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
CURSOR_SCALE = 1

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
SETTINGS_LABEL_STYLE = {
    "font_size": 15,
    "font_name": "Kenney Blocks",
    "font_color": arcade.color.RED,
}
SETTINGS_SLIDER_STYLE = {
    "normal_bg":  arcade.color.NAVAJO_WHITE,
    "normal_border":  arcade.color.ALLOY_ORANGE,
    "normal_border_width": 1,
    "normal_filled_bar":  arcade.color.BARBIE_PINK,
    "normal_unfilled_bar":  arcade.color.BLOND,

    # hovered
    "hovered_bg":  arcade.color.NAVAJO_WHITE,
    "hovered_border":  arcade.color.ORANGE_PEEL,
    "hovered_border_width": 2,
    "hovered_filled_bar":  arcade.color.BARBIE_PINK,
    "hovered_unfilled_bar":  arcade.color.BLOND,

    # pressed
    "pressed_bg":  arcade.color.NAVAJO_WHITE,
    "pressed_border":  arcade.color.OPERA_MAUVE,
    "pressed_border_width": 3,
    "pressed_filled_bar": arcade.color.BARBIE_PINK,
    "pressed_unfilled_bar":  arcade.color.BLOND
}


