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
SCALING_FACTOR  = 10
GRID_WIDTH      = SCREEN_WIDTH // SCALING_FACTOR
GRID_HEIGHT     = SCREEN_HEIGHT // SCALING_FACTOR
FRAMES          = 3

all_colors = list(pygame.colordict.THECOLORS.values())


def set_neighbors(grid, x, y, color):
    print(f"set_neighbors({x}, {y})")
    next_color = choice(all_colors)
    if x > 0:
        set_neighbors(grid, x-1, y, next_color)
    if x < grid_width-1:
        set_neighbors(grid, x+1, y, next_color)
    if y > 0:
        set_neighbors(grid, x, y-1, next_color)
    if y < grid_height-1:
        set_neighbors(grid, x, y+1, next_color)
    grid[x, y] = color


def traverse(point_distances, points):
    next_points = set()
    color = choice(all_colors)

    for x, y in points:
        point_distances[(x,y)] = color
        if x > 0 and (x-1, y) not in point_distances:
            next_points.add((x-1, y))
        if x < GRID_WIDTH-1 and (x+1, y) not in point_distances:
            next_points.add((x+1, y))
        if y > 0 and (x, y-1) not in point_distances:
            next_points.add((x, y-1))
        if y < GRID_HEIGHT-1 and (x, y+1) not in point_distances:
            next_points.add((x, y+1))

    if next_points:
        traverse(point_distances, next_points)


def traverse1(point_distances, point, distance):
    point_distances[point] = distance

    x, y = point
    if x > 0 and (x-1, y) not in point_distances:
        print(point, distance)
        traverse(point_distances, (x-1, y), distance+1)
    if x < GRID_WIDTH-1 and (x+1, y) not in point_distances:
        print(point, distance)
        traverse(point_distances, (x+1, y), distance+1)
    if y > 0 and (x, y-1) not in point_distances:
        print(point, distance)
        traverse(point_distances, (x, y-1), distance+1)
    if y < GRID_HEIGHT-1 and (x, y+1) not in point_distances:
        print(point, distance)
        traverse(point_distances, (x, y+1), distance+1)


def colorize(grid, point_distances):
    for x, y in point_distances:
        grid[x, y] = point_distances[(x,y)]


def colorize1(grid, point_distances):
    color_map = {}

    for x, y in point_distances:
        distance = point_distances[(x,y)]
        if distance not in color_map:
            color_map[distance] = choice(all_colors)
        grid[x, y] = color_map[distance]
    breakpoint()


def main():
    pygame.init()
    pygame.display.set_caption("diamonds")
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    grid_surface = pygame.Surface((GRID_WIDTH, GRID_HEIGHT))
    grid = pygame.PixelArray(grid_surface)

    x = GRID_WIDTH // 2
    y = GRID_HEIGHT // 2
    point_distances = {}
    traverse(point_distances, {(x, y)})
    colorize(grid, point_distances)

    pygame.transform.scale(grid_surface, (SCREEN_WIDTH, SCREEN_HEIGHT), screen)
    pygame.display.flip()
    clock.tick(FRAMES)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE or event.key == K_q:
                    running = False
            elif event.type == QUIT:
                running = False


if __name__ == "__main__":
    main()
