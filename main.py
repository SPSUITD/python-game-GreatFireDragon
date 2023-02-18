#  modules
import arcade
# files
import logic
from Card import Card



def main():
    """Main function"""
    window = logic.MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()