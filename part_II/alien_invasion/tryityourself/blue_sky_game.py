import sys
import pygame

from player import Player


class BlueSkyGame:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Blue Game Sky")
        # self.screen.fill(color=(0, 0, 220))
        self.player = Player(self)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(color=(0, 0, 220))
            self.player.blitme()
            pygame.display.flip()


if __name__ == "__main__":
    bsg = BlueSkyGame()
    bsg.run_game()
