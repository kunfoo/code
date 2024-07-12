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

SCALING_FACTOR  = 10
FRAMES          = 2

ALIVE           = 0x00ff00
DEAD            = 0xff0000

def calc_num_neighbors(grid, x, y):
    num_neighbors = 0
    x_max = grid.shape[0]-1
    y_max = grid.shape[1]-1

    if x > 0 and grid[x-1, y] == ALIVE:
        num_neighbors += 1
    if x < x_max and grid[x+1, y] == ALIVE:
        num_neighbors += 1
    if x > 0 and y > 0 and grid[x-1, y-1] == ALIVE:
        num_neighbors += 1
    if x > 0 and y < y_max and grid[x-1, y+1] == ALIVE:
        num_neighbors += 1
    if x < x_max and y > 0 and grid[x+1, y-1] == ALIVE:
        num_neighbors += 1
    if x < x_max and y < y_max and grid[x+1, y+1] == ALIVE:
        num_neighbors += 1
    if y > 0 and grid[x, y-1] == ALIVE:
        num_neighbors += 1
    if y < y_max and grid[x, y+1] == ALIVE:
        num_neighbors += 1

    return num_neighbors


def next_generation(grid):
    x_max = grid.shape[0]
    y_max = grid.shape[1]
    new_grid_surface = grid.surface.copy()
    new_grid = pygame.PixelArray(new_grid_surface)
    for x in range(x_max):
        for y in range(y_max):
            num_neighbors = calc_num_neighbors(grid, x, y)
            if grid[x, y] == ALIVE:
                if num_neighbors < 2 or num_neighbors > 3:
                    # new_grid[x, y] = DEAD
                    new_grid[x, y] = 0xffffff
            elif num_neighbors == 3:
                new_grid[x, y] = ALIVE

    return new_grid_surface, new_grid


def main():
    pygame.init()
    pygame.display.set_caption("game of life")
    clock = pygame.time.Clock()

    resolution = pygame.display.get_desktop_sizes()[0]
    flags = pygame.FULLSCREEN
    screen = pygame.display.set_mode(resolution, flags)
    screen.fill(pygame.Color("white"))
    grid_width = resolution[0]//SCALING_FACTOR
    grid_height = resolution[1]//SCALING_FACTOR
    grid_surface = pygame.Surface((grid_width, grid_height))
    grid_surface.fill(pygame.Color("white"))
    grid = pygame.PixelArray(grid_surface)

    num_init_cells = randint(10, grid_width*grid_height)
    for cell in range(num_init_cells):
        x = randint(0, grid_width-1)
        y = randint(0, grid_height-1)
        grid[x, y] = ALIVE
    pygame.transform.scale(grid_surface, resolution, screen)
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE or event.key == K_q:
                    running = False
            elif event.type == QUIT:
                running = False

        grid_surface, grid = next_generation(grid)
        pygame.transform.scale(grid_surface, resolution, screen)
        pygame.display.flip()
        clock.tick(FRAMES)

if __name__ == "__main__":
    main()
