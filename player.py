import pygame
from pathlib import Path
from laser import Laser


class Player(pygame.sprite.Sprite):

    def __init__(self, pos,constraint, speed):
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

        self.speed = speed
        self.max_x_constraint = constraint
        self.ready = True
        self.laser_time = 0
        self.laser_cooldown = 600

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        elif keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        
        if keys[pygame.K_SPACE] and self.ready:
            self.shoot_laser()
            self.ready = False
            self.laser_time = pygame.time.get_ticks()

    def recharge(self):
        if not self.ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_time >= self.laser_cooldown:
                self.ready = True
        
    
    def constrain(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.max_x_constraint:
            self.rect.right = self.max_x_constraint

    def shoot_laser(self):
        print('pew')

    def update(self):
        self.get_input()
        self.constrain()
        self.recharge()
        
       