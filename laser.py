import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self, pos, speed):
        super().__init__()
        self.image = pygame.Surface((4, 20))
        self.image.fill((0, 255, 0))  # green laser
        self.rect = self.image.get_rect(midbottom=pos)
        self.speed = speed
