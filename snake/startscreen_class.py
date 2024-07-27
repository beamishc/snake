import pygame
from icecream import ic
from scoreboard_class import Scoreboard

class Startscreen():
    '''Class to run the start screen for the game'''
    def __init__(self, screen, width, real_height, title, myfont, background, font_colour):
        self.screen = screen
        self.width = width
        self.real_height = real_height
        self.title = title
        self.myfont = myfont
        self.background = background
        self.font_colour = font_colour
        self.high_scores = Scoreboard("snake/high_scores.txt", self.myfont, width)
        self.start_screen = pygame.display.set_mode((self.width, self.real_height))

    def run_startscreen(self):
        '''Run the start screen for the game'''
        waiting = True

        while waiting:
            self.start_screen.fill(self.background)
            pygame.display.set_caption(self.title)

            self.myfont.render_to(self.start_screen, (self.width//2 - 350, 200), "Welcome to the Snake Game!", self.font_colour, size=42)
            self.myfont.render_to(self.start_screen, (self.width//2 - 250, 250), "Press any key to start the game", self.font_colour, size=24)

            self.high_scores.display_scores(self.start_screen)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    waiting = False
                    break

    def get_high_scores(self):
        '''Return the high scores object'''
        return self.high_scores
