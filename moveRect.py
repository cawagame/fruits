
mvRect=None


#-----------------------  decoreateur move rec ----------
def decmvRectDisp(func):
    def f(*args):
        print ("movre rect  ", args[0])
        return func (args[0])
    return f

@decmvRectDisp
def MobeRectP1(ind):
    mvRect[ind][5] +=1
    return

def MoveRect():
    eff=[]
    for ind,ele in enumerate(mvRect):
        MobeRectP1(ind)
        if mvRect[ind][5] > mvRect[ind][4]: eff.append(ind)
    eff.reverse()
    for i in eff:
        mvRect.pop(i)