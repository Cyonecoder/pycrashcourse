import sys
from ship import Ship
from settings import Settings
import pygame  # pylint: disable=no-member


class AlienInvasion:
    """Overall class to manage assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("alien Invasion")
        self.bg_color = self.settings.bg_color
        self.ship = Ship(self)

    def run_game(self):
        while True:
            # Watch for keyboard and mouse event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # make the most recently drawn screen visible
            self.screen.fill(self.bg_color)
            self.ship.blitme()
            pygame.display.flip()


if __name__ == "__main__":

    # Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
