import pygame
from pygame.locals import *
mouseCodePres =[False,-1,10]


def MousePre():
    mousPr =pygame.mouse.get_pressed(5)
    if mousPr.count(True):
        tt=0
        for ind,ele in enumerate(mousPr):
            if ele:tt=tt+2**(ind+1)
        if mouseCodePres[0]!=tt:
            mouseCodePres[0]=tt
            mouseCodePres[1]=0
        else:
            mouseCodePres[1]+=1
        if mouseCodePres[1]>mouseCodePres[2]:mouseCodePres[1]=1
    else:
        mouseCodePres[0]=False
        mouseCodePres[1]=-1

