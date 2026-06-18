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
        self.maxOvers = maxOvers
        self.wicketRuns = wicketRuns
        self.startingRuns = int(startingRuns)
        self.inningsNum = int(inningsNum)
        self.extraRuns = int(extraRuns)
    
        
