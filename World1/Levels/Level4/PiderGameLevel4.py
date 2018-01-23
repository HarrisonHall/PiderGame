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
