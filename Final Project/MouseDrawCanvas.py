import pygame
import sys

pygame.init()

Width, Height = 900, 700
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Mouse Draw Window")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((240, 240, 245))
    pygame.display.flip()
    clock.tick(60) 