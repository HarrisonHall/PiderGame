## PiderGame
Physics sim game using automated piders. 

This is a personal project I'll be working on for the next few years. World 1 is approximately 60% complete with a completion date sometime before June 2018. 

## Installation (General)
*Download*

* Press the "Clone or download" button

*Python3*

* Install Python3
* Install pygame for Python3
* Run main.py (ex. Linux: `python3 /World1/main.py`)
* Type `1` for level 1

*Editing Piders*

* Pider files are located in `World1/main.py`
* piderEngine.py explanation:
```Python
class pider():
    def __init__(self, PiderDirectionInputOutput):
        self.directionInputOutput = PiderDirectionInputOutput
    #ex (270,speech.yes,speech.no) (90,true,turn.0)
    #outputs: motor.on, motor.off, turn.0, turn.90, turn.180, turn.270, speech.""
    #inputs: speech."", color.color, height.height
```
* Add `pider_ = piderEngine.pider("(direction,input,output)")` below other piders
* Add `pider_` to list `piderList`, and remove the piders you do not want to use
* Save file, and execute `main.py` in order to see the change


## Dev Plan

1. ~~Add color to piders~~
2. Add animations to ship (probably not going to happen)
3. ~~Add new tiles to tilemap (along with functionality)~~
4. Create 10 levels
  * Keep in debug levels
5. Levelmap

* World1 menu

**Example Code and Execution**

*Example Level File*
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
thisLevel.levelStartPosition = [1,1]
```
*Snip from piderEngine.py*
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
