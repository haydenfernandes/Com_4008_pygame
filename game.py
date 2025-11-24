import pygame,sys

pygame.init()
screenwidth, screenheight = 600, 600 # set the screen size
screen = pygame.display.set_mode((screenwidth, screenheight))
pygame.display.set_caption("space invaders")
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0)) # fill the screen with black
    pygame.display.flip()  # update the display
    clock.tick(60)