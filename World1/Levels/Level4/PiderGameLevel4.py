# "World 1 Level 4: Whirl Pools are Not Fun Pools" by Harrison Hall

import Engine.levelEngine as levelEngine

thisLevel = levelEngine.level()
thisLevel.levelTitle = "World 1 Level 4: Whirl Pools are Not Fun Pools"
thisLevel.levelStartText = "Whirl Pools kill you. Don't touch 'em"
thisLevel.levelMap = [[1,  1,  1,  1,  1,  1,  1,  1],
                      [1,  0, -1,  0,  0,  0,  0,  1],
                      [1,  0,  0,  0,  0,  1,  0,  1],
                      [1,  0,  0,  0,  1,  1,  0,  1],
                      [1,  1,  0,  0,  0,  1,  0,  1],
                      [1,  0, -1,  0,  0,  0,  0,  1],
                      [1,  1,  1,  1,  0, -1,  0,  1],
                      [1,  9,  0,  0,  0,  0,  0,  1],
                      [1,  1,  1,  1,  1,  1,  1,  1]]
thisLevel.maxTurns = 10
thisLevel.levelStartOrientation = 270
thisLevel.levelStartPosition = [1,1]

## Winning Piders:                                                                
'''                                                                               
pider1 = piderEngine.pider("(90,true,motor.on)")                                  
pider2 = piderEngine.pider("(0,color.gray,turn.180)")                                   
pider3 = piderEngine.pider("(180,height.-1,turn.0)")                                   
pider4 = piderEngine.pider("(0,height.0,turn.0)")                                   
pider5 = piderEngine.pider("(0,height.-1,turn.180)")                                   
pider6 = piderEngine.pider("(90,true,nothing)")                      
                                                                                  
piderList = [pider1,pider2,pider3,pider4,pider5,pider6]   
'''
