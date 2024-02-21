import pygame as pg
from random import randrange
import sys

vec2 = pg.math.Vector2

class Snake:
    """A class to manage snake characteristics throughout the game."""
    def __init__(self, ai_game):
        """Initialize snake object characteristics."""
        self.game = ai_game
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.size = self.settings.tile_size
        self.w_size = self.settings.window_size
        self.rect = pg.rect.Rect(0, 0, self.size - 2, self.size - 2)
        self.rect.center = self.get_random_position()
        self.direction = vec2(self.size, 0)
        self.time = 0
        self.length = 1
        self.segments = []
        self.allowed_dir = {pg.K_UP: 1, pg.K_DOWN: 1, pg.K_LEFT: 1, pg.K_RIGHT: 1}

    def delta_time(self):
        """Create a time delay to control how fast the snake moves."""
        time_now = pg.time.get_ticks()
        if time_now - self.time > self.settings.step_delay:
            self.time = time_now
            return True

    def get_random_position(self):
        """Return a random number that match the center position of each cell."""
        return [randrange(self.size // 2, (self.w_size / 2 - self.size // 2), self.size)] * 2

    def control(self, event):
        if event.key == pg.K_LEFT and self.allowed_dir[pg.K_LEFT]:
            self.direction = vec2(-self.size, 0)
            self.allowed_dir = {pg.K_UP: 1, pg.K_DOWN: 1, pg.K_LEFT: 1, pg.K_RIGHT: 0}
        elif event.key == pg.K_RIGHT and self.allowed_dir[pg.K_RIGHT]:
            self.direction = vec2(self.size, 0)
            self.allowed_dir = {pg.K_UP: 1, pg.K_DOWN: 1, pg.K_LEFT: 0, pg.K_RIGHT: 1}
        elif event.key == pg.K_UP and self.allowed_dir[pg.K_UP]:
            self.direction = vec2(0, -self.size)
            self.allowed_dir = {pg.K_UP: 1, pg.K_DOWN: 0, pg.K_LEFT: 1, pg.K_RIGHT: 1}
        elif event.key == pg.K_DOWN and self.allowed_dir[pg.K_DOWN]:
            self.direction = vec2(0, self.size)
            self.allowed_dir = {pg.K_UP: 0, pg.K_DOWN: 1, pg.K_LEFT: 1, pg.K_RIGHT: 1}

    def update(self):
        self.check_wall_collision()
        self.check_self_collision()
        self.check_food()
        self.move()

    def check_wall_collision(self):
        """Check for wall collision."""
        if self.rect.left < 0 or self.rect.right > self.w_size:
            self.game.game_active = False
            pg.mouse.set_visible(True)
        if self.rect.top < 0 or self.rect.bottom > self.w_size:
            self.game.game_active = False
            pg.mouse.set_visible(True)

    def check_self_collision(self):
        """Check for self collision."""
        if len(self.segments) != len(set(segment.center for segment in self.segments)):
            self.game.game_active = False
            pg.mouse.set_visible(True)

    def check_food(self):
        """Check if snake ate the food."""
        if self.rect.center == self.game.food.rect.center:
            self.game.food.rect.center = self.get_random_position()
            self.length += 1
    
    def move(self):
        """Move snake and store the segments of snake to a list of rect obj."""
        if self.delta_time():
            self.rect.move_ip(self.direction)
            self.segments.append(self.rect.copy())
            self.segments = self.segments[-self.length:]

    def draw(self):
        """Draw the list of snake segments to the screen."""
        [pg.draw.rect(self.screen, self.settings.snake_colour, segment) for segment in self.segments]

class Food:
    """A class to manage food characteristics throughout the game."""
    def __init__(self, ai_game):
        """Initialize food characteristics."""
        self.game = ai_game
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.size = self.settings.tile_size
        self.rect = pg.rect.Rect(0, 0, self.size - 2, self.size - 2)
        self.rect.center = ai_game.snake.get_random_position()
    
    def draw(self):
        """Draw the food to the screen."""
        pg.draw.rect(self.screen, self.settings.food_colour, self.rect)