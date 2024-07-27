import pygame
from icecream import ic

class Scoreboard():
    '''Class to diaplay the high scores of the game'''
    def __init__(self, score_file, myfont, width):
        '''Initialise the scoreboard object with the high scores'''
        self.score_file = score_file
        self.top_scores = self.load_scores()
        self.myfont = myfont
        self.width = width

    def load_scores(self):
        '''Load the high scores from the file'''
        scores = []
        for line in open(self.score_file, "r"):
            name, score = line.strip().split(" ")
            scores.append((name, int(score)))
        return sorted(scores, key=lambda x: x[1], reverse=True)[:5]


    def new_high_score(self, player_score):
        '''Check if the current score is a new high score'''
        if player_score > self.top_scores[-1][1]:
            return True
        return False

    def add_score(self, name, score):
        '''Add the new high score to the scoreboard'''
        self.top_scores.append((name.upper(), score))
        self.top_scores = sorted(self.top_scores, key=lambda x: x[1], reverse=True)[:5]
        self.save_scores()

    def display_scores(self, game_screen):
        '''Display the high scores on the game screen'''
        y = 350
        myfont_size = 32
        for name, score in self.top_scores:
            self.myfont.render_to(game_screen, (self.width//2 - 100, y), f"{name} {score}", (255, 255, 255), None, size=myfont_size)
            y += myfont_size

    def save_scores(self):
        '''Save the high scores to the file'''
        with open(self.score_file, "w") as f:
            for name, score in self.top_scores:
                f.write(f"{name} {score}\n")

    #TO DO: fix this function - duplicate names break the dictionary for top scores
    def run_new_high_score_screen(self, score_screen, background, font_colour):
        '''Run the new high score screen'''
        active = True
        name = ' '
        score_screen.fill(background)
        self.myfont.render_to(score_screen, (self.width//2 - 350, 100), "New high score!", font_colour, size=76)
        self.myfont.render_to(score_screen, (self.width//2 - 350, 250), "You've made the leader board!", font_colour, size=24)
        self.myfont.render_to(score_screen, (self.width//2 - 350, 300), "Enter your player name: ", font_colour, size=24)

        while active:
            base_font = pygame.font.Font(None, 45)
            input_box = pygame.Rect(400, 400, 150, 50)
            color = pygame.Color('chartreuse4')
            for event in pygame.event.get():
            # if the user types QUIT then the screen will close
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    # Check for backspace
                    if event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    if event.key == pygame.K_RETURN:
                        active = False
                        return name.strip()
                    else:
                        if event.unicode.isalnum():
                            name += event.unicode.upper()
                    # draw rectangle and the argument passed which should be on-screen
                pygame.draw.rect(score_screen, color, input_box)
                txt_surface = base_font.render(name , True, font_colour)
                # render at position stated in arguments
                score_screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
                # set the width of textfield so that text cannot get outside of user's text input
                input_box.w = max(100, txt_surface.get_width()+10)
                # display.flip() will try to update only a portion of the screen to updated, not full area
                pygame.display.flip()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    active = False
                    return name.strip()
        # return name
