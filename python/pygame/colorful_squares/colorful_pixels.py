#!/usr/bin/env python3
import pygame
from pygame.gfxdraw import pixel
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


def main():
    pygame.init()
    # resolution = pygame.display.get_desktop_sizes()[0]
    # flags = pygame.FULLSCREEN
    # screen = pygame.display.set_mode(resolution, flags)
    resolution = (640, 480)
    screen = pygame.display.set_mode(resolution)
    pygame.display.set_caption("colorful pixels")
    clock = pygame.time.Clock()

    all_colors = list(pygame.colordict.THECOLORS.values())
    num_colors = len(all_colors) - 1

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE or event.key == K_q:
                    running = False
            elif event.type == QUIT:
                running = False

        for x in range(resolution[0]):
            for y in range(resolution[1]):
                random_color = all_colors[randint(0, num_colors)]
                pixel(screen, x, y, random_color)

        pygame.display.flip()
        # clock.tick(FRAMES)


if __name__ == "__main__":
    main()
