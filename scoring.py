class score(object):
    
    def __init__(self, gameType, maxWickets, maxOvers, wicketRuns, startingRuns, inningsNum, bowlAgain, extraRuns):
    
        self.runs = 0
        self.wickets = 0
        self.overs = 0.0
        
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
        self.maxOvers = maxOvers
        self.wicketRuns = wicketRuns
        self.startingRuns = int(startingRuns)
        self.inningsNum = int(inningsNum)
        self.extraRuns = int(extraRuns)
        
        self.extras = 0
        self.wides = 0
        self.noballs = 0
        self.byes = 0
        self.overScore = 0
        
        self.runs += startingRuns
    
        
    def runsScored(self, runType, runAmount):
        
        if runType == 0:                    # Scored with bat
            self.runs += runAmount
            self.overScore += runAmount
            
        elif runType == 1:                  # Wide, could include byes
            self.runs += runAmount
            self.overScore += runAmount
            self.extras += runAmount
            self.wides += 1
            self.byes += (runAmount - self.self.extraRuns)
            
        elif runType == 2:                  # No ball, could include byes
            self.runs += runAmount
            self.overScore += runAmount
            self.extras += runAmount
            self.noballs += 1
            self.byes += (runAmount - self.self.extraRuns)
            
        elif runType == 3:                  # Byes off a valid delivery
            self.runs += runAmount
            self.overScore += runAmount
            self.extras += runAmount
            self.byes += runAmount
            
        elif runType == 4:                  # Penalty runs, won't go through ballBowled
            self.runs += runAmount
            
            
    def wicketTaken(self):
        self.wickets += 1
        self.runs -= self.wicketRuns
             
                         
    def ballBowled(self, runType, runAmount, wicket):
        if self.gameType == 2:                              # In the Hundred format, overs are 5 balls
            if (runType != 2 and runType != 3) or self.bowlAgain == 1 or (self.bowlAgain == 2 and int(self.overs) != self.maxOvers):
                if (self.overs % 1) == 0.4:
                    self.overs += 0.6
                else:
                    self.overs += 0.1
        else:                                               # 6 ball overs in all other formats
            if (runType != 2 and runType != 3) or self.bowlAgain == 1 or (self.bowlAgain == 2 and int(self.overs) != self.maxOvers):
                if (self.overs % 1) == 0.5:
                    self.overs += 0.5
                else:
                    self.overs += 0.1
        
        if runAmount > 0:
            self.runsScored(runType, runAmount)
        if wicket:
            self.wicketTaken()
            
        return self.inningsDoneCheck()
            
    
    def inningsDoneCheck(self):
        if self.overs > 0 and self.overs == self.maxOvers:
            return True
        elif self.wickets > 0 and self.wickets == self.maxWickets:
            return True
        else:
            return False