
from math import cos, pi, sin, sqrt
from random import random
import pygame

pygame.init()

#function naming

def newPointGen (start, length):
    theta = random() * pi
    newPointX = start[0] + (cos(theta) * length)
    newPointY = start[1] + (sin(theta) * length)
    return [newPointX, newPointY]


# variable initializations

animate = False

screenWidth = 1000
screenHeight = 600

dt = 200      #in milliseconds

screen_size = [ screenWidth, screenHeight]

screen = pygame.display.set_mode(screen_size)



restart = False



lineStartX = screenWidth/2
lineStartY = 0
startPoint = [lineStartX, lineStartY]

boltColor = (250, 250, 0)

maxLength = 100

lengthMulti = 90

boltStrength = screenWidth/100

grounded = False

allPoints = [startPoint]


Nbldgs = 30
cityPts = [[screenWidth, screenHeight], [0, screenHeight]]
cityColor = [150, 150, 150]
bldgWidth = screenWidth/Nbldgs
bldgHeight = screenHeight/ 7
for i in range(Nbldgs + 1):
    cityPts.append([ i * bldgWidth, screenHeight - (random() * bldgHeight) - screenHeight/10])




pygame.event.get()
keys = pygame.key.get_pressed()

if keys[pygame.K_f]:
    pygame.display.quit()
    pygame.display.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

while (keys[pygame.K_q] != True):
    pygame.event.get()
    keys = pygame.key.get_pressed()

    if (keys[pygame.K_SPACE]) or (animate == True):

        if(grounded == True):
            restart = True

        mainLength = random() * lengthMulti + (maxLength - lengthMulti)

        endPoint = newPointGen(startPoint, mainLength)

        for bldg in range(1, len(cityPts) -1):
            i = cityPts[bldg]
            hypo = sqrt(((startPoint[0] - i[0]) ** 2) + ((startPoint[1] - i[1]) ** 2))
            if (hypo <= mainLength):
                endPoint = i
                grounded = True
                break
            

        allPoints.append(endPoint)

        pygame.draw.polygon(screen, (0, 0, 0), [(0, 0), (screenWidth, 0), (screenWidth, screenHeight), (0, screenHeight)], 0)

        for i in range(len(allPoints)-2):
            pygame.draw.line(screen, boltColor, allPoints[i], allPoints[i+1], boltStrength)
            boltStrength = int(boltStrength * 0.9)
            if(boltStrength <= 2):
                boltStrength = 2

        boltStrength = 10

        pygame.draw.circle(screen, boltColor, startPoint, mainLength, 2)

        startPoint = endPoint


        pygame.draw.polygon(screen, cityColor, cityPts, 0)

    
        pygame.time.delay(dt)

    if (allPoints[len(allPoints) - 1][1] > screenHeight or restart == True):
        startPoint = [screenWidth/2, 0]
        allPoints = [startPoint]
        cityPts = [(screenWidth, screenHeight), (0, screenHeight)]
        for i in range(Nbldgs + 1):
            cityPts.append([ i * bldgWidth, screenHeight - (random() * bldgHeight) - screenHeight/10])
        grounded = False
        restart = False

# displays
    pygame.display.update()