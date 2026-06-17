import pygame_gui, pygame

class Settings:

    def __init__(self):
        self.screen_width = 1500
        self.screen_height = 750
        self.bg_color = ("#141821")


class GUI():
    
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Cricket Scoring")

    def run_start(self):
        disp = self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        background = pygame.Surface((self.settings.screen_width,self.settings.screen_height))
        width = self.settings.screen_width
        height = self.settings.screen_height

        self.screen.fill(self.settings.bg_color)
        pygame.display.update()

        manager = pygame_gui.UIManager((width,height))
        
        clock = pygame.time.Clock()
        running = True

        #pygame.draw.line(disp, (255,255,255), (500,0), (500, 750), 5)
        pygame.draw.rect(disp, (255,255,255), (505,5, 990, 740), 5)
        
        manager.draw_ui(disp)
        pygame.display.update()

        while running:

            time_delta = clock.tick(60)/1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
        
 
def startScoring(gameType, maxWickets, maxOvers, wicketRuns, startingRuns, bowlAgain, extraRuns):
    print(gameType, maxWickets, maxOvers, wicketRuns, startingRuns, bowlAgain, extraRuns)       
    scorePage = GUI()
    scorePage.run_start()
