import pygame
import pygame.freetype
import os
from startscreen_class import Startscreen
from game_class import Game
from icecream import ic

# RGB color codes
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
RED_COLOR = (255, 0, 0)

# define the clock
clock = pygame.time.Clock()

font_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),"fonts","slkscr.ttf")
pygame.freetype.init()
myfont = pygame.freetype.Font(font_path, 16)

# game width and game height
width = 800
height = 600
real_height = 650

# game title
title = "SnAkE"

# initialise game
pygame.init()

ic('Welcome to the Snake Game!')

start = Startscreen(pygame.display.set_mode, width, real_height, title, myfont, BLACK_COLOR, WHITE_COLOR)
start.run_startscreen()
high_scores = start.get_high_scores()

game = Game(width, height, real_height)
game.run_game_loop(myfont, clock)

if high_scores.new_high_score(game.score):
    score_screen = pygame.display.set_mode((width, real_height))
    name = high_scores.run_new_high_score_screen(score_screen, BLACK_COLOR, WHITE_COLOR)
    high_scores.add_score(name.upper(), game.score)
    high_scores.save_scores()

start.run_startscreen()
