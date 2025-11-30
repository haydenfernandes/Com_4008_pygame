import pygame
from pathlib import Path


class Player(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        # load image relative to this file so the project can be moved
        img_path = Path(__file__).resolve().parent / "defender.png"
        try:
            self.image = pygame.image.load(str(img_path)).convert_alpha()
        except Exception as e:
            print(f"Warning: failed to load image {img_path}: {e}")
            # fallback visible placeholder so the player is always visible
            self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
            self.image.fill((255, 0, 255))

        self.rect = self.image.get_rect(center=pos)

        self.speed = 5

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        elif keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

    def update(self):
        self.get_input()
        
       