import pygame,sys

class Game:
    def __init__(self): # initialize game variables
        pass

    def run(self): # main game loop
        pass

if __name__ == "__main__":
    pygame.init()
    screenwidth, screenheight = 600, 600 # set the screen size
    screen = pygame.display.set_mode((screenwidth, screenheight))
    pygame.display.set_caption("space invaders")
    clock = pygame.time.Clock()
    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0)) # fill the screen with black
        pygame.display.flip()  # update the display
        clock.tick(60)
        game.run()