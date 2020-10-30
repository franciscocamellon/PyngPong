# -*- coding: utf-8 -*-

import pygame


class Movements():
    """ Docstring """

    def __init__(self):
        """ Constructor """

    def ball_movement(self, ball, x_pos, y_pos):
        """ Docstring """
        ball.x += x_pos
        ball.y += y_pos
        return ball
