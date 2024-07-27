import pygame
from icecream import ic

class Snake():
    '''Snake class to create the snake object'''

    def __init__(self, x=0, y=0, snake_block=10, direction="right", speed=2, colour=(255, 255, 255)):
        '''Initialise the snake object with the initial position, direction, speed and colour'''
        self.x = x
        self.y = y
        self.snake_block = snake_block
        self.head = [self.x, self.y]
        self.rect = pygame.Rect(self.x, self.y, self.snake_block, self.snake_block)
        self.body = [[self.x, self.y]]
        self.direction = direction
        self.speed = speed
        self.colour = colour

    def draw(self, game_screen):
        '''Draw the snake on the game screen'''
        for part in self.body:
            pygame.draw.rect(game_screen, (0,255,0), [part[0], part[1], self.snake_block, self.snake_block])

    def move(self):
        '''Move the snake in the current direction'''
        if self.direction == "right":
            self.x += self.speed
        elif self.direction == "left":
            self.x -= self.speed
        elif self.direction == "up":
            self.y -= self.speed
        elif self.direction == "down":
            self.y += self.speed
        self.head = [self.x, self.y]
        self.rect = pygame.Rect(self.x, self.y, self.snake_block, self.snake_block)
        self.body.insert(0, self.head)
        self.body.pop()

    def is_collision_with_food(self, food):
        '''Check if the snake has collided with the food block'''
        if pygame.Rect.colliderect(self.rect, food.rect):
            return True
        return False

    def eat_food(self):
        '''Increase the length of the snake when it eats the food block'''
        self.body.insert(0, self.head)

    def is_collision_with_wall(self, right_wall, left_wall, top_wall, bottom_wall):
        '''Check if the snake has collided with the walls of the game screen'''
        if (self.x + self.snake_block) >= right_wall or self.x < left_wall or (self.y + self.snake_block) >= bottom_wall or self.y < top_wall:
            return True
        return False

    def is_collision_with_self(self):
        '''Check if the snake has collided with itself'''
        if self.head in self.body[1:]:
            return True
        return False
