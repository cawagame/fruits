import pygame
from pygame.locals import  *
import os
import random

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

#------------------------ decorateir parametres
def decmousePres(pr):
    def dec(func):
        def f(*args):
            if type(args[0]) ==type(10):return func(args[0])
            out = args[0]
            if args[0][pr]==True:out=pr
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

#------------------------ class ---------------
@decmousePres(2)
@decmousePres(0)
@decnomFruits
def MousePres(pr:tuple=None):
    out =False
    if type(pr)==type(10):
        x,y =pygame.mouse.get_pos()
        out =(int(x/100),int(y/100))
    return out

@decalfa100
@declfaxx(200,(0,-1))
@declfaxx(200,(1,0))
@declfaxx(200,(0,1))
@declfaxx(200,(-1,0))
@declfaxx(250,(0,0))
def FruitSelect(nomfruit:tuple=False):
    return nomfruit




def DisplRect():
    for ind,ele in  enumerate(mfruits.keys()):
        x,y =ele
        v = mfruits[ele]
        supfruits.blit(sfruits[v['surf']],(0,0))
        supfruits.set_alpha(v['alfa'])
        root.blit(supfruits,(x*100,y*100))


#---------------  init variable de basse
sfruits={}
gfruits =[]
mfruits ={}
supfruits =pygame.surface.Surface((100,100))
#--------------- chargement les image en surface
lfruits =os.listdir("fruits")

for ind,ele in enumerate(lfruits):
    sfruits[ele] =pygame.image.load("fruits/"+ele)
#cress la grill 8*8=64  64/2=32

for i in range(32):
    gfruits.append(random.choice(lfruits))
gfruits =gfruits+gfruits #les doubles

ifr=0
for i in range (8):
    for ib in range(8):
        mfruits[(ib,i)]={"surf":gfruits[ifr],"alfa":255}
        ifr +=1


pygame.init()
root =pygame.display.set_mode([800,800])



diimde =[]
while 1:
    root.fill((0,0,0))
    DisplRect()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    nomFruits=MousePres(pygame.mouse.get_pressed())
    if nomFruits:FruitSelect(nomFruits)


    pygame.display.update()
    pygame.time.wait(60)



