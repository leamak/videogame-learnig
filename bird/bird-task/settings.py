"""Game settings

This file contains all game settings such window dimensions, resolution,
default objects values, textures, sounds, fonts, etc.

Author: Alejandro Mujica (aledrums@gmail.com)
Date: 07/11/2020
"""
import pygame

pygame.init()

# physical screen dimensions
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

# virtual resolution dimensions
VIRTUAL_WIDTH = 512
VIRTUAL_HEIGHT = 288

BACKGROUND_LOOP_POINT = 413
BACKGROUND_SPEED = 30
GROUND_SPEED = 60

PIPE_SPEED = 60
PIPE_WIDTH = 70
PIPE_HEIGHT = 288
PIPE_GAP = 80

GROUND_HEIGHT = 16

GRAVITY = 980

GAME_SOUNDS =  {
    'jump': pygame.mixer.Sound('sounds/jump.wav'),
    'score': pygame.mixer.Sound('sounds/score.wav'),
    'death': pygame.mixer.Sound('sounds/death.wav'),
    'count': pygame.mixer.Sound('sounds/count.wav'),
    'paused': pygame.mixer.Sound('sounds/pause.wav'),
}

GAME_FONTS = {
    'medium': pygame.font.Font('fonts/flappy.ttf', 14),
    'large': pygame.font.Font('fonts/flappy.ttf', 28),
    'huge': pygame.font.Font('fonts/flappy.ttf', 56),
}

GAME_TEXTURES = {
    'background': pygame.image.load('graphics/background.png'),
    'ground': pygame.image.load('graphics/ground.png'),
    'bird': pygame.image.load('graphics/bird.png'),
    'pipe': pygame.image.load('graphics/pipe.png'),
}

key_pressed = {}
paused = False