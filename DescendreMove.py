
def Descendre(mfruits):
    out =[]
    for ind,ele in enumerate(mfruits):
        if type(mfruits[ele]['surf'])==type(""):
            xe,ye =ele
            x,y =xe,ye+1
            if y<8:
                if mfruits[(x,y)]['surf']==-1:
                    mfruits[(x,y)]['surf']=1
                    out.append(ele)
    return out
