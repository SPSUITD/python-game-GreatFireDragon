#  modules
import arcade
# files
import logic



def main():
    """Main function"""
    window = logic.MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()