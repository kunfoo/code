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
from random import choice

SCREEN_WIDTH    = 1600
SCREEN_HEIGHT   = 1200
FRAMES          = 60
SCALING_FACTOR  = 20

all_colors = list(pygame.colordict.THECOLORS.values())
num_colors = len(all_colors)
num_columns = SCREEN_WIDTH // SCALING_FACTOR
num_rows = SCREEN_HEIGHT // SCALING_FACTOR


def get_colors(c):
    other_side = []
    slice_begin = c - num_columns
    if slice_begin < 0:
        other_side = all_colors[slice_begin:]
        slice_begin = 0

    return other_side + all_colors[slice_begin:c]


def main():
    pygame.init()
    pygame.display.set_caption("floating colors")
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    grid_surface = pygame.Surface((num_columns, num_rows))
    grid = pygame.PixelArray(grid_surface)

    c = num_colors-1
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE or event.key == K_q:
                    running = False
            elif event.type == QUIT:
                running = False

        colors = get_colors(c)
        if c > 0:
            c -= 1
        else:
            c = num_colors-1

        for x in range(num_columns):
            for y in range(num_rows):
                grid[x, y] = colors[x]

        pygame.transform.scale(grid_surface, (SCREEN_WIDTH, SCREEN_HEIGHT), screen)
        pygame.display.flip()
        clock.tick(FRAMES)


if __name__ == "__main__":
    main()
