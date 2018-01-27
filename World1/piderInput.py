import Engine.piderEngine as piderEngine
pider1 = piderEngine.pider("(90,true,motor.on)")
pider2 = piderEngine.pider("(0,color.gray,turn.180)")
pider3 = piderEngine.pider("(90,color.blue,speech.stop)")
pider4 = piderEngine.pider("(0,true,motor.off)")
pider5 = piderEngine.pider("(0,speech.swag,motor.on)")
pider6 = piderEngine.pider("(90,true,nothing)")

piderList = [pider1,pider2,pider3,pider4,pider5,pider6]

