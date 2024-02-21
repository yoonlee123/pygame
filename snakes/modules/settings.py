class Settings():
    """Define the settings of the game here."""
    def __init__(self):
        """Initialize the settings of the game."""
        # Screen settings.
        self.window_size = 1000
        self.tile_size = 50
        self.tile_colour = (50, 50, 50)
        self.snake_colour = (0, 255, 0)
        self.food_colour = (255, 0, 0)
        self.step_delay = 150 # in ms, e.g. 100 means 10fps or 10Hz


