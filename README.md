## PiderGame
Physics sim game using automated piders. 

This is a personal project I'll be working on for the next few years. 

Update 4.

**Dev Plan**

1. Add color to piders
2. Add animations to ship
3. Add new tiles to tilemap (along with functionality)
4. Create 10 levels
  * Keep in debug levels
5. Levelmap

* World1 menu

*Example Code and Execution*
```Python
#"Ship Kingdom: 2" by Harrison Hall
#import numpy as np

import Engine.levelEngine as levelEngine

thisLevel = levelEngine.level()
thisLevel.levelStartText = "Debug1: You have unlocked boats: small and wooden, motor: manual, pider: color, height."
#level1.unlocked.append("wood", "small", "manual", "color", "height")
thisLevel.levelMap = [[1,1,1,1,1,1,1,1],
                      [1,0,1,0,0,0,1,1],
                      [1,0,1,0,1,0,0,1],
                      [1,0,1,0,1,0,0,1],
                      [1,0,1,0,1,0,0,1],
                      [1,0,1,0,1,0,0,1],
                      [1,0,1,0,1,0,0,1],
                      [1,0,0,0,1,9,0,1],
                      [1,1,1,1,1,1,1,1]]
#level1.levelStartPosition = [0, 0]
thisLevel.maxTurns = 10
thisLevel.levelStartOrientation = 270
thisLevel.levelStartPosition = [1,1]```
```Python
def piderCommands(piderList,shipDirection,thisLevel,xposition,yposition): #Add and position*
    runningPiderList = copy.deepcopy(piderList)
    speechArray = []
    outputArray = ["off",shipDirection] #[motorOn,direction]
    sightPidersArray = []
    speechPidersArray = []

    for x in runningPiderList:
        direction = findDirectionInputOutput(x, shipDirection)[0]
        y = copy.deepcopy(x)
        Input = findDirectionInputOutput(x, shipDirection)[1]
        Output = findDirectionInputOutput(x, shipDirection)[2]

        ##Section runs outputs if input is "true" (and does other inputs)
        ##else sends to runOutputsAgain
        if Input == "true":
            if Output == "motor.off":
                outputArray[0] = "off"
            elif Output == "motor.on":
                outputArray[0] = "on"
```
[//]: #![code1](/ExampleFiles/code1.png)
[//]: #![code2](/ExampleFiles/code2.png)
![Game Output](/ExampleFiles/Level2.png)



**The rest are doodles while I learn github**

```Python
pider5 = piderEngine.pider("0,true,motor.on")

print("Cool yo")

```

`This` is in code.

[Link me boss]("https://www.google.com")
