
moveRect =None
sfruits =None
voiFruits =None
mfruits =None
rootFruits =None


def MoveRect(z=None):
    eff =[]
    for ind,ele in enumerate(moveRect):
        xm,ym =ele[4]
        p =ele[3]
        x,y =(ele[2][0]*p)+(ele[6]*xm*p),(ele[2][1]*p)+(ele[6]*ym*p)
        try:
            ele[0].blit(sfruits[ele[1]],(x,y))
        except:eff.append(ind)
        moveRect[ind][6] +=1
        if moveRect[ind][6]>moveRect[ind][5]:eff.append(ind)
    return eff

def MoveRectEff(eff,z=None):
    eff.reverse()
    for i in eff:
        ele =moveRect[i]
        xm, ym = ele[4]
        p = ele[3]
        x, y = (ele[2][0] * p) + (ele[6] * xm * p), (ele[2][1] * p) + (ele[6] * ym * p)
        xn,yn =int(x/100),int(y/100)
        if xm==-1:xn+=1
        if ym == -1: yn += 1
        voiFruits.append((xn,yn))
        try:
            mfruits[(xn,yn)]['surf']=ele[1]
        except:pass
        rootFruits.blit(sfruits[ele[1]],(xn*100,yn*100))
        moveRect.pop(i)

def dd():
    pass