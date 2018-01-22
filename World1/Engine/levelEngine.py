#levelEngine.py

class level(): #filled in values are defaults
    levelStartText = ""
    levelTitle = ""
    levelMap =[[1,1,1,1],
               [1,0,0,1],
               [1,0,9,1],
               [1,1,1,1]]
    levelStartPosition = [1,1] #position starts at top left
    currentPosition = levelStartPosition #x,y or row,column
    levelStartOrientation = 0
    unlocked = []
    maxTurns = 10
