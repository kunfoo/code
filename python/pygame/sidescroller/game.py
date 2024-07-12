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

SCREEN_WIDTH    = 1600
SCREEN_HEIGHT   = 1200
FRAMES          = 60

PLAYER_WIDTH    = 50
PLAYER_HEIGHT   = 50
ENEMY_WIDTH     = 20
ENEMY_HEIGHT    = 20


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surface = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.surface.fill((0xff, 0, 0))
        self.rect = self.surface.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -20)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 20)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-20, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(20, 0)

        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surface = pygame.Surface((ENEMY_WIDTH, ENEMY_HEIGHT))
        self.surface.fill((0, 0xff, 0))
        self.rect = self.surface.get_rect(
                center = (
                    randint(SCREEN_WIDTH + ENEMY_WIDTH, SCREEN_WIDTH + ENEMY_WIDTH*5),
                    randint(0, SCREEN_HEIGHT)
                )
        )
        self.speed = randint(1, 5)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


def main():
    pygame.init()
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    pygame.display.set_caption("awesome game")
    clock = pygame.time.Clock()

    pygame.mixer.music.load("background_music.mp3")
    pygame.mixer.music.play(-1)

    ADD_ENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADD_ENEMY, 250)

    player = Player()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    enemies = pygame.sprite.Group()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE or event.key == K_q:
                    running = False
            elif event.type == QUIT:
                running = False
            elif event.type == ADD_ENEMY:
                new_enemy = Enemy()
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)

        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        enemies.update()
        # screen.blit(player.surface, (0, SCREEN_HEIGHT//2 - PLAYER_HEIGHT//2))
        screen.fill((0, 0, 0))
        for sprite in all_sprites:
            screen.blit(sprite.surface, sprite.rect)

        if pygame.sprite.spritecollideany(player, enemies):
            running = False
        # screen.blit(player.surface, player.rect)
        # screen.blit(enemy.surface, enemy.rect)
        pygame.display.flip()
        clock.tick(FRAMES)

    
    pygame.mixer.music.stop()
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
