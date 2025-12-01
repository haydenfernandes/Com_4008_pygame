import pygame, sys
import random
pygame.init()
screenwidth, screenheight = 600, 600
screen = pygame.display.set_mode((screenwidth, screenheight))
pygame.display.set_caption("space invaders")
clock = pygame.time.Clock()

# player
player_img = pygame.image.load(r"c:\Users\Lewtunes\Downloads\space invaders\images\defender.png")
player_img = pygame.transform.scale(player_img, (35, 30))
player_x = (screenwidth - player_img.get_width()) // 2
player_y = screenheight - player_img.get_height() - 10

# load invader images
invader_paths = [
    r"c:\Users\Lewtunes\Downloads\space invaders\images\invader1.png",
    r"c:\Users\Lewtunes\Downloads\space invaders\images\invader2.png",
    r"c:\Users\Lewtunes\Downloads\space invaders\images\invader3.png",
]
invader_imgs = [pygame.transform.scale(pygame.image.load(p), (25, 25)) for p in invader_paths]

# formation
cols = 11
rows = 5
spacing_x = 40
spacing_y = 35
total_width = (cols - 1) * spacing_x
start_x = (screenwidth - total_width) // 2
start_y = 60

invaders = []
for r in range(rows):
    for c in range(cols):
        img = invader_imgs[r % len(invader_imgs)]  
        rect = img.get_rect(topleft=(start_x + c * spacing_x, start_y + r * spacing_y))
        invaders.append({"img": img, "rect": rect, "alive": True})

# formation movement
invader_dir = 1        
invader_speed = 1
descend_amount = 10
edge_margin = 8

# enemy bullets
bullet_path = r"c:\Users\Lewtunes\Downloads\space invaders\images\bullet.png"
enemy_bullet_img = pygame.image.load(bullet_path)
enemy_bullet_img = pygame.transform.scale(enemy_bullet_img, (5, 15))
enemy_bullets = []
enemy_fire_cooldown = 500   # ms between enemy shots
last_enemy_fire = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        

    # move formation horizontally
    for inv in invaders:
        if inv["alive"]:
            inv["rect"].x += invader_dir * invader_speed

    # check edges and descend+reverse when necessary
    alive_rects = [inv["rect"] for inv in invaders if inv["alive"]]
    if alive_rects:
        leftmost = min(r.left for r in alive_rects)
        rightmost = max(r.right for r in alive_rects)
        if rightmost >= screenwidth - edge_margin and invader_dir > 0:
            invader_dir = -1
            for inv in invaders:
                inv["rect"].y += descend_amount
        elif leftmost <= edge_margin and invader_dir < 0:
            invader_dir = 1
            for inv in invaders:
                inv["rect"].y += descend_amount

    screen.fill((0, 0, 0))
    screen.blit(player_img, (player_x, player_y))

    # draw invaders
    for inv in invaders:
        if inv["alive"]:
            screen.blit(inv["img"], inv["rect"].topleft)

    # enemy firing 
    now = pygame.time.get_ticks()
    if now - last_enemy_fire >= enemy_fire_cooldown:
        shooters = [inv for inv in invaders if inv["alive"]]
        if shooters:
            shooter = random.choice(shooters)
            bullet_rect = enemy_bullet_img.get_rect(midtop=shooter["rect"].midbottom)
            enemy_bullets.append(bullet_rect)
            last_enemy_fire = now

    # update and draw enemy bullets
    for bullet in enemy_bullets[:]:
        bullet.y += 5  # bullet speed
        screen.blit(enemy_bullet_img, bullet.topleft)
        if bullet.colliderect(pygame.Rect(player_x, player_y, player_img.get_width(), player_img.get_height())):
            print("Player hit!")
            enemy_bullets.remove(bullet)
        elif bullet.top > screenheight:
            enemy_bullets.remove(bullet)

    

    pygame.display.flip()
    clock.tick(60)

















