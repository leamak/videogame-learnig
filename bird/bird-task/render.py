"""
This file contains an utility function to render text.

Author: Alejandro Mujica (aledrums@gmail.com)
Date: 07/12/2020
"""
import settings


def render_text(surface, text, font, x, y, center=False):
    font_obj = settings.GAME_FONTS[font]
    text_obj = font_obj.render(text, True, (255, 255, 255))
    text_rect = text_obj.get_rect()
    if center:
        text_rect.center = (x, y)
    else:
        text_rect.x = x
        text_rect.y = y
    surface.blit(text_obj, text_rect)
