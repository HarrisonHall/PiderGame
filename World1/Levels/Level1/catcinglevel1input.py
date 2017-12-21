# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 16:47:40 2017

@author: Harrison
"""
import catCingLevel1 as thisLevel
import catCingEngine as game



##what user would input and would be parsed through
thisLevel.level1.levelShip.type = "wood"
thisLevel.level1.levelShip.pider1 = "input: color, if color == purple: output == speech2pider4(\"GO\")"
thisLevel.level1.levelShip.bottom.append("pider1")
thisLevel.level1.levelShip.top.append("pider2")

pider1 = game.pider()
pider1.location = "top"
pider2.inputType = "color,1"
outputTo = "pider2, pider3"
outputType = "string"
outputInfo = "(if black, then \"turn\"),(if blue, then \"go\")"
  
    inputType = "string" #string, number, boolean, check(color, height, etc of block x distance away (0 being self) ex. (inputType = "height, 1"))
    inputInfo = "actualInput"
    outputTo = "pider1" #pider, or instrument (self, motor, etc)
    outputType = "string" #string, number, boolean, color, action
    outputInfo = "actualOnput"
    outputType = "string" #string, number, boolean, color, action

pider2 = game.pider()
pider2.location = "bottom"


pider3 = game.pider()
pider3.location = "bottom"

pider5 = game.pider()
