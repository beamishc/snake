import pygame

# RGB color codes
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)

# define the clock
clock = pygame.time.Clock()

width = 800
height = 600
title = "SnAkE"

# initialise game
pygame.init()

class Game:
    # Typical rate of 60 , equivalent to FPS
    TICK_RATE = 60

    def __init__(self):
        self.snake_length = 1
        self.level = 0

        # Set up the screen
        self.game_screen = pygame.display.set_mode((width, height))

        self.game_screen.fill(WHITE_COLOR)

        pygame.display.set_caption(title)

    def run_game_loop(self):
        game_over = False

        while not game_over:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True

            self.snake = pygame.draw.rect(self.game_screen,WHITE_COLOR,[200,150,10,10])

            # Update the screen
            pygame.display.update()

            # Tick the clock to update everything within the game
            clock.tick(self.TICK_RATE)

        # end game
        pygame.quit()
        quit()
