# modules
import arcade
# files
import main
from ._constants import *

#  ЛОГИКА
# setup() → on_draw() → on_update()

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.tile_map = None
        self.scene = None
        self.player_sprite = None
        self.physics_engine = None
        self.camera = None
        self.gui_camera = None

        self.score = 0
        # Load sounds
        self.collect_coin_sound = arcade.load_sound(":resources:sounds/coin1.wav")
        self.jump_sound = arcade.load_sound(":resources:sounds/jump1.wav")

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    from ._setup import setup

    def on_draw(self):
        """Render the screen."""

        # Clear the screen to the background color
        self.clear()

        # Activate the game camera
        self.camera.use()


        # Draw our Scene
        self.scene.draw()


        # Activate the GUI camera before drawing GUI elements
        self.gui_camera.use()

        # Draw our score on the screen, scrolling it with the viewport
        score_text = f"Score: {self.score}"
        newText = arcade.Text(score_text,10,10,arcade.csscolor.WHITE,18,)
        newText.draw()

    from ._controls import on_key_press, on_key_release
    from ._camera import center_camera_to_player

    # Здесь основная логика
    def on_update(self, delta_time):
        # Move the player with the physics engine
        self.physics_engine.update()

        # See if we hit any coins
        coin_hit_list = arcade.check_for_collision_with_list(
            self.player_sprite, self.scene["Coins"]
        )

        # Loop through each coin we hit (if any) and remove it
        for coin in coin_hit_list:
            coin.remove_from_sprite_lists()                 # Remove the coin
            arcade.play_sound(self.collect_coin_sound)      # Play a sound
            self.score += 1                                 # Add one to the score

        # Position the camera
        self.center_camera_to_player()