import pygame, sys
from player import Player
from invaders import InvaderGroup
from pathlib import Path
from obstacle import Block,shape

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



        self.blocks = pygame.sprite.Group()
        self.create_shield(50,400)
        self.create_shield(200,400)
        self.create_shield(350,400)
        self.create_shield(500,400)


        #health, score

        self.lives = 3
        img_path = Path(__file__).resolve().parent / "defender.png"
        self.live_surf = pygame.image.load(str(img_path)).convert_alpha()
        self.live_surf = pygame.transform.scale(self.live_surf, (30, 30))
        self.live_x_start_pos = screenwidth - (self.lives * (self.live_surf.get_size()[0] + 10))
        
        self.score = 0
        self.score_font = pygame.font.SysFont(None, 36)

    
        self.game_over=False
        self.font = pygame.font.SysFont(None, 64)
        self.small_font = pygame.font.SysFont(None, 32)

    def create_shield(self, x_start, y_start):

        block_size = 10
        block_color = (0, 255, 0)


        for row_index, row in enumerate(shape):
            for col_index, col in enumerate(row):
                if col == 'x':
                    x = x_start + col_index * 5
                    y = y_start + row_index * 5
                    block = Block(5, (0, 255, 0), x, y)
                    self.blocks.add(block)


    def display_lives(self, surface):
        for live in range(self.lives):
            x = self.live_x_start_pos + (live * (self.live_surf.get_size()[0] + 10))
            y = 8
            surface.blit(self.live_surf, (x, y))

    def display_score(self, screen):
        score_surf = self.score_font.render(f"Score: {self.score}", True, (255, 255, 255))
        score_rect = score_surf.get_rect(topleft=(10, 10))
        screen.blit(score_surf, score_rect)

            


    def run(self, screen):
        # update
        self.player.update()
        player_hit = self.invaders.update(self.player.sprite)

        if player_hit and not self.game_over:
            self.lives -= 1
            

        if self.lives < 0:
            self.game_over = True
  # pass player to check hits

        self.collision_check()

        # draw
        self.invaders.draw(screen)
        self.player.draw(screen)
        self.player.sprite.lasers.draw(screen)
        self.blocks.draw(screen)
        
        pygame.sprite.groupcollide(
            self.player.sprite.lasers,  
            self.blocks,                
            True,                       
            True   
        )
        
        for bullet in self.invaders.enemy_bullets[:]:
            for block in self.blocks.sprites():
                if bullet.colliderect(block.rect):
                    self.invaders.enemy_bullets.remove(bullet)
                    block.kill()
                    break

                     




        self.display_lives(screen)
        self.display_score(screen)

        if self.game_over:
            self.game_over_screen(screen)
    

    def collision_check(self):
        for laser in self.player.sprite.lasers:
            collided_invaders = pygame.sprite.spritecollide(
                laser,
                self.invaders,
                dokill=True
            )
            if collided_invaders:
                laser.kill()
                self.score += 100



    def game_over_screen(self, screen):
        game_over_text = self.font.render("GAME OVER", True, (255, 0, 0))
        restart_text = self.small_font.render("Press R to Restart", True, (255, 255, 255))
        quit_text = self.small_font.render("Press ESC to Quit", True, (255, 255, 255))

        game_over_rect = game_over_text.get_rect(center=(self.screenwidth // 2, self.screenheight // 2 - 30))
        restart_rect = restart_text.get_rect(center=(self.screenwidth // 2, self.screenheight // 2 + 20))
        quit_rect = quit_text.get_rect(center=(self.screenwidth // 2, self.screenheight // 2 + 60))

        screen.blit(game_over_text, game_over_rect)
        screen.blit(restart_text, restart_rect)
        screen.blit(quit_text, quit_rect)
                    


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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_r and game.game_over:
                    game = Game(screenwidth, screenheight)

                    


        screen.fill((0, 0, 0))  # fill the screen with black
        # pass screen to run()
        game.run(screen)        # draw sprites before flipping the display
        pygame.display.flip()   # update the display
        clock.tick(60)          # limit to 60 FPS
