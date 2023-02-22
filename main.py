import random
import time

import keyboard


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

    return Game


def good_print(list):
    if(list != [0]):
        addRandom()
        for i in range(4):
            print(list[i])
        print("----------")



Init()

while True:
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