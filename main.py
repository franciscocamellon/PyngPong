# -*- coding: utf-8 -*-

import pygame
import sys
from pygame.locals import *

from src.Court import Tenis_Court as court
from src.Court import Pong_Player as player
from src.Court import Pong_Ball as ball
from src.Court import Movements as mov


class Main_Game():
    """ Docstring """

    def __init__(self):
        """ Constructor """

        pygame.init()
        pygame.display.set_caption('Crazy Snake Pong - from Francisco Camello')
        self.FONTSIZE = 20
        self.FONT = pygame.font.Font('freesansbold.ttf', self.FONTSIZE)
        self.SCREEN_WIDTH = 500
        self.SCREEN_HEIGHT = 400
        self.SCREEN = pygame.display.set_mode(
            (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.FPS = 200
        self.FPSCLOCK = pygame.time.Clock()
        self.BORDER_SIZE = 5
        self.finish = False
        self.ball_x_dir = -1
        self.ball_y_dir = -1
        self.score_player_one = 0
        self.score_player_two = 0

    def init_game(self):
        """ Docstring """

        # self.ball_x_pos = ball().ball_position()[0]
        # self.ball_y_pos = ball().ball_position()[1]

        self.ball_x_pos = 245
        self.ball_y_pos = 195

        # print(self.ball_x_pos, self.ball_y_pos)

        player_one_pos = player().player_position()
        player_two_pos = player().player_position()

        # print(player_one_pos, player_two_pos)

        player_one = pygame.Rect(70, player_one_pos, 5, 50)
        player_two = pygame.Rect((430), player_two_pos, 5, 50)
        # _ball = pygame.Rect(self.ball_x_pos, self.ball_x_pos, 5, 5)
        _ball = pygame.Rect(245, 195, 5, 5)

        # print(player_one, player_two)

        court().create_court(self.SCREEN)
        player().create_player(self.SCREEN, self.SCREEN_HEIGHT, player_one)
        player().create_player(self.SCREEN, self.SCREEN_HEIGHT, player_two)
        ball().create_ball(self.SCREEN, _ball)


        while True:
            self.SCREEN.fill((0, 0, 0))

            # Checar os eventos do mouse aqui:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEMOTION:
                    mouseX, mouseY = event.pos
                    player_one.y = mouseY
                    pygame.mouse.set_visible(1)


            court().create_court(self.SCREEN)
            player().create_player(self.SCREEN, self.SCREEN_HEIGHT, player_one)
            player().create_player(self.SCREEN, self.SCREEN_HEIGHT, player_two)
            ball().create_ball(self.SCREEN, _ball)

            _ball = mov().ball_movement(_ball, self.ball_x_dir, self.ball_y_dir)
            self.ball_x_dir, self.ball_y_dir = mov().verify_collision( _ball,
                                                                      self.ball_x_dir,
                                                                      self.ball_y_dir)
            new_dir = mov().ball_collision(_ball, player_one, player_two, self.ball_x_dir)
            if new_dir == 1:
                self.ball_x_dir = self.ball_x_dir * new_dir
            elif new_dir == -1:
                self.ball_x_dir = self.ball_x_dir * new_dir
            else:
                self.ball_x_dir = self.ball_x_dir
            # self.ball_x_dir = self.ball_x_dir * mov().ball_collision(_ball, player_one, player_two, self.ball_x_dir)
            # a = mov().ball_collision(_ball, player_one, player_two, self.ball_x_dir)
            # print('a: ',a)
            player_two = mov().computer_movements(_ball, self.ball_x_dir, player_two)
            self.score_player_one = mov().compute_score(player_one, _ball, self.score_player_one, self.ball_x_dir, True)
            self.score_player_two = mov().compute_score(player_two, _ball, self.score_player_two, self.ball_x_dir, player_two=True)
            player().create_score(self.SCREEN, 'You', self.score_player_one, self.FONT, (100,15))
            player().create_score(self.SCREEN, 'PC',self.score_player_two, self.FONT, (300,15))

            # Atualiza o desenho na tela
            pygame.display.update()

            # Configura 200 atualizações de tela por segundo
            self.FPSCLOCK.tick(self.FPS)


Main_Game().init_game()
