import pygame.transform

moveRect =None
sfruits =None
voiFruits =None
mfruits =None
rootFruits =None

def decmvRect(func):
    def f(*args):
        ele =args[1]
        xm, ym = ele[4]
        p = ele[3]
        x, y = (ele[2][0] * p) + (ele[6] * xm * p), (ele[2][1] * p) + (ele[6] * ym * p)
        return func (*args[:2],(x,y))
    return f

def decmvRectGp(a,b):
    def fa(func):
        def f(*args):
            xm, ym = args[1][4]
            x,y =args[2]
            xn, yn = int(x / a), int(y / a)
            if xm == -1 and xn!=0: xn += 1
            if ym == -1 and yn!=0: yn += 1
            return func(*args[:2],(xn,yn))
        return f
    return fa

def decmvReff(func):
    def f(*args):
        xp,yp =args[1][2]
        g =args[1][3]
        m =args[1][6]
        if  ((yp+m)*g>800):args[1][5]=0
        return func(*args)
    return f


@decmvRect
@decmvReff
def _mvRectEnu(ind,ele,z=None):
    eff=[]
    moveRect[ind][6] += 1
    if moveRect[ind][6] > moveRect[ind][5]: eff.append(ind)
    frt =sfruits[ele[1]].copy()
    frt.set_alpha(220)
    frt=pygame.transform.scale(frt,[90,90])
    ele[0].blit(frt,z)
    return eff

def decmvRect5(func):
    def f(*args):
        print ("----",args[1],"  ======  ",args[2])
        if args[1][5]<args[1][6]:
            ele =args[1]
            xn, yn = args[2]
            if yn>7:return func(*args)
            if args[1][7]==1: voiFruits.append((xn, yn))
            elif type(args[1][7])==type(()):
                mfruits[(args[1][7])]['surf'] =-1
            mfruits[(xn, yn)]['surf'] = ele[1]
            rootFruits.blit(sfruits[ele[1]], (xn * 100, yn * 100))
        return func(*args)
    return f

def decremeGrille(func):
    def f(*args):
        if args[1][7]==2:

            print ('MoveDesc',args[1])
        return func(*args)
    return f

def MoveRect(z=None):
    eff =[]
    for ind,ele in enumerate(moveRect):
        ef =_mvRectEnu(ind,ele)
        if ef!=[]:eff =eff+ef
    return eff

#------------------------------------------------------------------------------
@decmvRect
@decmvRectGp(100,150)
@decmvRect5
def _MoveRectEff(i,ele,z='eeeeee'):
    moveRect.pop(i)

def MoveRectEff(eff,z=None):
    eff.reverse()
    for i in eff:_MoveRectEff(i,moveRect[i])
