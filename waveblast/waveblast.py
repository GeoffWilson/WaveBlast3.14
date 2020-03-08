"""
WaveBlast 3.14 base code

"""
import random
from typing import Optional

import arcade

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SCREEN_TITLE = "Pyglet Blast"


class Control(object):
    """
    Main game control class
    """

    def __init__(self):
        self.lives = 3
        self.score = 0
        self.space_delta = 0

    def update(self):
        """
        updates the state of the game, doesn't do anything for now
        """
        pass


class Star(arcade.Sprite):
    """
    Class to represent a background star
    """

    def update(self):
        self.center_x -= 25
        if self.left < 0:
            self.center_x = random.randint(1921, 3840)
            self.center_y = random.randint(0, 1080)


class Shot(arcade.Sprite):
    """
    Class to represent a fired shot
    """

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
        super().__init__(width, height, title, antialiasing=True)

        arcade.set_background_color(arcade.color.BLACK)

        # Game control object
        self.control: Control = Control()

        # Your ship
        self.ship: Optional[arcade.sprite_list.Sprite] = None

        # Sprite lists
        self.stars: Optional[arcade.sprite_list.SpriteList] = None
        self.hostiles: Optional[arcade.sprite_list.SpriteList] = None
        self.shots: Optional[arcade.sprite_list.SpriteList] = None
        self.friendlies: Optional[arcade.sprite_list.SpriteList] = None

        # Key event handler variables
        self.up_pressed: bool = False
        self.down_pressed: bool = False
        self.left_pressed: bool = False
        self.right_pressed: bool = False
        self.space_pressed: bool = False

        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):

        # Create your sprites and sprite lists here
        self.ship = arcade.Sprite('./sprites/ship.png')
        self.ship.center_x = 100
        self.ship.center_y = SCREEN_HEIGHT / 2

        self.stars = arcade.SpriteList()
        self.hostiles = arcade.SpriteList()
        self.shots = arcade.SpriteList()
        self.friendlies = arcade.SpriteList()

        for _ in range(0, 100):
            star = Star('./sprites/star.png')
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
        self.ship.change_x = 0
        self.ship.change_y = 0

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
                self._create_shot()
                self.control.space_delta = 0
            else:
                self.control.space_delta += delta_time

        # Update everything
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
            self._create_shot()

        # Quit the game
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

    def _create_shot(self):
        """
        Creates a new shot at the current ship location
        :return:
        """
        shot = Shot(
            filename='./sprites/shot.png',
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
