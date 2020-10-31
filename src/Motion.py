# -*- coding: utf-8 -*-


class Movements():
    """ Docstring """

    def __init__(self):
        """ Constructor """

    def ball_movement(self, ball, x_dir, y_dir):
        """ Docstring """
        ball.x += x_dir
        ball.y += y_dir
        return ball

    def verify_collision(self, width, height, border, ball, x_dir, y_dir):
        """ Docstring """
        if ball.top == border or ball.bottom == (height - border):
            y_dir *= -1
        if ball.left == border or ball.right == (width - border):
            x_dir *= -1
        return x_dir, y_dir


