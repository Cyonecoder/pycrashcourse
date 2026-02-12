import pygame


class Player:

    def __init__(self, ai_scren):
        self.screen = ai_scren.screen
        self.screen_rect = ai_scren.screen.get_rect()
        self.player_image = pygame.image.load("../ship.bmp")
        self.player_image_rect = self.player_image.get_rect()
        self.player_image_rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.player_image, self.player_image_rect)
