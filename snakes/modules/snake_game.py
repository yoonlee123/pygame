import pygame as pg
import sys

from settings import Settings
from game_objects import Snake, Food
from interactive import Button#, GameOver

class SnakeGame:
    """Highest level class to manage operation of the game."""
    def __init__(self):
        """Initialize the game, and create game resources."""
        pg.init()
        self.settings = Settings()
        self.screen = pg.display.set_mode([self.settings.window_size] * 2)
        self.clock = pg.time.Clock()
        pg.display.set_caption("Snakes")
        # Create game objects.
        self.snake = Snake(self)
        self.food = Food(self)
        # Game is not activated.
        self.game_active = False
        # Make the play button.
        self.play_button = Button(self, 'Play')
        # self.game_over_text = GameOver(self)
        # self.game_over = False
    
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            if self.game_active:
                self.snake.update()

            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()
                self._check_play_button(mouse_pos)
    
    def _check_keydown_events(self, event):
        """Check for keydown events and update relevant attributes."""
        self.snake.control(event)
    
    def _check_play_button(self, mouse_pos):
        """Check for mouse click events and update relevant attributes."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self.initialize_settings()

    def initialize_settings(self):
        self.game_active = True
        pg.mouse.set_visible(False)
        self.snake = Snake(self)
        self.food = Food(self)

    def _draw_grid(self):
        """Drawing grid on the screen."""
        # Draw veritcal lines.
        for x in range(0, self.settings.window_size, self.settings.tile_size):
            pg.draw.line(self.screen,
                         self.settings.tile_colour,
                         (x, 0),
                         (x, self.settings.window_size)
            )
        # Draw horizontal lines.
        for y in range(0, self.settings.window_size, self.settings.tile_size):
            pg.draw.line(self.screen,
                         self.settings.tile_colour,
                         (0, y),
                         (self.settings.window_size, y)
            )
        
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill('black')
        self._draw_grid()
        if not self.game_active:
            self.play_button.draw()
        else:
            self.snake.draw()
            self.food.draw()
        # if self.game_over:
        #     self.game_over_text.draw()
        pg.display.flip()
        
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = SnakeGame()
    ai.run_game()