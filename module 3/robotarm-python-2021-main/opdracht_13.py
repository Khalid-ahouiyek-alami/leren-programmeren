from RobotArm import RobotArm

robotArm = RobotArm('exercise 13')

# Jouw python instructies zet je vanaf hier:
robotArm = RobotArm()
robotArm.randomLevel(1,7)

# Jouw python instructies zet je vanaf hier:
robotArm.grab()
x = 1
while robotArm.scan() != "":
    for blokken in range(x):
        robotArm.moveRight()
    robotArm.drop()    
    for stappel in range(x):
        robotArm.moveLeft()
    robotArm.grab()
    x = x + 1

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()