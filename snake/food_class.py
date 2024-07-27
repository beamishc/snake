import random
import pygame
from icecream import ic

class Food():
    '''Food class to create the food block for the snake to eat'''

    def __init__(self, left_wall, right_wall, top_wall, bottom_wall, colour = (255,255,255), food_block = 10):
        '''Initialise the food block at a random position within the game screen'''
        self.range_x = [left_wall, right_wall-(food_block-1)]
        self.range_y = [top_wall, bottom_wall-(food_block-1)]
        self.x = random.randint(*self.range_x)
        self.y = random.randint(*self.range_y)
        self.food_block = food_block
        self.colour = colour

    def draw(self, game_screen):
        '''Draw the food block on the game screen'''
        self.rect = pygame.Rect(self.x, self.y, self.food_block, self.food_block)
        pygame.draw.rect(game_screen, self.colour, [self.x, self.y, self.food_block, self.food_block])

    def update(self):
        '''Update the position of the food block'''
        self.x = random.randint(*self.range_x)
        self.y = random.randint(*self.range_y)
        self.rect = pygame.Rect(self.x, self.y, self.food_block, self.food_block)
