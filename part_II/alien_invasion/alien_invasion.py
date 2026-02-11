import sys

import pygame  # pylint: disable=no-member


class AlienInvasion:
    """Overall class to manage assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("alien Invasion")

    def run_game(self):
        while True:
            # Watch for keyboard and mouse event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # make the most recently drawn screen visible
            pygame.display.flip()


if __name__ == "__main__":

    # Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
