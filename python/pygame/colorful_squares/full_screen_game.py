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

FRAMES          = 3
BORDER          = 5
RECT_SIZE       = 50


def main():
    pygame.init()
    resolution = pygame.display.get_desktop_sizes()[0]
    flags = pygame.FULLSCREEN
    screen = pygame.display.set_mode(resolution, flags)
    pygame.display.set_caption("awesome game")
    clock = pygame.time.Clock()

    all_colors = list(pygame.colordict.THECOLORS.values())

    # calculate number of squares that fit on screen including borders
    num_columns = (resolution[0] - BORDER) // (RECT_SIZE + BORDER)
    num_rows = (resolution[1] - BORDER) // (RECT_SIZE + BORDER)
    # adjust remaining space to left and upper border
    left_border = (resolution[0] - num_columns * (RECT_SIZE + BORDER)) // 2
    upper_border = (resolution[1] - num_rows * (RECT_SIZE + BORDER)) // 2

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE or event.key == K_q:
                    running = False
            elif event.type == QUIT:
                running = False

        screen.fill(pygame.Color("white"))
        cur_x = left_border
        increment = BORDER + RECT_SIZE
        for column in range(num_columns):
            cur_y = upper_border
            for row in range(num_rows):
                random_color = all_colors[randint(0, len(all_colors)-1)]
                pygame.draw.rect(screen, random_color, (cur_x, cur_y, RECT_SIZE, RECT_SIZE))
                cur_y = cur_y + RECT_SIZE + BORDER
            cur_x = cur_x + RECT_SIZE + BORDER

        pygame.display.flip()
        clock.tick(FRAMES)


if __name__ == "__main__":
    main()
