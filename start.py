import pygame

# RGB color codes
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
RED_COLOR = (255, 0, 0)

# define the clock
clock = pygame.time.Clock()

# game width and game height
width = 800
height = 600

# game title
title = "SnAkE"

# wall width from edge
wall_to_edge = 2

# wall width
wall_width = 4

# initialise game
pygame.init()

class Game:
    # Typical rate of 60 , equivalent to FPS
    TICK_RATE = 60

    def __init__(self):
        self.snake_block = 10
        self.snake_length = 1
        self.level = 0
        self.snake_x = width / 2
        self.snake_y = height / 2
        self.snake_body = [[self.snake_x, self.snake_y]]
        self.snake_speed = 2

        # Set up the screen
        self.game_screen = pygame.display.set_mode((width, height))

        self.game_screen.fill(BLACK_COLOR)

        pygame.display.set_caption(title)

    def run_game_loop(self):
        game_over = False
        x_diff, y_diff = 0, 0

        while not game_over:
            # Handle events
            for event in pygame.event.get():
                # End if quit
                if event.type == pygame.QUIT:
                    game_over = True

                # Change direction of the snake
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        x_diff, y_diff = 0, -self.snake_speed
                    elif event.key == pygame.K_DOWN:
                        x_diff, y_diff =  0, self.snake_speed
                    elif event.key == pygame.K_LEFT:
                        x_diff, y_diff =  -self.snake_speed, 0
                    elif event.key == pygame.K_RIGHT:
                        x_diff, y_diff =  self.snake_speed, 0

            self.snake_x += x_diff
            self.snake_y += y_diff

            # Draw the snake
            self.game_screen.fill(BLACK_COLOR)
            self.snake = pygame.draw.rect(self.game_screen, WHITE_COLOR, [self.snake_x, self.snake_y, self.snake_block, self.snake_block])

            # detect collision with walls
            if (self.snake_x + self.snake_block) >= width-(wall_to_edge + wall_width) or self.snake_x < wall_to_edge + wall_width or \
                (self.snake_y + self.snake_block) >= height-(wall_to_edge + wall_width) or self.snake_y < wall_to_edge + wall_width:
                game_over = True

            # Draw walls
            # left wall
            pygame.draw.rect(self.game_screen, WHITE_COLOR, [wall_to_edge, wall_to_edge, wall_width, height-(wall_width)])
            # top wall
            pygame.draw.rect(self.game_screen, WHITE_COLOR, [wall_to_edge, wall_to_edge, width-(wall_width), wall_width])
            # right wall
            pygame.draw.rect(self.game_screen, WHITE_COLOR, [width-(wall_to_edge + wall_width), wall_to_edge, wall_width, height-(wall_width)])
            # bottom wall
            pygame.draw.rect(self.game_screen, WHITE_COLOR, [wall_to_edge, height-(wall_to_edge + wall_width), width-wall_to_edge, wall_width])

            # Update the screen
            pygame.display.update()

            # Tick the clock to update everything within the game
            clock.tick(self.TICK_RATE)

        if game_over:
            pygame.quit()
            quit()

game = Game()
game.run_game_loop()
