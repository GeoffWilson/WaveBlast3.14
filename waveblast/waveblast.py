"""
Starting Template

Once you have learned how to use classes, you can begin your program with this
template.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.starting_template
"""
import arcade
import random

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SCREEN_TITLE = "Pyglet Blast"


class Control(object):
    def __init__(self):
        self.lives = 3
        self.score = 0
        self.space_delta = 0


class Star(arcade.Sprite):

    def update(self):
        self.center_x -= 25
        if self.left < 0:
            self.center_x = random.randint(1921, 3840)
            self.center_y = random.randint(0, 1080)


class Shot(arcade.Sprite):

    def update(self):
        self.center_x += 5
        if self.left > SCREEN_WIDTH:
            self.kill()


class MyGame(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.BLACK)

        self.control = None
        self.ship = None
        self.stars = None
        self.hostiles = None
        self.shots = None
        self.friendlies = None

        self.up_pressed = False
        self.down_pressed = False
        self.left_pressed = False
        self.right_pressed = False
        self.space_pressed = False
        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):

        self.control = Control()

        # Create your sprites and sprite lists here
        self.ship = arcade.Sprite('/home/benshiro/PycharmProjects/WaveBlast3.14/sprites/ship.png')
        self.ship.center_x = 100
        self.ship.center_y = SCREEN_HEIGHT / 2

        self.stars = arcade.SpriteList()
        self.hostiles = arcade.SpriteList()
        self.shots = arcade.SpriteList()
        self.friendlies = arcade.SpriteList()

        for _ in range(0, 100):
            star = Star('/home/benshiro/PycharmProjects/WaveBlast3.14/sprites/star.png')
            star.center_x = random.randint(0, 1920)
            star.center_y = random.randint(0, 1080)
            self.stars.append(star)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        # Call draw() on all your sprite lists below
        self.stars.draw()
        self.shots.draw()
        self.ship.draw()

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.ship.change_y = 0
        self.ship.change_x = 0

        if self.up_pressed and not self.down_pressed:
            if self.ship.top < SCREEN_HEIGHT:
                self.ship.change_y = 3
        elif self.down_pressed:
            if self.ship.bottom > 0:
                self.ship.change_y = -3

        if self.left_pressed and not self.right_pressed:
            if self.ship.left > 0:
                self.ship.change_x = -3
        elif self.right_pressed:
            if self.ship.right < SCREEN_WIDTH / 2:
                self.ship.change_x = 3

        if self.space_pressed:
            if self.control.space_delta > 0.16:
                self.create_shot()
                self.control.space_delta = 0
            else:
                self.control.space_delta += delta_time

        self.ship.update()
        self.stars.update()
        self.shots.update()

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        if key == arcade.key.UP:
            self.up_pressed = True

        if key == arcade.key.DOWN:
            self.down_pressed = True

        if key == arcade.key.LEFT:
            self.left_pressed = True

        if key == arcade.key.RIGHT:
            self.right_pressed = True

        if key == arcade.key.SPACE:
            self.space_pressed = True
            self.create_shot()

        if key == arcade.key.ESCAPE:
            exit(0)

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        if key == arcade.key.UP:
            self.up_pressed = False

        if key == arcade.key.DOWN:
            self.down_pressed = False

        if key == arcade.key.LEFT:
            self.left_pressed = False

        if key == arcade.key.RIGHT:
            self.right_pressed = False

        if key == arcade.key.SPACE:
            self.space_pressed = False

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass

    def create_shot(self):
        shot = Shot(
            filename='/home/benshiro/PycharmProjects/WaveBlast3.14/sprites/shot.png',
            center_x=self.ship.right,
            center_y=self.ship.center_y - 3
        )
        self.shots.append(shot)


def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
