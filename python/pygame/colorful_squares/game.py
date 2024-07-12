#!/usr/bin/env python3
import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_q
)
from random import randint

# SCREEN_WIDTH    = 1600
# SCREEN_HEIGHT   = 1200
FRAMES          = 3
BORDER          = 5
RECT_SIZE       = 50
NUM_COLUMNS     = 30
NUM_ROWS        = 30

def main():
    pygame.init()
    screen_width = NUM_COLUMNS * (BORDER + RECT_SIZE) + BORDER
    screen_height = NUM_ROWS * (BORDER + RECT_SIZE) + BORDER
    screen = pygame.display.set_mode([screen_width, screen_height])
    pygame.display.set_caption("awesome game")
    clock = pygame.time.Clock()

    all_colors = list(pygame.colordict.THECOLORS.values())

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE or event.key == K_q:
                    running = False
            elif event.type == QUIT:
                running = False

        screen.fill(pygame.Color("white"))
        cur_x = BORDER
        increment = BORDER + RECT_SIZE
        for column in range(NUM_COLUMNS):
            cur_y = BORDER
            for row in range(NUM_ROWS):
                random_color = all_colors[randint(0, len(all_colors)-1)]
                pygame.draw.rect(screen, random_color, (cur_x, cur_y, RECT_SIZE, RECT_SIZE))
                cur_y = cur_y + RECT_SIZE + BORDER
            cur_x = cur_x + RECT_SIZE + BORDER

        pygame.display.flip()
        clock.tick(FRAMES)

if __name__ == "__main__":
    main()
