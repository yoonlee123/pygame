import pygame.font

class Button:
    """A class to create buttons for Snake Game."""
    def __init__(self, ai_game, msg):
        """Initialize attributes of the button."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        # Set the dimensions and properties of the button.
        self.width, self.height = 250, 100
        self.button_colour = (0, 135, 0)
        self.text_colour = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 68)
        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        # The button message needs to be prepped only once.
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(
            msg,
            True,
            self.text_colour,
            self.button_colour
        )
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw(self):
        """Draw blank button and then draw message."""
        self.screen.fill(self.button_colour, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

# class GameOver:
#     """A class to create Game Over message for Snake Game."""
#     def __init__(self, ai_game):
#         """Initialize attributes of the message."""
#         self.screen = ai_game.screen
#         self.screen_rect = self.screen.get_rect()
#         # Build the message rect object and set its location.
#         self.text_colour = (50, 50, 50)
#         text = self.font.render('Game Over!', True, self.text_colour)
#         text_rect = text.get_rect(center=(200, 100))
#         self.v_offset = -300
#         self.text_rect.centery += self.v_offset

#     def draw(self):
#         """Draw blank message and then draw message."""
#         self.screen.blit(self.text, self.text_rect)
