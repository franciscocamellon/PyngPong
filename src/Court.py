# -*- coding: utf-8 -*-

import pygame


class Tenis_Court():
    """ Docstring """

    def __init__(self):
        """ Constructor """

        self.SCREEN_WIDTH = 400
        self.SCREEN_HEIGHT = 300
        self.PLAYER_SIZE = 50
        self.BORDER_SIZE = 5
        self.BORDER_OFFSET = 20
        self.COURT_OFFSET = 50
        self.COLOR = (255, 255, 255)

    def create_court(self, screen):
        """ Docstring """
        line = pygame.draw.line(screen, self.COLOR,
                                (250, 50), (250, 350), width=self.BORDER_SIZE)
        rect = pygame.Rect(50, 50, self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        court = pygame.draw.rect(
            screen, self.COLOR, rect, width=self.BORDER_SIZE)
        return court, line

    def constants(self):
        return self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.PLAYER_SIZE, self.BORDER_SIZE, self.BORDER_OFFSET, self.COLOR


class Pong_Ball(Tenis_Court):
    """ Docstring """

    def __init__(self):
        """ Constructor """
        super().__init__()
        self.RADIUS = 5

    def create_ball(self, screen, rect):
        """ Docstring """
        # ball = pygame.draw.circle(
        #     screen, self.COLOR, center, self.RADIUS, width=0)
        pygame.draw.rect(screen, self.COLOR, rect)

    def ball_position(self):
        """ Docstring """
        x_pos = self.SCREEN_WIDTH//2 - self.BORDER_SIZE//2
        y_pos = self.SCREEN_HEIGHT//2 - self.BORDER_SIZE//2

        return x_pos, y_pos


class Pong_Player(Tenis_Court):
    """ Docstring """

    def __init__(self):
        """ Constructor """
        super().__init__()

    def create_player(self, screen, height, player):
        """ Docstring """

        if player.bottom > height - self.BORDER_SIZE:
            player.bottom = height - self.BORDER_SIZE
        elif player.top < self.BORDER_SIZE:
            player.top = self.BORDER_SIZE

        line = pygame.draw.rect(screen, self.COLOR, player)
        return line

    def player_position(self):
        """ Docstring """
        position = (self.SCREEN_HEIGHT - self.PLAYER_SIZE)//2
        return position

    def create_score(self, screen, text, score, font, position):
        """ Docstring """
        score_result = font.render('{0} = {1}'.format(text, score), True, self.COLOR)
        score_result_rect = score_result.get_rect()
        score_result_rect.topleft = (position)
        return screen.blit(score_result, score_result_rect)




class Movements(Tenis_Court):
    """ Docstring """

    def __init__(self):
        """ Constructor """
        super().__init__()

    def ball_movement(self, ball, x_dir, y_dir):
        """ Docstring """
        ball.x += x_dir
        ball.y += y_dir
        return ball

    def verify_collision(self, ball, x_dir, y_dir):
        """ Docstring """
        if ball.top == (self.COURT_OFFSET + self.BORDER_SIZE) or \
            ball.bottom == (self.SCREEN_HEIGHT - self.BORDER_SIZE + self.COURT_OFFSET):
            y_dir *= -1
        if ball.left == (self.COURT_OFFSET + self.BORDER_SIZE) or \
            ball.right == (self.SCREEN_WIDTH - self.BORDER_SIZE + self.COURT_OFFSET):
            x_dir *= -1
        return x_dir, y_dir

    def computer_movements(self, ball, x_dir, player):
        """ Docstring """
        if x_dir == 1:
            if player.centery < ball.centery:
                player.y += 1
            else:
                player.y -= 1
        return player

    def ball_collision(self, ball, player_one, player_two, x_dir):
        """ Docstring """
        if x_dir == -1 and player_one.right == ball.left and player_one.top < ball.top and player_one.bottom > ball.bottom:
            return -1
        elif x_dir == 1 and player_two.left == ball.right and player_two.top < ball.top and player_two.bottom > ball.bottom:
            return -1

    def compute_score(self, player, ball, score, x_dir, player_one=False, player_two=False):
        """ Docstring """
        if player_one and ball.left == self.BORDER_SIZE + 50:
            score -= score
            return score
        elif player_one and ball.right == self.SCREEN_WIDTH - self.BORDER_SIZE + 50:
            score += 10
            return score
        #verify a ball collision
        elif player_one and x_dir == 1 and player.right == ball.left and player.top < ball.top and player.bottom > ball.bottom:
            score += 1
            return score
        else:

            if player_two and ball.left == self.BORDER_SIZE + 50:
                score += 10
                return score
            elif player_two and ball.right == self.SCREEN_WIDTH - self.BORDER_SIZE + 50:
                score -= score
                return score
            #verify a ball collision
            elif player_two and x_dir == -1 and player.left == ball.right and player.top < ball.top and player.bottom > ball.bottom:
                score += 1
                return score
            else:
                return score
