# "World 1 Level 7: The First Challenge" by Harrison Hall

import Engine.levelEngine as levelEngine

thisLevel = levelEngine.level()
thisLevel.levelTitle = "World 1 Level 7: The First Challenge"
thisLevel.levelStartText = "Ha. It only gets harder."
thisLevel.levelMap = [[1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1],
                      [1,  0,  0,  1, -1,  1,  0,  1,  0,  0,  2,  9,  1],
                      [1,  1,  0,  0,  0,  1,  2,  1,  0,  0,  0, -1,  1],
                      [1,3.1,  0,  0,3.2,  1,  0,  2,  0,  0,  0,  2,  1],
                      [1, -1,3.3,3.3,  0,  1,  0,  1,  0,  0,  0,  0,  1],
                      [1,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  1],
                      [1,  1,  1,  1,  0,  0,  0,  1,  0,  0,  0,  0,  1],
                      [1,  0,  0,  0,  2,  0,  0,  2,  0,  0,  0,  0,  1],
                      [1,  0,  0,  0,  0,  1, -1,  1,  0,  0,  0,  0,  1],
                      [1,  0,  0,  0,  0,  1,  0,  1,  0,  0,  0,  0,  1],
                      [1,  0,  0,  0,  0,  1,  0,  1,  0,  0,  0,  0,  1],
                      [1, -1,  0,  0,  0,  1,  0,  1,  0,  0,  0,  0,  1],
                      [1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1]]
thisLevel.maxTurns = 10
thisLevel.levelStartOrientation = 0
thisLevel.levelStartPosition = [1,1]
