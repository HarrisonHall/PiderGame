#"World 1 Level 2: The Twisted Icy Sequel" by Harrison Hall

import Engine.levelEngine as levelEngine

thisLevel = levelEngine.level()
thisLevel.levelTitle = "World 1 Level 2: The Twisted Icy Sequel"
thisLevel.levelStartText = "IceBurgs do not sink you, but they do remove a turn by slowing you down. See if you can make this turn."
thisLevel.levelMap = [[1,  1,  1,  1,  1,  1,  1,  1],
                      [1, -1,  0,  0, -1,  1,  9,  1],
                      [1,  0,  0,  0,  0,  1,  0,  1],
                      [1,3.1,  0,  0,3.2,  1,  0,  1],
                      [1,  0,3.3,3.3,  0,  1,  0,  1],
                      [1,  1,  1,  1,  1,  1,  0,  1],
                      [1,  0,  0,  0,  0,  0,  2,  1],
                      [1,  1,  1,  1,  1,  1,  1,  1]]
thisLevel.maxTurns = 10
thisLevel.levelStartOrientation = 0
thisLevel.levelStartPosition = [1,6]

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
