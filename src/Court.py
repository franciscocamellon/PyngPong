# -*- coding: utf-8 -*-

import pygame
from random import randint


class Tennis_Court():
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


class Collisions(Tennis_Court):
    """ Docstring """

    def __init__(self):
        """ Constructor """
        super().__init__()

    def wall_collision(self, ball):
        """ Docstring """
        if ball.rect.x >= 445:
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.x <= 55:
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.y > 345:
            ball.velocity[1] = -ball.velocity[1]
        if ball.rect.y < 55:
            ball.velocity[1] = -ball.velocity[1]

    def computer_movements(self, ball, player):
        """ Docstring """
        if ball.velocity[0] == 1:
            if player.rect.centery < ball.rect.centery:
                player.rect.y += 1
            else:
                player.rect.y -= 1
        return player

    def compute_score(self, player, ball, score, player_one=False, player_two=False):
        """ Docstring """
        if player_one and ball.rect.left == 55:
            score -= score
            return score
        elif player_one and ball.rect.right == 445:
            score += 10
            return score
        else:
            if player_two and ball.rect.left == 55:
                score += 10
                return score
            elif player_two and ball.rect.right == 445:
                score -= score
                return score
            else:
                return score

    def create_score(self, screen, text, score, font, position):
        """ Docstring """
        score_result = font.render(
            '{0} = {1}'.format(text, score), True, self.COLOR)
        score_result_rect = score_result.get_rect()
        score_result_rect.topleft = (position)
        return screen.blit(score_result, score_result_rect)


class Paddle(pygame.sprite.Sprite):
    # This class represents a paddle. It derives from the "Sprite" class in Pygame.

    def __init__(self, color, x, y):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.image = pygame.Surface(
            [Tennis_Court().BORDER_SIZE, Tennis_Court().PLAYER_SIZE])
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        pygame.draw.rect(self.image, color, [
                         0, 0, Tennis_Court().BORDER_SIZE, Tennis_Court().PLAYER_SIZE])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Ball(pygame.sprite.Sprite):
    # This class represents a ball. It derives from the "Sprite" class in Pygame.

    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.image = pygame.Surface(
            [Tennis_Court().BORDER_SIZE, Tennis_Court().BORDER_SIZE])
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        pygame.draw.rect(self.image, color, [
                         0, 0, Tennis_Court().BORDER_SIZE, Tennis_Court().BORDER_SIZE])
        self.velocity = [1, 1]
        self.rect = self.image.get_rect()
        self.rect.x = Tennis_Court().SCREEN_WIDTH // 2
        self.rect.y = Tennis_Court().SCREEN_HEIGHT // 2

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-1, 1)
