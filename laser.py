import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self, pos, speed,screenheight):
        super().__init__()
        self.image = pygame.Surface((4, 20))
        self.image.fill((0, 255, 0))  # green laser
        self.rect = self.image.get_rect(midbottom=pos)
        self.speed = speed
        self.screenheight_y_constraint = screenheight

    def destroy(self):
        if self.rect.y <= -50 or self.rect.y >= self.screenheight_y_constraint + 50:
            self.kill()

    def update(self):
        self.rect.y -= self.speed
        self.destroy()
