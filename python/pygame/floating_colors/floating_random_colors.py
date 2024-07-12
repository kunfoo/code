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


def main():
    pygame.init()
    pygame.display.set_caption("floating colors")
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    all_colors = list(pygame.colordict.THECOLORS.values())
    num_columns = SCREEN_WIDTH // SCALING_FACTOR
    num_rows = SCREEN_HEIGHT // SCALING_FACTOR
    grid_surface = pygame.Surface((num_columns, num_rows))
    grid = pygame.PixelArray(grid_surface)

    color_map = [ 0xffffff for _ in range(num_columns) ]
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE or event.key == K_q:
                    running = False
            elif event.type == QUIT:
                running = False

        next_color = choice(all_colors)
        color_map = color_map[1:num_columns] + [next_color]

        for x in range(num_columns):
            for y in range(num_rows):
                grid[x, y] = color_map[x]

        pygame.transform.scale(grid_surface, (SCREEN_WIDTH, SCREEN_HEIGHT), screen)
        pygame.display.flip()
        clock.tick(FRAMES)


if __name__ == "__main__":
    main()
