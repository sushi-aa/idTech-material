'''
import pygame

pygame.init()
wind = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Pygame Thing!")

x = 50
y = 50
width = 40
height = 60
vel = 5

run = True # boolean has values of either t or f
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel

    wind.fill((0, 0, 0))
    pygame.draw.rect(wind, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()

'''
import pygame

size = (50, 50)

run = True # boolean has values of either t or f
while run:
    pygame.time.delay(100)
    rect_border = pygame.Surface(size)
    pygame.draw.rect(rect_border, (0, 0, 255), rect_border.get_rect(), 10)
