import pygame
from pygame.locals import *

import os,random
import MoussePresse
import JfruitsVoisin
import MoveRectS
import DescendreMove
#---------------  init variable de basse
sfruits={}
gfruits =[]
mfruits ={}     #matrix fruits
descMv=[]       #descendre
supfruits =pygame.surface.Surface((100,100))

selFruit =[False,False,False]  #pos sele1,pos sele2, code act
moveRect =[]
voiFruits=[]


def decNomFruits(func):
    def f(*args):
        x=func(*args)
        if x:
            xp,yp =x
            xp0,yp0 =int(xp/100),int(yp/100)
            x=(xp0,yp0)
        return x
    return f




def DisplRect():
    rootFruits.fill((0,0,0,0))
    for ind,ele in  enumerate(mfruits.keys()):
        x,y =ele
        v = mfruits[ele]
        if type(v['surf'])==type(''):
            if v['surf']:rootFruits.blit(sfruits[v['surf']],(x*100,y*100))


@decNomFruits
def MousePre():
    MoussePresse.MousePre()
    if MoussePresse.mouseCodePres==[2,0,10]:
        return pygame.mouse.get_pos()
    return False

def SelFruit2(z=False):
    if selFruit[0] ==False:
        selFruit[0] = z
        pygame.draw.rect(rootSelCase,(255,200,100,100),(z[0]*100,z[1]*100,100,100),0)
    else:
        selFruit[1]=z
        pygame.draw.rect(rootSelCase, (255, 200, 150, 100), (z[0] * 100, z[1] * 100, 100, 100), 0)

    if selFruit[1]:
        x0,y0 =selFruit[0]
        x1,y1 =selFruit[1]
        x,y =x0-x1,y0-y1
        xy =abs(x)+abs(y)
        g=20
        if xy==1:
            rootSelCase.fill((0, 0, 0, 0))
            z = selFruit[0]
            pygame.draw.rect(rootFruits, (0, 200, 150, 255), (z[0] * 100, z[1] * 100, 100, 100), 0)
            xp,yp =int(x0*100/g),int(y0*100/g)
            moveRect.append([rootSelMv,mfruits[z]['surf'],(xp,yp),g,(x1-x0,y1-y0),5,0,1])
            mfruits[z]['surf'] = 0

            z = selFruit[1]
            xp, yp = int(x1 * 100 / g), int(y1 * 100 / g)
            moveRect.append([rootSelMv,mfruits[z]['surf'],(xp, yp), g, (x, y), 5, 0,1])
            pygame.draw.rect(rootFruits, (0, 200, 150, 255), (z[0] * 100, z[1] * 100, 100, 100), 0)
            mfruits[z]['surf'] = 0
            selFruit[0] = False
            selFruit[1] = False
            selFruit[2] = False

        elif xy ==0:
            rootSelCase.fill((0,0,0,0))
            selFruit[0] =False
            selFruit[1] =False
            selFruit[2] =False
        else:
            rootSelCase.fill((0,0,0,0))
            z = selFruit[1]
            selFruit[0] = selFruit[1]
            selFruit[1] = False
            selFruit[2] = False
            pygame.draw.rect(rootSelCase, (255, 200, 100, 100), (z[0] * 100, z[1] * 100, 100, 100), 0)
    return selFruit


def Voissin():
    lesVoissin=JfruitsVoisin.Voisin(voiFruits, mfruits)
    if lesVoissin!=[]:
        for ide,ele in enumerate(lesVoissin):
            x,y =ele
            z=ele
            g =10
            xp,yp =int(x*100/g),int(y*100/g)
            pygame.draw.rect(rootSelCase,(125,125,255,130),(x*100,y*100,100,100),0)

            pygame.draw.rect(rootFruits,(12,150,12),(x*100,y*100,100,100),0)
            moveRect.append([rootSelMv, mfruits[z]['surf'], (xp, yp), g, (0,1), 100000, 0,0])
            mfruits[z]['surf'] = -1

def MoveRecst():
    MoveRectS.moveRect = moveRect
    MoveRectS.sfruits = sfruits
    MoveRectS.voiFruits = voiFruits
    MoveRectS.mfruits = mfruits
    MoveRectS.rootFruits = rootFruits
    eff=MoveRectS.MoveRect()
    if eff!=[]:DisplRect()
    MoveRectS.MoveRectEff(eff,None)

def Descandre():
    rootSelDesc.fill((0,0,0,0))
    descMv = DescendreMove.Descendre(mfruits)

    g=50

    for ind,ele in enumerate(descMv):
        print (ele)
        x0, y0 = ele
        xp, yp = int(x0 * 100 / g), int(y0 * 100 / g)
        moveRect.append([rootSelDesc,mfruits[ele]['surf'],(xp,yp),g,(0,1),2,0,ele])   #ind 7  0 no voisin   1 voissin 2 no voisin remets sur la grille
        mfruits[ele]['surf'] = 2

    descMv=[]


#--------------- chargement les image en surface
lfruits =os.listdir("fruits")               #liste image fruits
for ind,ele in enumerate(lfruits):          #load les images en surface
    sfruits[ele] =pygame.image.load("fruits/"+ele)


#--------------- cress la grill 8*8=64
for i in range(64):
    gfruits.append(random.choice(lfruits))


#------------- metres dans la matrice fruits
ifr=0
for i in range (8):
    for ib in range(8):
        mfruits[(ib,i)]={"surf":gfruits[ifr],"alfa":0,"clsE":False,'pos':(ib,i)}
        ifr +=1

pygame.init()
root =pygame.display.set_mode([800,800])                            #maitre
rootCl  =(0,255,200)

rootFruits =pygame.Surface([800,8000], pygame.SRCALPHA, 32)         #mfruirs
rootFruits.convert_alpha()

rootSelCase =pygame.Surface([800,8000], pygame.SRCALPHA, 32)
rootSelCase.convert_alpha()

rootSelMv =pygame.Surface([800,8000], pygame.SRCALPHA, 32)
rootSelMv.convert_alpha()

rootSelDesc =pygame.Surface([800,8000], pygame.SRCALPHA, 32)
rootSelDesc.convert_alpha()

DisplRect()

while 1:
    root.fill((0,150,150))
    rootSelMv.fill((0,0,0,0))

    Voissin()
    voiFruits=[]
    MoveRecst()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    nomF =MousePre()
    if nomF:SelFruit2(nomF)


    root.blit(rootFruits,(0,0))
    root.blit(rootSelCase,(0,0))
    root.blit(rootSelMv,(0,0))
    root.blit(rootSelDesc,(0,0))

    Descandre()
    pygame.display.update()
    pygame.time.wait(60)