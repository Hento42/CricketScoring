import pygame_gui, pygame, time, sys
from scorePage import *

class Settings:

    def __init__(self):
        self.screen_width = 400
        self.screen_height = 725
        self.bg_color = ("#141821")


class GUI():
    
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Configure game")

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

        typeLabel = pygame_gui.elements.UITextBox(html_text="Select Game Type:", relative_rect=pygame.Rect((15,15), (200,40)), manager=manager)
        gameType = pygame_gui.elements.UIDropDownMenu(options_list=("Fixed Wickets", "Fixed Overs", "Hundred"), starting_option="Fixed Wickets", relative_rect=pygame.Rect((15, 45), (200, 50)), manager=manager)
        
        wicketLabel = pygame_gui.elements.UITextBox(html_text="Available Wickets:", relative_rect=pygame.Rect((15,110), (200,40)), manager=manager)
        maxWickets = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((15, 140), (200, 50)), start_value=0, value_range=(0,10), manager=manager)
        wicketText = pygame_gui.elements.UITextBox(html_text=str(maxWickets.get_current_value()), relative_rect=pygame.Rect((215, 140), (40, 50)), manager=manager)
        
        overLabel = pygame_gui.elements.UITextBox(html_text="Available Overs:", relative_rect=pygame.Rect((15,205), (200,40)), manager=manager)
        maxOvers = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((15, 235), (200, 50)), start_value=0, value_range=(0,50), manager=manager)
        overText = pygame_gui.elements.UITextBox(html_text=str(maxOvers.get_current_value()), relative_rect=pygame.Rect((215, 235), (40, 50)), manager=manager)
        
        runLabel = pygame_gui.elements.UITextBox(html_text="Runs Lost Per Wicket:", relative_rect=pygame.Rect((15,300), (200,40)), manager=manager)
        wicketRuns = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((15, 330), (200, 50)), start_value=0, value_range=(0,10), manager=manager)
        runText = pygame_gui.elements.UITextBox(html_text=str(wicketRuns.get_current_value()), relative_rect=pygame.Rect((215, 330), (40, 50)), manager=manager)
        
        startingLabel = pygame_gui.elements.UITextBox(html_text="Starting Runs:", relative_rect=pygame.Rect((15,395), (200,40)), manager=manager)
        startingRuns = pygame_gui.elements.UIDropDownMenu(options_list=("0", "100", "200"), starting_option="0", relative_rect=pygame.Rect((15, 425), (200, 50)), manager=manager)

        bowlAgainLabel = pygame_gui.elements.UITextBox(html_text="Bowl Extras Again?", relative_rect=pygame.Rect((15,485), (200,40)), manager=manager)
        bowlAgain = pygame_gui.elements.UIDropDownMenu(options_list=("Yes", "No", "Last Over Only"), starting_option="Yes", relative_rect=pygame.Rect((15, 515), (200, 50)), manager=manager)
        
        extraLabel = pygame_gui.elements.UITextBox(html_text="Runs For Extras:", relative_rect=pygame.Rect((15,575), (200,40)), manager=manager)
        extraRuns = pygame_gui.elements.UIDropDownMenu(options_list=("0", "1", "2"), starting_option="0", relative_rect=pygame.Rect((15, 605), (200, 50)), manager=manager)
        
        start = pygame_gui.elements.UIButton(text="Start Scoring", relative_rect=pygame.Rect((15,665), (200, 45)))
        
        
        manager.draw_ui(disp)
        pygame.display.update()

        while running:

            time_delta = clock.tick(60)/1000.0
            manager.update(time_delta)
            disp.fill(self.settings.bg_color)
            manager.draw_ui(disp)
            pygame.display.update()
            
            wicketText.set_text(str(maxWickets.get_current_value()))
            overText.set_text(str(maxOvers.get_current_value()))
            runText.set_text(str(wicketRuns.get_current_value()))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    
                    if event.ui_element == start:
                        running = False
                        pygame.quit()
                        time.sleep(0.5)
                        startScoring(gameType.selected_option[0], maxWickets.get_current_value(), maxOvers.get_current_value(), wicketRuns.get_current_value(), startingRuns.selected_option[0], bowlAgain.selected_option[0], extraRuns.selected_option[0])
                    
                manager.process_events(event)
                    
        
if __name__ == '__main__':
    setup = GUI()
    setup.run_start()