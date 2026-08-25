import pygame_gui, pygame
from scoring import score

class Settings:

    def __init__(self):
        self.screen_width = 1400
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

        pygame.draw.rect(disp, "#76787a", (305, 5, 1088, 740), 5)

        if scoreClass.maxOvers == 0 and scoreClass.gameType == 0:
            scoresheet = noOverLimit(disp)
        elif scoreClass.gameType == 2:
            scoresheet = twentyOverLimit(disp)
        else:
            if (scoreClass.maxOvers / 10) <= 10:
                scoresheet = tenOverLimit(disp)
            elif (scoreClass.maxOvers / 10) <= 20:
                scoresheet = twentyOverLimit(disp)
            elif (scoreClass.maxOvers / 10) <= 50:
                scoresheet = fiftyOverLimit(disp)

        currentOver = ""
        
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

            if scoreClass.inningsDoneCheck():
                submit.disable()
                print("Innings over")
                running = False

            time_delta = clock.tick(60)/1000.0
            manager.update(time_delta)
            disp.fill(self.settings.bg_color)
            pygame.draw.rect(disp, "#76787a", (305, 5, 1088, 740), 5)

            if scoreClass.maxOvers == 0 and scoreClass.gameType == 0:
                noOverLimit(disp)
            elif scoreClass.gameType == 2:
                twentyOverLimit(disp)
            else:
                if (scoreClass.maxOvers / 10) <= 10:
                    tenOverLimit(disp)
                elif (scoreClass.maxOvers / 10) <= 20:
                    twentyOverLimit(disp)
                elif (scoreClass.maxOvers / 10) <= 50:
                    fiftyOverLimit(disp)


            pygame.draw.line(disp, "#25292e", (15, 240), (290, 240), 5)
            pygame.draw.line(disp, "#25292e", (15, 505), (290, 505), 5)
            for i in range(len(scoresheet[0])):
                disp.blit(scoresheet[0][i], scoresheet[1][i])
            manager.draw_ui(disp)

            font = pygame.font.Font(None, 74)
            textSurface = font.render((str(scoreClass.runs) + "/" + str(scoreClass.wickets) + " (" + str(scoreClass.overs / 10) + ")"), True, (255,255,255))
            disp.blit(textSurface, (15, 520))

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
                        newFont = pygame.font.Font(None, 30)
                        print(scoresheet)
                        options = [wide.get_state(), noball.get_state(), bye.get_state(), wicket.get_state(), runCounter]
                        overNum = scoreClass.overs // 10
                        symbol, newOver = inputToRunsScored(options, scoreClass)
                        currentOver += symbol + "  "
                        scoresheet[0][overNum] = newFont.render((currentOver), True, (255,255,255))
                        for i in range(len(scoresheet[0])):
                            disp.blit(scoresheet[0][i], scoresheet[1][i])
                        if newOver:
                            currentOver = ""



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


def inputToRunsScored(options, scoreClass):

    if options[0]:
        symbol, newOver = scoreClass.ballBowled(1, options[4], options[3])
    elif options[1] and not options[2]:
        symbol, newOver = scoreClass.ballBowled(2, options[4], options[3])
    elif options[1] and options[2]:
        symbol, newOver = scoreClass.ballBowled(3, options[4], options[3])
    elif options[2]:
        symbol, newOver = scoreClass.ballBowled(4, options[4], options[3])
    else:
        symbol, newOver = scoreClass.ballBowled(0, options[4], options[3])

    scoreClass.getScore()
    return symbol, newOver


def noOverLimit(disp):
    pygame.draw.line(disp, "#76787a", (441, 5), (441, 740), 2)
    pygame.draw.line(disp, "#76787a", (577, 5), (577, 740), 2)
    pygame.draw.line(disp, "#76787a", (713, 5), (713, 740), 2)
    pygame.draw.line(disp, "#76787a", (849, 5), (849, 740), 2)
    pygame.draw.line(disp, "#76787a", (985, 5), (985, 740), 2)
    pygame.draw.line(disp, "#76787a", (1121, 5), (1121, 740), 2)
    pygame.draw.line(disp, "#76787a", (1257, 5), (1257, 740), 2)

    pygame.draw.line(disp, "#76787a", (305, 42), (1390, 42), 2)
    pygame.draw.line(disp, "#76787a", (305, 79), (1390, 79), 2)
    pygame.draw.line(disp, "#76787a", (305, 116), (1390, 116), 2)
    pygame.draw.line(disp, "#76787a", (305, 153), (1390, 153), 2)
    pygame.draw.line(disp, "#76787a", (305, 190), (1390, 190), 2)
    pygame.draw.line(disp, "#76787a", (305, 227), (1390, 227), 2)
    pygame.draw.line(disp, "#76787a", (305, 264), (1390, 264), 2)
    pygame.draw.line(disp, "#76787a", (305, 301), (1390, 301), 2)
    pygame.draw.line(disp, "#76787a", (305, 338), (1390, 338), 2)
    pygame.draw.line(disp, "#76787a", (305, 375), (1390, 375), 2)
    pygame.draw.line(disp, "#76787a", (305, 412), (1390, 412), 2)
    pygame.draw.line(disp, "#76787a", (305, 449), (1390, 449), 2)
    pygame.draw.line(disp, "#76787a", (305, 486), (1390, 486), 2)
    pygame.draw.line(disp, "#76787a", (305, 523), (1390, 523), 2)
    pygame.draw.line(disp, "#76787a", (305, 560), (1390, 560), 2)
    pygame.draw.line(disp, "#76787a", (305, 597), (1390, 597), 2)
    pygame.draw.line(disp, "#76787a", (305, 634), (1390, 634), 2)
    pygame.draw.line(disp, "#76787a", (305, 671), (1390, 671), 2)
    pygame.draw.line(disp, "#76787a", (305, 708), (1390, 708), 2)


def fiftyOverLimit(disp):
    pygame.draw.line(disp, "#76787a", (532, 5), (532, 740), 2)
    pygame.draw.line(disp, "#76787a", (741, 5), (741, 740), 2)
    pygame.draw.line(disp, "#76787a", (959, 5), (959, 740), 2)
    pygame.draw.line(disp, "#76787a", (1177, 5), (1177, 740), 2)

    pygame.draw.line(disp, "#76787a", (305, 79), (1390, 79), 2)
    pygame.draw.line(disp, "#76787a", (305, 153), (1390, 153), 2)
    pygame.draw.line(disp, "#76787a", (305, 227), (1390, 227), 2)
    pygame.draw.line(disp, "#76787a", (305, 301), (1390, 301), 2)
    pygame.draw.line(disp, "#76787a", (305, 375), (1390, 375), 2)
    pygame.draw.line(disp, "#76787a", (305, 449), (1390, 449), 2)
    pygame.draw.line(disp, "#76787a", (305, 523), (1390, 523), 2)
    pygame.draw.line(disp, "#76787a", (305, 597), (1390, 597), 2)
    pygame.draw.line(disp, "#76787a", (305, 671), (1390, 671), 2)


def twentyOverLimit(disp):
    pygame.draw.line(disp, "#76787a", (849, 5), (849, 740), 2)

    pygame.draw.line(disp, "#76787a", (305, 79), (1390, 79), 2)
    pygame.draw.line(disp, "#76787a", (305, 153), (1390, 153), 2)
    pygame.draw.line(disp, "#76787a", (305, 227), (1390, 227), 2)
    pygame.draw.line(disp, "#76787a", (305, 301), (1390, 301), 2)
    pygame.draw.line(disp, "#76787a", (305, 375), (1390, 375), 2)
    pygame.draw.line(disp, "#76787a", (305, 449), (1390, 449), 2)
    pygame.draw.line(disp, "#76787a", (305, 523), (1390, 523), 2)
    pygame.draw.line(disp, "#76787a", (305, 597), (1390, 597), 2)
    pygame.draw.line(disp, "#76787a", (305, 671), (1390, 671), 2)


def tenOverLimit(disp):
    pygame.draw.line(disp, "#76787a", (305, 79), (1390, 79), 2)
    pygame.draw.line(disp, "#76787a", (305, 153), (1390, 153), 2)
    pygame.draw.line(disp, "#76787a", (305, 227), (1390, 227), 2)
    pygame.draw.line(disp, "#76787a", (305, 301), (1390, 301), 2)
    pygame.draw.line(disp, "#76787a", (305, 375), (1390, 375), 2)
    pygame.draw.line(disp, "#76787a", (305, 449), (1390, 449), 2)
    pygame.draw.line(disp, "#76787a", (305, 523), (1390, 523), 2)
    pygame.draw.line(disp, "#76787a", (305, 597), (1390, 597), 2)
    pygame.draw.line(disp, "#76787a", (305, 671), (1390, 671), 2)

    newFont = pygame.font.Font(None, 30)
    overScores = [[newFont.render((""), True, (255,255,255)) for x in range(10)], [(320, 35 + (74*y)) for y in range(10)]]
    #print(overScores)
    # for i in range(10):
    #     disp.blit(overScores[0][i], overScores[1][i])
    return overScores