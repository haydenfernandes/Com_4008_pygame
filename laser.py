import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self, pos, speed=7):
        super().__init__()
        self.image = pygame.Surface((4, 20))
        self.image.fill((0, 255, 0))  # green laser
        self.rect = self.image.get_rect(midbottom=pos)
        self.speed = speed

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()
