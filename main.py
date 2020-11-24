# -*- coding: utf-8 -*-

import pygame
import sys
from pygame.locals import *

from src.Court import Tennis_Court as court
from src.Court import Collisions
from src.Court import Paddle
from src.Court import Ball


class Main_Game():
    """ Docstring """

    def __init__(self):
        """ Constructor """

        pygame.init()
        pygame.display.set_caption('Pyng Pong - from Francisco Camello')
        self.FONTSIZE = 20
        self.FONT = pygame.font.Font('freesansbold.ttf', self.FONTSIZE)
        self.SCREEN_WIDTH = 500
        self.SCREEN_HEIGHT = 400
        self.SCREEN = pygame.display.set_mode(
            (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.FPS = 200
        self.FPSCLOCK = pygame.time.Clock()
        self.finish = False
        self.score_one = 0
        self.score_two = 0

    def init_game(self):
        """ Docstring """

        # creates the players
        player_one = Paddle((255, 255, 255), 65, 175)
        player_two = Paddle((255, 255, 255), 430, 175)

        # creates the ball
        ball = Ball((255, 255, 255), 5, 5)

        # this will be a list of sprites
        all_sprites_list = pygame.sprite.Group()

        # Add the paddles to the list of sprites
        all_sprites_list.add(player_one)
        all_sprites_list.add(player_two)
        all_sprites_list.add(ball)


        court().create_court(self.SCREEN)

        while True:
            self.SCREEN.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEMOTION:
                    mouseX, mouseY = event.pos
                    player_one.rect.y = mouseY
                    pygame.mouse.set_visible(1)

            all_sprites_list.update()

            # creates the court
            court().create_court(self.SCREEN)

            # detect collisions between ball and the walls
            Collisions().wall_collision(ball)

            # detect collisions between the ball and the players
            if pygame.sprite.collide_mask(ball, player_one):
                ball.bounce()
                self.score_one +=1
            elif pygame.sprite.collide_mask(ball, player_two):
                ball.bounce()
                self.score_two += 1

            # computer movements
            player_two = Collisions().computer_movements(ball, player_two)

            # scores points for player one
            self.score_one = Collisions().compute_score(
                player_one, ball, self.score_one, True)


            # if self.score_one > 1 and self.score_one % 10 == 0:
            #     ball.velocity[0] += 1

            # # scores points for player two
            self.score_two = Collisions().compute_score(
                player_two, ball, self.score_two, player_two=True)

            # shows the score for both players
            Collisions().create_score(self.SCREEN, 'You', self.score_one, self.FONT, (100, 15))
            Collisions().create_score(self.SCREEN, 'PC', self.score_two, self.FONT, (300, 15))

            # now let's draw all the sprites in one go
            all_sprites_list.draw(self.SCREEN)

            # pygame.display.update()
            pygame.display.flip()

            self.FPSCLOCK.tick(self.FPS)


Main_Game().init_game()
