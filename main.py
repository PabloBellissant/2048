#2048 Game, rework in python by Adrilava in february 2023, python 3.10


import random
import time

import keyboard

import pygame
pygame.init()



Game = [[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]

def addRandom():
    if(Game[0].__contains__(0) or Game[1].__contains__(0) or Game[2].__contains__(0) or Game[3].__contains__(0)):
        while True:
            rdm1 = random.randint(0,3)
            rdm2 = random.randint(0,3)
            rdm3 = random.randint(1,2)
            if(Game[rdm1][rdm2] == 0):
                Game[rdm1][rdm2] = rdm3
                break


def Init():
    addRandom()
    good_print(Game)


def calcAll(lst, calc = True):
    for i in range(4):
        if (lst[i] == 0):
            lst.remove(lst[i])
            lst.append(0)
    if(calc == True):
        for i in range(3):
            if(lst[i] == lst[i+1] and lst[i] != 0):
                lst[i] = lst[i]+1
                lst[i+1] = 0
        calcAll(lst, False)
    return lst


def deplace(val, calcul = True):

    #Save Old Value
    oldGame = [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]
    for i in range(4):
        for p in range(4):
            oldGame[i][p] = Game[i][p]



    if(val == 0): # LEFT
        for i in range(4):
            Game[i] = calcAll(Game[i])

    if (val == 1):  # Up
        for i in range(4):
            newLst = calcAll([Game[0][i],Game[1][i],Game[2][i],Game[3][i]])
            for p in range(4):
                Game[p][i] = newLst[p]

    if (val == 2):  # RIGHT
        for i in range(4):
            newLst = calcAll([Game[i][3], Game[i][2], Game[i][1], Game[i][0]])
            newLst = [newLst[3],newLst[2],newLst[1],newLst[0]]

            Game[i] = newLst

    if (val == 3):  # Down
        for i in range(4):
            newLst = calcAll([Game[3][i],Game[2][i],Game[1][i],Game[0][i]])
            for p in range(4):
                Game[3-p][i] = newLst[p]
    if(oldGame == Game): return [0]
    else: return Game


def good_print(list):
    if(list != [0]):
        addRandom()
        for i in range(4):
            print(list[i])
        print("----------")

def DrawNumbers(X,Y,numberCompact):
    listColor = [(238, 228, 218),(237, 224, 200),(242,177,121),(245,149,99),(246,124,95),(246,94,59),(237,207,114),(237,204,97),(237,200,80),(237,197,63),(227,188,53)]
    listWhere = [[10,90,0],[-7,86,0],[-12,70,5],[-14,53,11],[-14,40,14]]

    if(numberCompact > len(listColor)): color = listColor[len(listColor)-1] #Get Color
    else: color = listColor[numberCompact-1]

    if (numberCompact > len(listColor)): size = 38
    else: size = listWhere[len(str(2**numberCompact))-1][1]

    if(numberCompact != 0):
        pygame.draw.rect(screen, color, (58+98*(X-2), 58+98*(Y), 93, 93), 0, 0)
        font = pygame.font.SysFont(None, size)
        img = font.render(str(2**numberCompact), True, (0,0,0))
        screen.blit(img, (100*(X-1)+listWhere[len(str(2**numberCompact))-1][0]-25, 100*(Y+1)+listWhere[len(str(2**numberCompact))-1][2]-25))






Init()

screen = pygame.display.set_mode([500, 500])

# Run
running = True
while running:

    if keyboard.is_pressed("LEFT"):
        good_print(deplace(0))
        while (keyboard.is_pressed("LEFT")): time.sleep(0)

    if keyboard.is_pressed("UP"):
        good_print(deplace(1))
        while(keyboard.is_pressed("UP")): time.sleep(0)

    if keyboard.is_pressed("RIGHT"):
        good_print(deplace(2))
        while(keyboard.is_pressed("RIGHT")): time.sleep(0)

    if keyboard.is_pressed("DOWN"):
        good_print(deplace(3))
        while(keyboard.is_pressed("DOWN")): time.sleep(0)

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with color
    screen.fill((10, 10, 10))



    for i in range(4):
        for p in range(4):
            DrawNumbers(i+2,p,Game[p][i])


    # External Square
    pygame.draw.rect(screen, (187, 173, 160), (50,50,400,400), 10, 10)



    for i in range(3): # Draw lines
        pygame.draw.line(screen, (187,173,160), ((i+1)*100+50, 50),((i+1)*100+50, 449)  , 10) # lines
        pygame.draw.line(screen, (187,173,160), (50, (i+1)*100+50),(449, (i+1)*100+50), 10) #column




    # Flip the display
    pygame.display.flip()

pygame.quit()