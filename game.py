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

        #health, score

        self.lives = 3
        self.live_surf = pygame.image.load("C:\\Users\\gomes\\OneDrive\\Desktop\\Com_4008_pygame\\defender.png").convert_alpha()
        self.live_surf = pygame.transform.scale(self.live_surf, (30, 30))
        self.live_x_start_pos = screenwidth - (self.lives * (self.live_surf.get_size()[0] + 10))
    
    


    def display_lives(self, surface):
        for live in range(self.lives):
            x = self.live_x_start_pos + (live * (self.live_surf.get_size()[0] + 10))
            y = 8
            surface.blit(self.live_surf, (x, y))
            


    def run(self, screen):
        # update
        self.player.update()
        player_hit = self.invaders.update(self.player.sprite)

        if player_hit:
            self.lives -= 1
            print("Lives left:", self.lives)

        if self.lives < 0:
            print("GAME OVER")
            pygame.quit()
            sys.exit()
  # pass player to check hits

        self.collision_check()

        # draw
        self.invaders.draw(screen)
        self.player.draw(screen)
        self.player.sprite.lasers.draw(screen)
        self.display_lives(screen)

    def collision_check(self):
        for laser in self.player.sprite.lasers:
            collided_invaders = pygame.sprite.spritecollide(
                laser,
                self.invaders,
                dokill=True
            )
            if collided_invaders:
                laser.kill()
                


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
