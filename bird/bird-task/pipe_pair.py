"""
This file contains the implememtation of the class Pipe.

Author: Alejandro Mujica (aledrums@gmail.com)
Date: 07/11/2020
"""
import pygame

import settings

from pipe import Pipe


class PipePair:
    def __init__(self, x, y):
        self.x = x
        self.lower_pipe = Pipe(x, y, 'lower')
        self.upper_pipe = Pipe(
            x, y - settings.PIPE_HEIGHT - settings.PIPE_GAP, 'upper'
        )
        self.remove = False
        self.scored = False
    
    def collides(self, bird):
        return (
            bird.collides(self.lower_pipe) or bird.collides(self.upper_pipe)
        )
    def update(self, dt):
        if self.x < -settings.PIPE_WIDTH:
            self.remove = True
        else:
            self.x += -settings.PIPE_SPEED * dt
            self.lower_pipe.x = self.x
            self.upper_pipe.x = self.x
    
    def render(self, surface):
        self.lower_pipe.render(surface)
        self.upper_pipe.render(surface)
