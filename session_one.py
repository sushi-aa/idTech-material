import pygame, sys

pygame.init()

orange = (255,100,10)

#Variables for window and tiles
#clock = pygame.time.Clock()
#FPS = 60
WIDTH = 640
HEIGHT = 480
TILE_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")

# Game States
RESTART = -1
PLAYING = 0
GAME_OVER = 1
game_state = PLAYING

# Game Loop
while True:

   while game_state == PLAYING:

       for event in pygame.event.get():

           if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()

       screen.fill((0,0,0))
       pygame.draw.rect(screen, orange, (WIDTH/2, HEIGHT/2, TILE_SIZE,TILE_SIZE))
       pygame.display.update()