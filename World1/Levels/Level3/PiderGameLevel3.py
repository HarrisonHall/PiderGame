#"World 1 Level 3: Twisty and Turny" by Harrison Hall

import Engine.levelEngine as levelEngine

thisLevel = levelEngine.level()
thisLevel.levelStartText = "Piders can see both color and height of the objects. See if you can make choose to turn."
thisLevel.levelTitle = "World 1 Level 3: Twisty and Turny"
thisLevel.levelMap = [[1,1,1,1,1,1,1],
                      [1,9,1,0,0,0,1],
                      [1,0,1,0,1,0,1],
                      [1,0,1,0,1,0,1],
                      [1,0,1,0,1,0,1],
                      [1,0,1,0,1,0,1],
                      [1,0,1,0,1,0,1],
                      [1,0,0,0,1,0,1],
                      [1,1,1,1,1,1,1]]
thisLevel.maxTurns = 10
thisLevel.levelStartOrientation = 90
thisLevel.levelStartPosition = [5,7]

## Winning Piders:                                                                
'''                                                                               
pider1 = piderEngine.pider("(90,true,motor.on)")                                  
pider2 = piderEngine.pider("(0,color.gray,turn.180)")                                   
pider3 = piderEngine.pider("(180,color.gray,turn.0)")                                   
pider4 = piderEngine.pider("(90,true,nothing)")                                   
pider5 = piderEngine.pider("(90,true,nothing)")                                   
pider6 = piderEngine.pider("(90,true,nothing)")                      
                                                                                  
piderList = [pider1,pider2,pider3,pider4,pider5,pider6] 
'''  
