import pygame
import sys

pygame.init()

Width, Height = 900, 700
Toolbar_Height = 120
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Mouse Draw Window")

canvas = pygame.Surface((Width, Height - Toolbar_Height))
canvas.fill((255, 255, 255))

Colors = {
    "red": (230, 57, 70),
    "orange": (247, 127, 0),
    "yellow": (252, 191, 73),
    "green": (42, 157, 143),
    "blue": (0, 150, 199),
    "purple": (157, 78, 221),
    "black": (20, 20, 20),
    "white": (255, 255, 255) # Used as eraser
}

drawing = False
last_pos = None
current_color = (0, 180, 216)
brush_size = 5



clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            #check if click is on canvas area
            if event.pos[1] >= Toolbar_Height:
                drawing = True
                canvas_pos = (event.pos[0], event.pos[1] - Toolbar_Height)
                last_pos = canvas_pos

        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            last_pos = None

        elif event.type == pygame.MOUSEMOTION and drawing:
            if event.pos[1] >= Toolbar_Height:
                canvas_pos = (event.pos[0], event.pos[1] - Toolbar_Height)
                if last_pos:
                    # have smooth lines between mouse movements
                    pygame.draw.line(canvas, current_color, last_pos, canvas_pos,
                brush_size, last_pos = canvas_pos)

    screen.fill((240, 240, 245))
    screen.blit(canvas, (0, Toolbar_Height))

    pygame.display.flip()
    clock.tick(60) 