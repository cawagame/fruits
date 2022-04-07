import pygame
from pygame.locals import  *
import os
import random
import threading
import itertools
#------------ voisin
voisinCheck =[]
voisinSuite =[]
voisinGroupe =[]
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
codeDirect =[(0,-1),(1,0),(0,1),(-1,0)]
#-------------- init varaible move fruits
mvRect =[]  #surface, position arriver, postion move, vitesse




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
            mfruits[(x+xp,y+yp)]['alfa'] = 100
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
        rootFruits.blit(sfruits[v['surf']],(x*100,y*100))
        if v["clsE"]:cl=[0,250,250,v['alfa']]
        else:cl=[255,0,0,v['alfa']]
        pygame.draw.rect(rootSelCase,cl,(x*100,y*100,100,100),0)
        #if v['alfa']!=0:print(v)
    root.blit(rootFruits,(0,0))
    root.blit(rootSelCase,(0,0))


def MoveRect():
    ""
    for ind,ele in enumerate(mvRect):
        #print(ele)
        x,y     =ele[1]
        xc,yc   =ele[2]

        x100,y100 =x*100,y*100
        x20,y20 =x100/ele[3],y100/ele[3]
        xm,ym   =x20*20+(20*ele[5])*xc,y20*20+(20*ele[5])*yc
        rootFruitsSel.blit(sfruits[ele[0]],(xm,ym))
        mvRect[ind][5] +=1

    if ele[5]> ele[4]:
        voisinCheck.append(mvRect[0][1])
        voisinCheck.append(mvRect[1][1])

        mfruits[mvRect[1][1]]['surf']=mvRect[0][0]
        mfruits[mvRect[0][1]]['surf'] = mvRect[1][0]
        mfruits[mvRect[1][1]]['alfa'] = 0
        mfruits[mvRect[0][1]]['alfa'] = 0
        mvRect.pop(0)
        mvRect.pop(0)


    root.blit(rootFruitsSel,(0,0))


#*********************** class select case Fruits *************
@dec2Selc
@dec2SelcXY
def Selc2Fruits(z=False):

    return z
def Selc3Case():
    if mouPres != [0,0,0]:return -100
    xy =selFruit[2]
    print (xy,selFruit)
    if xy==10:return 10
    if xy ==-10:
        mfruits[selFruit[0]]['alfa']=0
        selFruit[0] =False
        selFruit[1] = False
        selFruit[2] = False
        return 0
    elif xy==-20:
        print(selFruit)
        mfruits[selFruit[0]]['alfa'] = 0
        selFruit[0] = selFruit[1]
        selFruit[1] = False
        selFruit[2] = False
        return 0


    p0=mfruits[selFruit[0]]['surf']
    p1 = mfruits[selFruit[1]]['surf']

    mfruits[selFruit[0]]['alfa']    = 100
    mfruits[selFruit[1]]['alfa']    = 100
    #print(p1,selFruit[1],xy)
    xyInv=(xy[0]*-1,xy[1]*-1)

    mvRect.append([p0, selFruit[0], xyInv, 20, 5, 0])
    mvRect.append([p1,selFruit[1],xy,20,5,0])
    selFruit[0] = False
    selFruit[1] = False
    selFruit[2] = False

    #print(xy)
    return xy
def VoisinGrille(g):
    out =[]
    for ind,ele in enumerate(g):
        x,y =ele
        print (ele)
        if 0<=x<=7 and 0<=y<=7:out.append(ele)
    return out
def VoisinCode(cdir):
    xv,yv =cdir
    out =[]
    for ind,ele in enumerate(codeDirect):
        xc,yc=ele
        x,y =xv+xc,yv+yc
        out.append((x,y))
    return out
def VoisinFruits(fr0,voisin):
    out  =[]
    sfr =mfruits[fr0]['surf']
    for ind,ele in enumerate(voisin):
        sfrv =mfruits[ele]['surf']
        if sfr==sfrv:out.append(ele)
    return out
def VoisinColor(fr):
    for ind,ele in enumerate(fr):
        mfruits[ele]['alfa'] = 50
        mfruits[ele]['clsE'] = True


def voisin(z=(0,0)):
    global voisinCheck,voisinSuite
    if voisinCheck!=[]:
        voisinSuite =voisinSuite+voisinCheck
        voisinCheck=[]
    out =[]
    for ind,ele in enumerate(voisinSuite):
        v0 =VoisinCode(ele)
        v1 =VoisinGrille(v0)
        v2 =VoisinFruits(ele,v1)
        if v2 !=[]:
            VoisinColor(v2+[ele])
            print (ele,'------')


    voisinSuite=[]





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
        mfruits[(ib,i)]={"surf":gfruits[ifr],"alfa":0,"clsE":False}
        ifr +=1



pygame.init()
root =pygame.display.set_mode([800,800])
rootFruits =pygame.Surface([800,8000], pygame.SRCALPHA, 32)
rootFruits.convert_alpha()
rootFruitsSel =pygame.Surface([800,8000], pygame.SRCALPHA, 32)
rootFruitsSel.convert_alpha()
rootSelCase =pygame.Surface([800,8000], pygame.SRCALPHA, 32)



diimde =[]
while 1:

    if selFruit[2]==10:voisin()
    if selFruit[1]:Selc2Fruits()
    if selFruit[2]:Selc3Case()
    voisin()


    root.fill((255,255,0))
    DisplRect()
    if mvRect!=[]:MoveRect()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    nomFruits=MousePres(pygame.mouse.get_pressed())
    if nomFruits:FruitSelect(nomFruits)
    else:mouPres =[0,0,0]

    pygame.display.update()
    pygame.time.wait(60)



