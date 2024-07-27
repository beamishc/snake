import pygame
import pygame.freetype
from snake_class import Snake
from food_class import Food
from icecream import ic

WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
RED_COLOR = (255, 0, 0)

class Game:
    '''Game class to run the game loop'''
    # Typical rate of 60 , equivalent to FPS
    TICK_RATE = 60

    def __init__(self, width, height, real_height, title = "SnAkE", level = 1, snake_block = 15, snake_speed = 2, snake_colour = WHITE_COLOR):
        # scoring
        self.score = 0
        self.level = level
        self.increment = 10 * self.level

        # wall width from edge
        w2e = 2

        # wall width
        ww = 4

        # gap between top of screen and game screen
        top_gap = real_height - height

        # set wall edges
        self.left_wall = w2e + ww
        self.right_wall = width - self.left_wall
        self.top_wall = self.left_wall + top_gap
        self.bottom_wall = real_height - self.left_wall

        # define wall dimensions

        # [left_x, top_y, right_x, bottom_y] - w2e is the wall width from the edge, ww is the wall width
        top = w2e + top_gap
        bottom = height - ww + top_gap

        # [left wall, top wall, right wall, bottom wall]
        self.dimensions = [[w2e, top, ww, bottom]\
                        , [w2e, top, width - ww, ww]\
                        , [self.right_wall, top, ww, bottom]\
                        , [w2e, height - self.left_wall + top_gap, width - w2e, ww]]


        # instantiate classes
        self.snake = Snake(x = width // 2, y = height // 2, snake_block=snake_block, speed=snake_speed, colour=snake_colour)
        self.food = Food(self.left_wall, self.right_wall, self.top_wall, self.bottom_wall, food_block=self.snake.snake_block)

        # Set up the screen
        self.game_screen = pygame.display.set_mode((width, real_height))

        self.game_screen.fill(BLACK_COLOR)

        pygame.display.set_caption(title)

        self.snake.draw(self.game_screen)

    def update(self):
        ic('Nom!')
        self.score += self.increment
        self.snake.eat_food()
        self.food = Food(self.left_wall, self.right_wall, self.top_wall, self.bottom_wall, food_block=self.snake.snake_block)
        self.food.draw(self.game_screen)
        if len(self.snake.body) % 20 == 0:
            self.level += 1
            ic(f'Level {self.level}')
            self.increment = 10 * self.level

    def run_game_loop(self, myfont, clock):
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
            myfont.render_to(self.game_screen, (4, 4), f"Score: {str(self.score)}", WHITE_COLOR, None, size=64)

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
                self.update()

            for dimension in self.dimensions:
                pygame.draw.rect(self.game_screen, WHITE_COLOR, dimension)

            # Update the screen
            pygame.display.update()

            # Tick the clock to update everything within the game
            clock.tick(self.TICK_RATE)

        if game_over:
            ic(self.score)
