from random import randrange
from heapq import heappush, heappop

from helpers import *
from player import *
import skills

# enemy ai and stats

#    1: +
#       ^ 
# 0: +  e  -
#
#       -

nogoe = { 0, 7 }
class Enemy():
    def __init__(self,fileName):
        f = open("enemies/" + fileName + ".enemy")
        l = f.read().splitlines()
        f.close()
        self.name = l[0]
        self.tier = int(l[1]) # normal, miniboss, boss... for loot generation
        self.sr = int(l[2][:l[2].index('x')])
        self.sc = int(l[2][l[2].index('x') + 1:])
        self.hp = randrange(*(int(i) for i in l[3].split(' ') if i!=""))
        self.attack = randrange(*(int(i) for i in l[4].split(' ') if i!=""))
        self.a = skills.q["basic"]
    def fits(self,r,c,p):
        for i in range(self.sr):
            for j in range(self.sc):
                if p.level.dungeon[r+i][c+j] in nogoe:
                    return True
        self.r = r
        self.c = c
        return False
    def path(self,p):
        pancake = [P(self.r - p.r, self.c - p.c, 0)]
        bancake = {(self.r - p.r, self.c - p.c):None}
        while pancake:
            cur = heappop(pancake)
            for i in range(4):
                tpl = (cur.r+rr(i,0),cur.c+rr(i,1)) #  TODO change for different enemy movve types.
                if tpl not in bancake:
                    bancake[tpl]=(cur.r,cur.c)
                    if p.level.dungeon[tpl[0]+p.r][tpl[1]+p.c] not in nogoe:
                        if tpl==(0,0):
                            return self.bpath(tpl,bancake,(p.r,p.c))
                        heappush(pancake,P(tpl[0],tpl[1],cur.l+1))
    def bpath(self, tpl, bancake, pc):
        t = (tpl[0]+pc[0], tpl[1]+pc[1])
        if t!=(self.r,self.c):
            return self.bpath(bancake[tpl], bancake, pc) + [t] 
        return []
    def cattack(self,p):
        for i in range(4):
            for j in self.a()['a']:

if __name__=="__main__":
    a = Enemy("test")
    p = Player()
    while a.fits(randrange(p.level.r),randrange(p.level.c),p):
        pass
    pth = a.path(p)
    for i in pth:
        p.level.dungeon[i[0]][i[1]] = 5
    print("\n\n\n", p.level)
