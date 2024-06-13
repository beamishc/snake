import pygame
import pygame.freetype
import os
from snake_class import Snake
from food_class import Food
from icecream import ic

# RGB color codes
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
RED_COLOR = (255, 0, 0)

# define the clock
clock = pygame.time.Clock()

font_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),"fonts","slkscr.ttf")
# font_size = tx
pygame.freetype.init()
myfont = pygame.freetype.Font(font_path, 16)

# game width and game height
width = 800
height = 600
real_height = 650

# game title
title = "SnAkE"

# wall width from edge
wall_to_edge = 2

# wall width
wall_width = 4

# initialise game
pygame.init()

ic('Welcome to the Snake Game!')

class Game:
    '''Game class to run the game loop'''
    # Typical rate of 60 , equivalent to FPS
    TICK_RATE = 60

    def __init__(self, level = 1, snake_block = 10, snake_speed = 2, snake_colour = WHITE_COLOR):
        # scoring
        self.score = 0
        self.level = level
        self.increment = 10 * self.level

        # set wall edges
        self.right_wall = width - (wall_to_edge + wall_width)
        self.left_wall = wall_to_edge + wall_width
        self.top_wall = wall_to_edge + wall_width + (real_height - height)
        self.bottom_wall = real_height - (wall_to_edge + wall_width)

        # instantiate classes
        self.food = Food(self.left_wall, self.right_wall, self.top_wall, self.bottom_wall)
        self.snake = Snake(x = width // 2, y= height // 2, snake_block=snake_block, speed=snake_speed, colour=snake_colour)

        # Set up the screen
        self.game_screen = pygame.display.set_mode((width, real_height))

        self.game_screen.fill(BLACK_COLOR)

        pygame.display.set_caption(title)

        self.snake.draw(self.game_screen)

    def run_game_loop(self):
        '''Game loop to run the game until game over'''
        game_over = False

        while not game_over:
            # Handle events
            for event in pygame.event.get():
                # ic(event)
                # End if quit
                if event.type == pygame.QUIT:
                    game_over = True

                # Change direction of the snake
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.snake.direction != "down":
                        self.snake.direction = "up"
                    elif event.key == pygame.K_DOWN and self.snake.direction != "up":
                        self.snake.direction = "down"
                    elif event.key == pygame.K_LEFT and self.snake.direction != "right":
                        self.snake.direction = "left"
                    elif event.key == pygame.K_RIGHT and self.snake.direction != "left":
                        self.snake.direction = "right"

            # Refresh screen
            self.game_screen.fill(BLACK_COLOR)

            # Draw score
            myfont.render_to(self.game_screen, (4, 4), str(self.score), WHITE_COLOR, None, size=64)

            # Draw food
            self.food.draw(self.game_screen)

            # Move the snake
            self.snake.move()
            self.snake.draw(self.game_screen)

            # detect collision with walls
            if self.snake.is_collision_with_wall(self.right_wall, self.left_wall, self.top_wall, self.bottom_wall):
                ic('Hit a wall! Game Over!')
                game_over = True

            # detect collision with self
            if self.snake.is_collision_with_self():
                ic('Stop hitting yourself! Game Over!')
                game_over = True

            # detect collision with food
            if self.snake.is_collision_with_food(self.food):
                ic('Nom!')
                self.score += self.increment
                self.snake.eat_food()
                self.food = Food(self.left_wall, self.right_wall, self.top_wall, self.bottom_wall)
                self.food.draw(self.game_screen)
                if len(self.snake.body) % 20 == 0:
                    self.level += 1
                    ic(f'Level {self.level}')
                    self.increment = 10 * self.level


            # Draw walls
            # left wall
            pygame.draw.rect(self.game_screen, WHITE_COLOR, [wall_to_edge, wall_to_edge + (real_height - height), wall_width, height-(wall_width)  + (real_height - height)])
            # top wall
            pygame.draw.rect(self.game_screen, WHITE_COLOR, [wall_to_edge, wall_to_edge + (real_height - height), width-(wall_width), wall_width])
            # right wall
            pygame.draw.rect(self.game_screen, WHITE_COLOR, [width-(wall_to_edge + wall_width), wall_to_edge + (real_height - height), wall_width, height-(wall_width) + (real_height - height)])
            # bottom wall
            pygame.draw.rect(self.game_screen, WHITE_COLOR, [wall_to_edge, height-(wall_to_edge + wall_width) + (real_height - height), width-wall_to_edge, wall_width])

            # Update the screen
            pygame.display.update()

            # Tick the clock to update everything within the game
            clock.tick(self.TICK_RATE)

        if game_over:
            ic(self.score)
            pygame.quit()
            quit()

game = Game()
game.run_game_loop()
