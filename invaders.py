import pygame
import random
from pathlib import Path


class Invader(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)


class InvaderGroup(pygame.sprite.Group):
    def __init__(self, screenwidth, screenheight):
        super().__init__()

        self.screenwidth = screenwidth
        self.screenheight = screenheight

        # --- load invader images ---
        root = Path(__file__).resolve().parent
        img_dir = root / "invader_images"

        self.invader_imgs = []
        for name in ("invader1.png", "invader2.png", "invader3.png"):
            p = img_dir / name
            try:
                img = pygame.image.load(str(p)).convert_alpha()
                img = pygame.transform.scale(img, (25, 25))
            except Exception as e:
                print(f"Warning: failed to load invader image {p}: {e}")
                img = pygame.Surface((25, 25), pygame.SRCALPHA)
                img.fill((200, 50, 50))
            self.invader_imgs.append(img)

        # --- create formation ---
        cols = 11
        rows = 5
        spacing_x = 40
        spacing_y = 35
        total_width = (cols - 1) * spacing_x
        start_x = (screenwidth - total_width) // 2
        start_y = 60

        for r in range(rows):
            for c in range(cols):
                img = self.invader_imgs[r % len(self.invader_imgs)]
                x = start_x + c * spacing_x
                y = start_y + r * spacing_y
                self.add(Invader(img, (x, y)))

        # --- formation movement ---
        self.direction = 1       # 1 = right, -1 = left
        self.speed = 1
        self.descend_amount = 10
        self.edge_margin = 8

        # --- enemy bullets ---
        bullet_path = img_dir / "bullet.png"
        try:
            self.enemy_bullet_img = pygame.image.load(str(bullet_path)).convert_alpha()
            self.enemy_bullet_img = pygame.transform.scale(self.enemy_bullet_img, (5, 15))
        except Exception as e:
            print(f"Warning: failed to load bullet image {bullet_path}: {e}")
            self.enemy_bullet_img = pygame.Surface((5, 15), pygame.SRCALPHA)
            self.enemy_bullet_img.fill((255, 255, 0))

        self.enemy_bullets = []
        self.enemy_fire_cooldown = 500  # ms between shots
        self.last_enemy_fire = 0

    def update(self, *args):
        """
        Optionally pass the player sprite as the first arg:
        invaders.update(player.sprite)
        """
        player_sprite = args[0] if args else None

        # --- move formation horizontally ---
        for inv in self.sprites():
            inv.rect.x += self.direction * self.speed

        # --- check edges, descend + reverse when needed ---
        if self.sprites():
            leftmost = min(inv.rect.left for inv in self.sprites())
            rightmost = max(inv.rect.right for inv in self.sprites())

            if rightmost >= self.screenwidth - self.edge_margin and self.direction > 0:
                self.direction = -1
                for inv in self.sprites():
                    inv.rect.y += self.descend_amount
            elif leftmost <= self.edge_margin and self.direction < 0:
                self.direction = 1
                for inv in self.sprites():
                    inv.rect.y += self.descend_amount

        # --- enemy firing ---
        now = pygame.time.get_ticks()
        if now - self.last_enemy_fire >= self.enemy_fire_cooldown and len(self.sprites()) > 0:
            shooter = random.choice(self.sprites())
            bullet_rect = self.enemy_bullet_img.get_rect(
                midtop=shooter.rect.midbottom
            )
            self.enemy_bullets.append(bullet_rect)
            self.last_enemy_fire = now

        # --- update bullets & check collision with player ---
        player_rect = player_sprite.rect if player_sprite is not None else None

        for bullet in self.enemy_bullets[:]:
            bullet.y += 5  # bullet speed

            if player_rect and bullet.colliderect(player_rect):
                print("Player hit!")
                self.enemy_bullets.remove(bullet)
            elif bullet.top > self.screenheight:
                self.enemy_bullets.remove(bullet)

    def draw(self, surface):
        # draw invaders
        super().draw(surface)
        # draw bullets
        for bullet in self.enemy_bullets:
            surface.blit(self.enemy_bullet_img, bullet.topleft)
















