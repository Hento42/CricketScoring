import pygame_gui, pygame
from scoring import score

class Settings:

    def __init__(self):
        self.screen_width = 1300
        self.screen_height = 750
        self.bg_color = ("#141821")


class GUI():
    
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Cricket Scoring")

    def run_start(self, scoreClass):
        disp = self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        background = pygame.Surface((self.settings.screen_width,self.settings.screen_height))
        width = self.settings.screen_width
        height = self.settings.screen_height
        runCounter = 0

        self.screen.fill(self.settings.bg_color)
        pygame.display.update()

        manager = pygame_gui.UIManager((width,height))
        manager.get_theme().load_theme('themes.json')
        
        clock = pygame.time.Clock()
        running = True

        pygame.draw.rect(disp, (255,255,255), (305, 5, 990, 740), 5)
        
        runText = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((15,15), (270,40)), html_text="Enter runs scored (excluding extras):", manager=manager)
        minus = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((15,60), (50,50)), text="-1", manager=manager)
        runs = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((65,60), (50,50)), html_text="0", manager=manager, object_id=pygame_gui.core.ObjectID(class_id='@CentredText'))
        plus = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((115,60), (50,50)), text="+1", manager=manager)

        wide = pygame_gui.elements.UICheckBox(relative_rect=pygame.Rect((15,120), (20,20)), text="Wide", manager=manager)
        noball = pygame_gui.elements.UICheckBox(relative_rect=pygame.Rect((15,145), (20,20)), text="No Ball", manager=manager)
        bye = pygame_gui.elements.UICheckBox(relative_rect=pygame.Rect((15,170), (20,20)), text="Byes", manager=manager)
        wicket = pygame_gui.elements.UICheckBox(relative_rect=pygame.Rect((15,195), (20,20)), text="Wicket", manager=manager)

        pygame.draw.line(disp, "#25292e", (15, 240), (290, 240), 5)

        bowled = pygame_gui.elements.UICheckBox(relative_rect=pygame.Rect((15,250), (20,20)), text="Bowled", manager=manager)
        caught = pygame_gui.elements.UICheckBox(relative_rect=pygame.Rect((15,275), (20,20)), text="Caught", manager=manager)
        lbw = pygame_gui.elements.UICheckBox(relative_rect=pygame.Rect((15,300), (20,20)), text="LBW", manager=manager)
        runout = pygame_gui.elements.UICheckBox(relative_rect=pygame.Rect((15,325), (20,20)), text="Run out", manager=manager)
        stumped = pygame_gui.elements.UICheckBox(relative_rect=pygame.Rect((15,350), (20,20)), text="Stumped", manager=manager)
        retired = pygame_gui.elements.UICheckBox(relative_rect=pygame.Rect((15,375), (20,20)), text="Retired", manager=manager)
        hittwice = pygame_gui.elements.UICheckBox(relative_rect=pygame.Rect((15,400), (20,20)), text="Hit twice", manager=manager)
        hitwicket = pygame_gui.elements.UICheckBox(relative_rect=pygame.Rect((15,425), (20,20)), text="Hit wicket", manager=manager)
        obstructing = pygame_gui.elements.UICheckBox(relative_rect=pygame.Rect((15,450), (20,20)), text="Obstructing the field", manager=manager)
        timedout = pygame_gui.elements.UICheckBox(relative_rect=pygame.Rect((15,475), (20,20)), text="Timed out", manager=manager)
        wicketList = [bowled, caught, lbw, runout, stumped, retired, hittwice, hitwicket, obstructing, timedout]
        for box in wicketList:
            box.disable()
        noBallWickets = [runout, retired, hittwice, obstructing, timedout]
        wideWickets = [runout, stumped, retired, hitwicket, obstructing, timedout]

        pygame.draw.line(disp, "#25292e", (15, 505), (290, 505), 5)

        submit = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((15,685), (275,50)), text="Enter runs from delivery", manager=manager)



        manager.draw_ui(disp)
        pygame.display.update()

        while running:

            time_delta = clock.tick(60)/1000.0
            manager.update(time_delta)
            disp.fill(self.settings.bg_color)
            pygame.draw.rect(disp, (255,255,255), (305,5, 990, 740), 5)
            pygame.draw.line(disp, "#25292e", (15, 240), (290, 240), 5)
            pygame.draw.line(disp, "#25292e", (15, 505), (290, 505), 5)
            manager.draw_ui(disp)
            pygame.display.update()

            runs.set_text(str(runCounter))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    
                    if event.ui_element == minus:
                        if runCounter > 0:
                            runCounter -= 1
                    elif event.ui_element == plus:
                        runCounter += 1
                    elif event.ui_element == submit:
                        options = [wide.get_state(), noball.get_state(), bye.get_state()]

                if event.type == pygame_gui.UI_CHECK_BOX_CHECKED:

                    if event.ui_element == wide:
                        noball.set_state(False)
                        bye.set_state(False)
                        bye.disable()
                        if wicket.get_state():
                            for box in wicketList:
                                if box not in wideWickets:
                                    box.set_state(False)
                                    box.disable()
                    elif event.ui_element == noball:
                        wide.set_state(False)
                        if wicket.get_state():
                            for box in wicketList:
                                if box not in noBallWickets:
                                    box.set_state(False)
                                    box.disable()
                    elif event.ui_element == wicket:
                        if noball.get_state():
                            for box in noBallWickets:
                                box.enable()
                        elif wide.get_state():
                            for box in wideWickets:
                                box.enable()
                        else:
                            for box in wicketList:
                                box.enable()

                            
                    elif event.ui_element in wicketList:
                        for box in wicketList:
                            if box != event.ui_element:
                                box.set_state(False)

                if event.type == pygame_gui.UI_CHECK_BOX_UNCHECKED:

                    if event.ui_element == wicket:
                        for box in wicketList:
                            box.set_state(False)
                            box.disable()
                    elif event.ui_element == wide:
                        bye.enable()
                        if wicket.get_state():
                            for box in wicketList:
                                box.enable()
                            if noball.get_state():
                                for box in wicketList:
                                    if box not in noBallWickets:
                                        box.set_state(False)
                                        box.disable()
                    elif event.ui_element == noball:
                        if wicket.get_state():
                            for box in wicketList:
                                box.enable()
                            if wide.get_state():
                                for box in wicketList:
                                    if box not in wideWickets:
                                        box.set_state(False)
                                        box.disable()
                    
                manager.process_events(event)
                    
        
 
def startScoring(gameType, maxWickets, maxOvers, wicketRuns, startingRuns, inningsNum, bowlAgain, extraRuns):
    print(gameType, maxWickets, maxOvers, wicketRuns, startingRuns, inningsNum, bowlAgain, extraRuns)       
    scorePage = GUI()
    scorePage.run_start(score(gameType, maxWickets, maxOvers, wicketRuns, startingRuns, inningsNum, bowlAgain, extraRuns))
