import pygame
import sys

pygame.init()

Width, Height = 900, 700
Toolbar_Height = 120
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Mouse Draw Window")

canvas = pygame.Surface((Width, Height - Toolbar_Height))
canvas.fill((255, 255, 255))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((240, 240, 245))
    screen.blit(canvas, (0, Toolbar_Height))

    pygame.display.flip()
    clock.tick(60) 