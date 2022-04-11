
codeDirect =[(0,-1),(1,0),(0,1),(-1,0)]

def decDIrVoisin(func):
    def f(*args):
        x,y=args[0]
        out=[]
        for ind,ele in enumerate(codeDirect):
            xp,yp=ele
            xn,yn =x+xp,y+yp
            out.append((xn,yn))
        return func(args[0],args[1],out)
    return f

def decFruVoisin(func):
    def f(*args):
        out =[]
        x =func(*args)
        for i in x:
            out.append((args[1][i]['surf']))
        return x,out
    return f

def decIdemVoissin(func):
    def f(*args):
        fs =args[1][args[0]]['surf']
        out =[args[0]]
        if args[2][1].count(fs):
            for ind,ele in enumerate(args[2][1]):
                if ele==fs:out.append(args[2][0][ind])
        if len(out)==1:out=[]
        return func(*args[:2],out)
    return f

@decDIrVoisin
@decFruVoisin
def SimpVoisin(vfs,mfruits,cd=False):
    out =[]
    for ind,ele in enumerate(cd):
        x,y =ele
        if 0<=x<8 and 0<=y<8:out.append((x,y))
    return out

@decIdemVoissin
def IdemVoisin(vfs,mfruits,lvoisin):
    return lvoisin



def Voisin(vF,mfruits,cd=False):
    if vF!=[]:
        for ind,ele in enumerate(vF):
            voisiS=SimpVoisin(ele,mfruits)
            print (IdemVoisin(ele,mfruits,voisiS))