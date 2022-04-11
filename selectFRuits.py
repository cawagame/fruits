import pygame
from pygame.locals import  *

mfruits =None
selFruit =None
mvRect =None
rootFruits =None

def decSelCodeM10(func):
    def f(*args):
        if args[0][2] ==-10:
            mfruits[selFruit[0]]['alfa'] = 0
            selFruit[0] = False
            selFruit[1] = False
            selFruit[2] = False
        return func(args[0])
    return f
def decSElCodeM20(func):
    def f(*args):
        if args[0][2]==-20:
            mfruits[selFruit[0]]['alfa'] = 0
            selFruit[0] = selFruit[1]
            selFruit[1] = False
            selFruit[2] = False

        return func(args[0])
    return f



#----------------------- select 2 frurt ------------
def dec2Selc(func):         #calcule la distance des 2 fruits
    def f(*args):
        xa,ya =selFruit[0]
        xb,yb =selFruit[1]
        x,y =xa-xb,ya-yb
        return func ((x,y))
    return f

def dec2SelcXY(func):
    "return -10 -20 list"
    def f(*args):
        x,y = args[0]
        z =abs(x)+abs(y)
        if z==0:selFruit[2]=-10
        elif z>1:selFruit[2]=-20
        else:selFruit[2] =(x,y)
        return func (selFruit[2])
    return f

@dec2Selc
@dec2SelcXY
def Selc2Fruits(z=False):
    return z

@decSelCodeM10
@decSElCodeM20
def Selc3Case(z=selFruit):
    out =False
    if type(selFruit[2])==type(()):
        g   =20 #grille 20
        x0,y0 =selFruit[0]
        x01,y01 =int((x0*100)/g),int((y0*100)/g)
        x1, y1 = selFruit[1]
        x11,y11 =int(x1*100/g),int(y1*100/g)
        xd,yd =selFruit[2]
        xdi,ydi =xd*-1,yd*-1
        out =x0,y0,x1,y1



        mvRect.append([mfruits[selFruit[0]]['surf'],(x01,y01),(xdi,ydi),g,5,0])
        mvRect.append([mfruits[selFruit[1]]['surf'], (x11,y11),selFruit[2],g,5,0])

        mfruits[selFruit[0]]['surf'] = False
        mfruits[selFruit[1]]['surf'] = False
        print (mvRect,"---")
        selFruit[0] =False
        selFruit[1] = False
        selFruit[2] = False
    return out