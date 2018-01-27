#piderEngine.py

import copy

class pider():
    def __init__(self, PiderDirectionInputOutput):
        self.directionInputOutput = PiderDirectionInputOutput
    #ex (270,speech.yes,speech.no) (90,true,turn.0)
    #outputs: motor.on, motor.off, turn.0, turn.90, turn.180, turn.270, speech.""
    #inputs: speech."", color.color, height.height

def directionCorrection(shipDirection,direction): #function corrects direction
    if shipDirection == 0 or shipDirection == 360:
        trueDirection = direction - 90
    elif shipDirection == 90:
        trueDirection = direction
    elif shipDirection == 180:
        trueDirection = direction + 90
    else:#shipDirection == 270
        trueDirection = direction + 180

    #corrects trueDirection
    if trueDirection == -90:
        trueDirection = 270
    if trueDirection == 450:
        trueDirection = 90
    if trueDirection == 360:
        trueDirection = 0
    return trueDirection

def findDirectionInputOutput(pider, shipDirection):
        ##Section parses for inputs and outputs
        #direction section
    piderCopy = copy.deepcopy(pider)
    startDirection = piderCopy.directionInputOutput.find("(") + 1
    endDirection = piderCopy.directionInputOutput.find(",") #exclusive value
    directionString = piderCopy.directionInputOutput[startDirection:endDirection]
    direction = int(directionString)
    piderCopy.directionInputOutput = piderCopy.directionInputOutput[(endDirection+1):]
    #input section
    startInput = 0
    endInput = piderCopy.directionInputOutput.find(",") #exclusive value
    Input = piderCopy.directionInputOutput[startInput:endInput]
    piderCopy.directionInputOutput = piderCopy.directionInputOutput[(endInput+1):]
    #output section
    startOutput = 0
    endOutput = piderCopy.directionInputOutput.find(")")
    Output = piderCopy.directionInputOutput[startOutput:endOutput]

    return [direction, Input, Output]

def piderDoStuff(pider,outputArray,speechArray):
    if Output == "motor.off":
        outputArray[0] = "off"
    elif Output == "motor.on":
        outputArray[0] = "on"
    elif Output == "turn.0" or Output == "turn.360": #donothingfor90
        outputArray[1] = directionCorrection(shipDirection,0)
    elif Output == "turn.90":
        outputArray[1] = directionCorrection(shipDirection,90)
    elif Output == "turn.270":
        outputArray[1] = directionCorrection(shipDirection,270)
    elif Output == "turn.180":
        outputArray[1] = directionCorrection(shipDirection,180)
    elif Output[:Output.find(".")] == "speech":
        speechArray.append(Output[Output.find(".")+1:])



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
            elif Output == "turn.0" or Output == "turn.360": #donothingfor90
                outputArray[1] = directionCorrection(shipDirection,0)
            elif Output == "turn.90":
                outputArray[1] = directionCorrection(shipDirection,90)
            elif Output == "turn.270":
                outputArray[1] = directionCorrection(shipDirection,270)
            elif Output == "turn.180":
                outputArray[1] = directionCorrection(shipDirection,180)
            elif Output[:Output.find(".")] == "speech":
                speechArray.append(Output[Output.find(".")+1:])

        else:
            if Input[:Input.find(".")] == "speech":
                speechPidersArray.append(y)
            elif Input[:Input.find(".")] == "color" or Input[:Input.find(".")] == "height":
                sightPidersArray.append(y)

    for x in sightPidersArray:
        direction = findDirectionInputOutput(x, shipDirection)[0]
        realDirection = directionCorrection(shipDirection,direction)
        Input = findDirectionInputOutput(x, shipDirection)[1]
        Output = findDirectionInputOutput(x, shipDirection)[2]
        doOutput = False
        #print(x.__class__.__name__,": direction: ",realDirection)
        if Input[:Input.find(".")] == "height":
            searchHeight = int(Input[(Input.find(".")+1):])
            if realDirection == 0 or realDirection == 360:
                doOutput = (searchHeight == thisLevel.levelMap[yposition][xposition+1])
            elif realDirection == 180:
                doOutput = (searchHeight == thisLevel.levelMap[yposition][xposition-1])
            elif realDirection == 270:
                doOutput = (searchHeight == thisLevel.levelMap[yposition+1][xposition])
            else:
                doOutput = (searchHeight == thisLevel.levelMap[yposition-1][xposition])
        if Input[:Input.find(".")] == "color":
            searchColor = Input[(Input.find(".")+1):].lower()
            if searchColor == "grey":
                searchColor = "gray"
            ##Add dictionary to convert from color to number
            numberToColor = {0 : "blue",
                             1 : "gray",
                             2 : "white",
                             3.1: "sshhh",
                             3.2: "sshhh",
                             3.3: "sshhh",
                             3.4: "sshhh",
                             -1 : "blue",
                             9 : "green"}
            if realDirection == 0 or realDirection == 360:
                doOutput = (searchColor == numberToColor[thisLevel.levelMap[yposition][xposition+1]])
            elif realDirection == 180:
                doOutput = (searchColor == numberToColor[thisLevel.levelMap[yposition][xposition-1]])
            elif realDirection == 270:
                doOutput = (searchColor == numberToColor[thisLevel.levelMap[yposition+1][xposition]])
            else:
                doOutput = (searchColor == numberToColor[thisLevel.levelMap[yposition-1][xposition]])
        
        #print("Do Output? ",doOutput)
        if doOutput == True:
            if Output == "motor.off":
                outputArray[0] = "off"
            elif Output == "motor.on":
                outputArray[0] = "on"
            elif Output == "turn.0" or Output == "turn.360": #donothingfor90
                outputArray[1] = directionCorrection(shipDirection,0)
            elif Output == "turn.90":
                outputArray[1] = directionCorrection(shipDirection,90)
            elif Output == "turn.270":
                outputArray[1] = directionCorrection(shipDirection,270)
            elif Output == "turn.180":
                outputArray[1] = directionCorrection(shipDirection,180)
            elif Output[:Output.find(".")] == "speech":
                speechArray.append(Output[Output.find(".")+1:])

        

    for x in speechPidersArray:
        direction = findDirectionInputOutput(x, shipDirection)[0]
        Input = findDirectionInputOutput(x, shipDirection)[1]
        Output = findDirectionInputOutput(x, shipDirection)[2]
        #print(Input[Input.find("."):])
        if Input[(Input.find(".")+1):] in speechArray:
            if Output == "motor.off":
                outputArray[0] = "off"
            elif Output == "motor.on":
                outputArray[0] = "on"
            elif Output == "turn.0" or Output == "turn.360": #donothingfor90
                outputArray[1] = directionCorrection(shipDirection,0)
            elif Output == "turn.90":
                outputArray[1] = directionCorrection(shipDirection,90)
            elif Output == "turn.270":
                outputArray[1] = directionCorrection(shipDirection,270)
            elif Output == "turn.180":
                outputArray[1] = directionCorrection(shipDirection,180)
            elif Output[:Output.find(".")] == "speech":
                speechArray.append(Output[Output.find(".")+1:])

    #find and run outputs if input is speech and in speechArray**
    #if Output[:Output.find(".")] == "speech":

    #print(speechArray) #Take out after debugging**
    return outputArray #format: [motorOn,direction]
