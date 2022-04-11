
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
        out =[]
        if args[2][1].count(fs):
            for ind,ele in enumerate(args[2][1]):
                if ele==fs:out.append(args[2][0][ind])
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
def IdemVoisin(vfs,mfruits,lvoisin=[]):
    return lvoisin

def BouclVoisin(c0,mfruits):
    outV =[c0]
    i =0
    while 1:
        cible =outV[i]
        vs =SimpVoisin(cible,mfruits)
        vt =IdemVoisin(cible,mfruits,vs)
        for ind,ele in enumerate(vt):
            if outV.count(ele) ==0:outV.append(ele)
        i+=1
        if i>len(outV)-1:break
    return outV



def Voisin(vF,mfruits,cd=False):
    outV0 =[]
    outV1 =[]
    if vF!=[]:
        for ind,ele in enumerate(vF):
            out =BouclVoisin(ele,mfruits)
            if len(out)==1:out =[False]
            outV0.append(out)
        for ind,ele in enumerate(outV0):
            for ind0,ele0 in enumerate(ele):
                if outV1.count(ele0)==0:
                    if ele0:outV1.append(ele0)
    return outV1

            #voisiS=SimpVoisin(ele,mfruits)
            #print (IdemVoisin(ele,mfruits,voisiS))