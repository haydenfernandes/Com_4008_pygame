import pygame,sys

from player import Player

class Game:
    def __init__(self): # initialize game variables
    
        player_sprite = Player((300,500),screenwidth, 5) 
        self.player = pygame.sprite.GroupSingle(player_sprite)
    def run(self): 

        self.player.update()    
        player_sprite = Player((300,500)) 
        self.player = pygame.sprite.GroupSingle(player_sprite)

    #obstacle setup
    self.shape = obstacle.shape
    self.block_size = 6
    self.blocks = pygame.sprite.group
    self.obstacle_amout = 4
    self.obstacle_x_position = [num * (screen width / self.obstacle_amount)for num in range(self.obstacle_amount)]
    self.creat_multiple_obstacles(* self.obstacle_x_positions, x_start = screen_width / 15, y=start = 480, )

def create_obstacle(self, x_start y_start,offset_x):
    for row_index, row in enumerate(self.shape):
        for col_index.col in enumerate(row):
            if col == 'x':
                x = x_start + col_index * self.block_size + offset_x
                y = y_start + row_index * self.block_size 
                block = obstacle.block(self.block_size,(255,89,70),x,y)
                self.blocks.add(block)

    def create_multiple_obstacles(self,*offset,x_start,y_start):
        for offset_x in offset:
            self.create_obstacle(x_start, y_start,offset_x)
            
                
    
    
    

    def run(self): # main game loop

        
        self.player.update()    

        self.player.sprite.lasers.draw(screen)  # draw the player's lasers on the screen 
        self.player.draw(screen) # draw the player sprite on the screen
        self.blocks.draw(screen)




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
        game.run()  # draw sprites before flipping the display
        pygame.display.flip()  # update the display
        clock.tick(60)
