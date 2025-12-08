import pygame, sys
from player import Player
from invaders import InvaderGroup


class Game:
    def __init__(self, screenwidth, screenheight):
        self.screenwidth = screenwidth
        self.screenheight = screenheight

        player_sprite = Player(
            (screenwidth // 2, screenheight - 80),
            screenwidth,
            5,
            screen_height=screenheight
        )
        self.player = pygame.sprite.GroupSingle(player_sprite)

        self.invaders = InvaderGroup(screenwidth, screenheight)

    def run(self, screen):
        # update
        self.player.update()
        self.invaders.update(self.player.sprite)  # pass player to check hits

        # draw
        self.invaders.draw(screen)
        self.player.draw(screen)
        self.player.sprite.lasers.draw(screen)


if __name__ == "__main__":
    pygame.init()
    screenwidth, screenheight = 600, 600  # set the screen size
    screen = pygame.display.set_mode((screenwidth, screenheight))
    pygame.display.set_caption("space invaders")
    clock = pygame.time.Clock()

    #pass screenwidth & screenheight
    game = Game(screenwidth, screenheight)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))  # fill the screen with black
        # pass screen to run()
        game.run(screen)        # draw sprites before flipping the display
        pygame.display.flip()   # update the display
        clock.tick(60)          # limit to 60 FPS
