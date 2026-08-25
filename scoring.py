class score(object):
    
    def __init__(self, gameType, maxWickets, maxOvers, wicketRuns, startingRuns, inningsNum, bowlAgain, extraRuns):
    
        self.runs = 0
        self.wickets = 0
        self.overs = 0
        
        if gameType == "Fixed Wickets":
            self.gameType = 0
        elif gameType == "Fixed Overs":
            self.gameType = 1
        elif gameType == "Hundred":
            self.gameType = 2
            
        if bowlAgain == "Yes":
            self.bowlAgain = 0
        elif bowlAgain == "No":
            self.bowlAgain = 1
        if bowlAgain == "Last Over Only":
            self.bowlAgain = 2
            
        self.maxWickets = maxWickets
        self.maxOvers = maxOvers * 10
        self.wicketRuns = wicketRuns
        self.startingRuns = int(startingRuns)
        self.inningsNum = int(inningsNum)
        self.extraRuns = int(extraRuns)
        
        self.extras = 0
        self.wides = 0
        self.noballs = 0
        self.byes = 0
        self.overScore = 0
        
        self.runs += int(startingRuns)
    
        
    def runsScored(self, runType, runAmount):
        
        if runType == 0:                    # Scored with bat
            self.runs += runAmount
            self.overScore += runAmount
            if runAmount == 0:
                symbol = "."
            else:
                symbol = str(runAmount)
            
        elif runType == 1:                  # Wide
            self.runs += (runAmount + self.extraRuns)
            self.overScore += (runAmount + self.extraRuns)
            self.extras += (runAmount + self.extraRuns)
            self.wides += 1
            if runAmount == 0:
                symbol = "+"
            else:
                symbol = "+" + str(runAmount)
            
        elif runType == 2:                  # No ball with hit
            self.runs += (runAmount + self.extraRuns)
            self.overScore += (runAmount + self.extraRuns)
            self.extras += (runAmount + self.extraRuns)
            self.noballs += 1
            if runAmount == 0:
                symbol = "o"
            else:
                symbol = "o" + str(runAmount)

        elif runType == 3:                  # No ball with byes
            self.runs += (runAmount + self.extraRuns)
            self.overScore += (runAmount + self.extraRuns)
            self.extras += (runAmount + self.extraRuns)
            self.noballs += 1
            self.byes += runAmount
            if runAmount == 0:
                symbol = "o"
            else:
                symbol = "oB" + str(runAmount)
            
        elif runType == 4:                  # Byes off a valid delivery
            self.runs += runAmount
            self.overScore += runAmount
            self.extras += runAmount
            self.byes += runAmount
            symbol = "B" + str(runAmount)
            
        elif runType == 5:                  # Penalty runs, won't go through ballBowled
            self.runs += runAmount
            symbol = "P"

        return symbol
            
            
    def wicketTaken(self):
        self.wickets += 1
        self.runs -= self.wicketRuns
             
                         
    def ballBowled(self, runType, runAmount, wicket):
        newOver = False
        if self.gameType == 2:                              # In the Hundred format, overs are 5 balls
            if (runType != 1 and runType != 2 and runType != 3) or self.bowlAgain == 1 or (self.bowlAgain == 2 and int(self.overs) != self.maxOvers):
                if (self.overs % 10) == 4:
                    self.overs += 6
                    newOver = True
                else:
                    self.overs += 1
        else:                                               # 6 ball overs in all other formats
            if (runType != 1 and runType != 2 and runType != 3) or self.bowlAgain == 1 or (self.bowlAgain == 2 and int(self.overs) != self.maxOvers):
                if (self.overs % 10) == 5:
                    self.overs += 5
                    newOver = True
                else:
                    self.overs += 1
        symbol = self.runsScored(runType, runAmount)
        if wicket:
            self.wicketTaken()
            if symbol == ".":
                symbol = "W"
            else:
                symbol = "W"+symbol
        return symbol, newOver
            
    
    def inningsDoneCheck(self):
        if self.overs > 0 and self.overs == self.maxOvers:
            return True
        elif self.wickets > 0 and self.wickets == self.maxWickets:
            return True
        else:
            return False


    def getScore(self):
        print(str(self.runs) + "/" + str(self.wickets) + " (" + str(self.overs / 10) + ")")