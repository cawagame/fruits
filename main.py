import pygame
from pygame.locals import  *
import os
import random
import itertools

#-----------------  appuits Simple
mouPres=[0,0,0]

#--------------- selct fruits
selFruit =[False,False,False]  #pos sele1,pos sele2, code act
selDepla ={}


#---------------  init variable de basse
sfruits={}
gfruits =[]
mfruits ={}     #matrix fruits
supfruits =pygame.surface.Surface((100,100))


#----------------------- select 2 frurt ------------
def dec2Selc(func):         #calcule la distance des 2 fruits
    def f(*args):
        xa,ya =selFruit[0]
        xb,yb =selFruit[1]
        x,y =xa-xb,ya-yb
        return func ((x,y))
    return f

def dec2SelcXY(func):
    def f(*args):
        x,y = args[0]
        z =abs(x)+abs(y)
        if z==0:selFruit[2]=-10
        elif z>1:selFruit[2]=-20
        else:selFruit[2] =(x,y)
        return func (args[0])
    return f


#------------------------  decorateur --------------
def decnomFruits(func):
    def f(*args):
        out =False
        x =func(*args)
        if x:out =x
        return out
    return f


def decalfa100(func):
    def f(*args):
        for ind, ele in enumerate(mfruits.keys()):
            mfruits[ele]['alfa'] = 100
        return func(args[0])
    return f

def decSelFruits(func):
    def f(*args):
        if selFruit[0] and mouPres[0]==1:selFruit[1] =args[0]
        elif not selFruit[0] and mouPres[0]==1:selFruit[0]=args[0]
        return func(args[0])
    return f




#------------------------ decorateir parametres
def decmousePres(pr):
    def dec(func):
        def f(*args):
            if type(args[0]) ==type(10):
                return func(args[0])
            out = args[0]
            if args[0][pr]==True:
                mouPres[pr] +=1
                out=pr
            return func(out)
        return f
    return dec

def declfaxx(alfa,posM):
    def dec(func):
        def f(*args):
            x,y =args[0]
            xp,yp =posM
            mfruits[(x+xp,y+yp)]['alfa'] = alfa
            return func(args[0])
        return f
    return dec


#*********************** class mouse pressed  *************
@decmousePres(2)
@decmousePres(0)
@decnomFruits   #return
def MousePres(pr:tuple=None):
    out =False
    if type(pr)==type(10):
        x,y =pygame.mouse.get_pos()
        out =(int(x/100),int(y/100))
    return out

#*********************** class select alpha case Fruits *************
@declfaxx(100,(0,0))
@decSelFruits
def FruitSelect(nomfruit:tuple=False):
    return nomfruit

#*********************** class display Fruits *************
def DisplRect():
    for ind,ele in  enumerate(mfruits.keys()):
        x,y =ele
        v = mfruits[ele]
        supfruits.blit(sfruits[v['surf']],(0,0))
        supfruits.set_alpha(v['alfa'])
        root.blit(supfruits,(x*100,y*100))

#*********************** class select case Fruits *************
@dec2Selc
@dec2SelcXY
def Selc2Fruits(z=False):
    return z
def Selc3Case():
    if mouPres != [0,0,0]:return -100
    xy =selFruit[2]
    if xy ==-10:
        mfruits[selFruit[0]]['alfa']=255
        selFruit[0] =False
        selFruit[1] = False
        selFruit[2] = False
        return 0
    elif xy==-20:
        mfruits[selFruit[0]]['alfa'] = 255
        selFruit[0] = selFruit[1]
        selFruit[1] = False
        selFruit[2] = False
        return 0

    x,y =xy
    if x==0 and y==1:
        p0=mfruits[selFruit[0]]['surf']
        p1 = mfruits[selFruit[1]]['surf']
        mfruits[selFruit[0]]['surf']    =p1
        mfruits[selFruit[1]]['surf'] = p0

        mfruits[selFruit[0]]['alfa'] = 255
        mfruits[selFruit[1]]['alfa'] = 255
        selFruit[0] = False
        selFruit[1] = False
        selFruit[2] = False


    return xy





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
        mfruits[(ib,i)]={"surf":gfruits[ifr],"alfa":255}
        ifr +=1



pygame.init()
root =pygame.display.set_mode([800,800])



diimde =[]
while 1:
    if selFruit[1]:Selc2Fruits()
    if selFruit[2]:Selc3Case()
    root.fill((0,0,0))
    DisplRect()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    nomFruits=MousePres(pygame.mouse.get_pressed())
    if nomFruits:FruitSelect(nomFruits)
    else:mouPres =[0,0,0]



    pygame.display.update()
    pygame.time.wait(60)



