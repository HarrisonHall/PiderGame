#"World 1 Level 8: " by Harrison Hall

import Engine.levelEngine as levelEngine

thisLevel = levelEngine.level()
thisLevel.levelTitle = "World 1 Level 8:"
thisLevel.levelStartText = ""
thisLevel.levelMap = [[1,  1,  1,  1,  1,  1,  1,  0,  1],
                      [1,  0,  0,  0,  9,  0,  0,  0,  1],
                      [1,  0,  0,  0, -1,  0,  0,  0,  1],
                      [1,  0,  0,  0,  0,  0,  0,  0,  1],
                      [1,  0,  0,  0,  0,  0,  0,  0,  1],
                      [1,  0,  0,  0,  0,  0,  0,  0,  1],
                      [1,  0,  0,  0,  0,  0,  0,  0,  1],
                      [1,  0,  0,  0,  0,  0,  0,  0,  1],
                      [1,  0,  0,  0,  0,  0,  0,  0,  1],
                      [1,  0,  0,  0,  2,  0,  0,  0,  1],
                      [1,  0,  0,  2,  0,  2,  0,  0,  1],
                      [1,  1,  1,  1,  1,  1,  1,  0,  1]]
thisLevel.maxTurns = 6
thisLevel.levelStartOrientation = 90
thisLevel.levelStartPosition = [4,10]
