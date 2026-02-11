import sys

import pygame  # pylint: disable=no-member


class AlienInvasion:
    """Overall class to manage assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("alien Invasion")
