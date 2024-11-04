import pygame
import random
import sys
from pygame.locals import*



SCREENWIDTH=626
SCREENHIEGHT=417
BACKGROUND=pygame.image.load('images/images (4).jpeg')
ROCK=pygame.image.load('images/rock.png')
SCISSORS=pygame.image.load('images/cut (1).png')
PAPER=pygame.image.load('images/paper-stationery-with-silhouette.png')
WIN=pygame.image.load('images/download_50.jpg')
LOOSE=pygame.image.load('images/pixil-frame-0.png')
# TIE=pygame.image.load('images/pixil-frame-0 (1).png')
CTURN=pygame.image.load('images/pixil-frame-0 (1).png')
PTURN=pygame.image.load('images/pixil-frame-0 (2).png')


Cchoice=""
Pchoice=""
pap=False
roc=False
sci=False
Cpap=True
Croc=True
# Csci=True
def paper():
    SCREEN.blit(PAPER,(450,150))
def rock():
    SCREEN.blit(ROCK,(450,150))
def scissors():
    SCREEN.blit(SCISSORS,(450,150))

def Cpaper():
    SCREEN.blit(PAPER,(55,150))
def Crock():
    SCREEN.blit(ROCK,(55,150))
def Cscissors():
    SCREEN.blit(SCISSORS,(55,150))
# def newGame():
#     for event in pygame.event.get():
#         if event.type==KEYUP and event.key==K_SPACE:
#             gameLoop()

def gameW():
    global Pchoice,sci,pap,roc,Cchoice
    if Cchoice==Pchoice:
        return None
    if Cchoice=='r':
        if Pchoice=='s':
            return False
        elif Pchoice=='p':
            return True
    elif Cchoice=='p':
        if Pchoice=='r':
            return False
        elif Pchoice=='s':
            return True
    elif Cchoice=='s':
        if Pchoice=='p':
            return False
        elif Pchoice=='r':
            return True
a=random.randint(1,3)

if __name__ == "__main__":
    pygame.init()
    SCREEN=pygame.display.set_mode((SCREENWIDTH,SCREENHIEGHT))


def gameLoop():
    global Pchoice,sci,pap,roc,Cchoice
    while True:
        SCREEN.blit(BACKGROUND,(0,0))
        
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYUP and event.key==K_p:
                pap=True
                Pchoice="p"
            if event.type==KEYUP and event.key==K_r:
                roc=True
                Pchoice="r"
            if event.type==KEYUP and event.key==K_s:
                sci=True
                Pchoice="s"
            if event.type==KEYUP and event.key==K_SPACE:
                gameLoop()
            
        if pap:
            paper()
        elif roc:
            rock()
        elif sci:
            scissors()


        if pap or roc or sci:
            if a==1:
                Cchoice="p"
                Cpaper()
            elif a==2:
                Cchoice="r"
                Crock()
            else:
                Cchoice="s"
                Cscissors()

        SCREEN.blit(CTURN,(60,100))
        SCREEN.blit(PTURN,(450,100))
        b=gameW()
        if b:
            SCREEN.blit(WIN,(230,300))
        elif b==None:
            pass
        else:
            SCREEN.blit(LOOSE,(230,300))
        # newGame()
        # for events in pygame.event.get():
        #     if event.type==KEYUP and event.key==K_SPACE:
        #         gameLoop()
        pygame.display.update()
while True:
    gameLoop()
    gameLoop()
    