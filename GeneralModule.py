

def cursor_coordinates(self, x, y):
    self.cursor_sprite.center_x = x
    self.cursor_sprite.center_y = y

def cursor_on_hover(self, x, y):
    # HOVER
    # cards = arcade.get_sprites_at_point((x, y), self.card_list)
    # if len(cards) > 0:
    #     self.cursor_sprite = arcade.Sprite("images/HANDS_CURSOR_2.png", 1)
    # else:
    #     self.cursor_sprite = arcade.Sprite("images/HANDS_CURSOR_1.png", 1)
    pass

def pull_to_top(self, card: arcade.Sprite):
    # Стопка наверх
    # self.card_list.remove(card)
    # self.card_list.append(card)
    pass