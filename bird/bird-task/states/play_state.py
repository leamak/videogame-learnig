"""
This file contains the implementation of the class StatePlay.

Author: Alejandro Mujica (aledrums@gmail.com)
Date: 07/12/2020
"""
import random
import pygame
import settings

from bird import Bird
from pipe_pair import PipePair

from states.base_state import BaseState
from render import render_text


class PlayState(BaseState):
    def enter(self):
        self.score = 0
        self.bird = Bird()

        self.pipes = []

        self.pipes_timer = 0
        self.pipes_time = 2.0  # Generate a pipe each two seconds

        self.last_pipe_y = random.randint(100, settings.VIRTUAL_HEIGHT - 20)

    def update(self, dt):
        if settings.paused == False:
            self.pipes_timer += dt 
            if self.pipes_timer >= self.pipes_time:
                pipe_y = min(
                    settings.VIRTUAL_HEIGHT - 20,
                    max(self.last_pipe_y + random.randint(-20, 20), 100)
                )
                self.last_pipe_y = pipe_y
                self.pipes.append(
                    PipePair(settings.VIRTUAL_WIDTH, pipe_y)
                )
                self.pipes_timer %= self.pipes_time
                self.pipes_time = random.uniform(1, 2)

            self.bird.update(dt)

            if (self.bird.get_collision_rect().bottom >
                    settings.VIRTUAL_HEIGHT - settings.GROUND_HEIGHT):
                settings.GAME_SOUNDS['death'].play()
                self.state_machine.change('score', score=self.score)

            for pipe in self.pipes:
                pipe.update(dt)
                if pipe.collides(self.bird):
                    settings.GAME_SOUNDS['death'].play()
                    self.state_machine.change('score', score=self.score)
                if self.bird.x > pipe.x + settings.PIPE_WIDTH and not pipe.scored:
                    settings.GAME_SOUNDS['score'].play()
                    pipe.scored = True
                    self.score += 1

            self.pipes = [pipe for pipe in self.pipes if not pipe.remove]

        if settings.key_pressed.get(pygame.K_p):
            settings.GAME_SOUNDS['paused'].play()
            settings.paused = not settings.paused
            if settings.paused == True:
                pygame.mixer_music.pause()
            else:
                pygame.mixer_music.unpause()


    def render(self, surface):
        for pipe in self.pipes:
            pipe.render(surface)

        self.bird.render(surface)
        render_text(surface, f'Score: {self.score}', 'large', 5, 5)
