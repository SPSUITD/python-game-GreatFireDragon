# modules
import arcade
import random
import json
f = open("controls.json")
data = json.load(f)

from constants import *
from GeneralModule import respawn_fruit, add_fruit_to_physics_engine, swap_fruit_index, add_fruit, add_power_up, teleport_basket
from GeneralModule import normal_basket, normal_fruits
width, height = arcade.window_commands.get_display_size()   # Window height and width


def on_update(self, delta_time):

    if self.on_pause:
        pass
    else:
        fruit_at_basket = self.basket.collides_with_list(self.held_fruits)
        # print(self.fruit_list)
        if len(fruit_at_basket)>0:
            # RESTART FRUIT
            self.held_fruits.pop()
            fruit_at_basket[0].set_position(-200, random.randrange(200, 1000))    # hide the fruit
            self.removed_from_engine = False
            self.physics_engine.add_sprite(fruit_at_basket[0])
            # TELEPORT BASKET
            teleport_basket(self)
            # ANIMATION ON
            self.fruit_pop.set_position(self.basket.position[0], self.basket.position[1])
            self.play_fruit_pop = 1
            # SCORE
            self.added_score_player = self.added_score.play()
            self.added_score.set_volume(data["volume"], self.added_score_player)

            self.gui["score"] += int(fruit_at_basket[0].scale*10/FS)
            score = self.gui["score"]
            self.gui["score_text"].text = f"{score:02d} points"
            

        self.physics_engine.step()

        # Если фрукт Out Of Bounds(OOB)
        for i in range(len(self.active_fruits)):
            if self.active_fruits[i].position[1] < random.randrange(OOB_START, OOB_OVER):
                swap_fruit_index(self, i)


        # TIMER
        self.gui["timer"] -= delta_time
        minutes = int(self.gui["timer"]) // 60
        seconds = int(self.gui["timer"]) % 60
        seconds_100s = int((self.gui["timer"] - seconds -minutes*60) * 100)
        self.gui["timer_text"].text = f"{minutes:02d}:{seconds:02d}:{seconds_100s:02d}"


        if self.gui["timer"] < 10:
            if self.gui["timer"]*10 % 2 > 1:
                self.gui["timer_text"].color = TIMER_ENDING_COLOR
            else:
                self.gui["timer_text"].color = TIMER_COLOR

        if self.gui["timer"] < 0:
            data["score"] = self.gui["score"]
            if self.gui["score"] > data["highest_score"]:
                data["highest_score"] = self.gui["score"]
            with open("controls.json", "w") as jsonFile:     # чтобы было удобно
                json.dump(data, jsonFile)

            from EndScreen import EndScreen
            view = EndScreen()
            self.window.show_view(view)

        # ADDING MORE FRUITS
        if seconds % 20 == 0:
            if not self.fruit_added:
                add_fruit(self)
                self.fruit_added = True
        else:
            self.fruit_added = False
        # ADDING MORE POWER-UPs
        if seconds % 5 == 0:
            if not self.power_up_added:
                self.current_power_up = add_power_up(self)
                self.power_up_added = True
        else:
            self.power_up_added = False





        # Если POWER-UP Out Of Bounds(OOB)
        for i in range(len(self.active_power_ups)):
            if self.active_power_ups[i].position[1] < random.randrange(OOB_START, OOB_OVER):
                self.physics_engine.remove_sprite(self.active_power_ups[i])
                self.power_up_list.insert(self.current_power_up, self.active_power_ups[i])
                self.power_up_list[-1].set_position(0, -200)
                self.active_power_ups.pop(i)

        # POWER-UP TIMER
        if (self.power_up_timer - self.gui["timer"]) > 5:
            normal_basket(self)
            normal_fruits(self)
            self.power_up_timer = 0


        # ANIMATIONS
        if self.play_fruit_pop > 0:
            self.fruit_pop.set_texture(self.play_fruit_pop//2)
            self.play_fruit_pop += 1
            
            self.gui["score_text"].color = SCORE_ADDED_COLOR

            if self.play_fruit_pop > 33*2:
                self.play_fruit_pop = 0
                self.gui["score_text"].color = TIMER_COLOR


                




                

