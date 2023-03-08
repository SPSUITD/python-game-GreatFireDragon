# modules
import arcade
import random
import json
f = open("static/controls.json")
data = json.load(f)

from static.constants import *
from GeneralModule import respawn_fruit, add_fruit_to_physics_engine, swap_fruit_index
width, height = arcade.window_commands.get_display_size()   # Window height and width


def on_update(self, delta_time):

    if self.on_pause:
        pass
    else:
        fruit_at_hoop = self.hoop.collides_with_list(self.held_fruits)
        # print(self.fruit_list)
        if len(fruit_at_hoop)>0:
            self.held_fruits.pop()
            fruit_at_hoop[0].set_position(-200, random.randrange(200, 1000))    # hide the fruit
            self.removed_from_engine = False
            self.physics_engine.add_sprite(fruit_at_hoop[0])

            # ANIMATION ON
            self.play_fruit_pop = 1
            # SCORE
            self.gui["score"] += int(fruit_at_hoop[0].scale*10/FS)
            score = self.gui["score"]
            self.gui["score_text"].text = f"{score} points"

        self.physics_engine.step()

        # Если фрукт Out Of Bounds(OOB)
        for i in range(len(self.active_fruits)):
            if self.active_fruits[i].position[1] < random.randrange(-500, -200):
                swap_fruit_index(self, i)


        # TIMER
        self.gui["timer"] -= delta_time
        minutes = int(self.gui["timer"]) // 60
        seconds = int(self.gui["timer"]) % 60
        seconds_100s = int((self.gui["timer"] - seconds) * 100)
        self.gui["timer_text"].text = f"{minutes:02d}:{seconds:02d}:{seconds_100s:02d}"

        if self.gui["timer"] < 10:
            if self.gui["timer"]*10 % 2 > 1:
                self.gui["timer_text"].color = arcade.color.RED
            else:
                self.gui["timer_text"].color = arcade.color.ORANGE_RED

        if self.gui["timer"] < 0:
            data["score"] = self.gui["score"]
            if self.gui["score"] > data["highest_score"]:
                data["highest_score"] = self.gui["score"]
            with open("static/controls.json", "w") as jsonFile:     # чтобы было удобно
                json.dump(data, jsonFile)

            from EndScreen import EndScreen
            view = EndScreen()
            self.window.show_view(view)


        # ANIMATIONS
        if self.play_fruit_pop > 0:
            self.fruit_pop.update_animation()
            self.play_fruit_pop += 1

            if self.play_fruit_pop > 85:
                self.play_fruit_pop = 0




                

