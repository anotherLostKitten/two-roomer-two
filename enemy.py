from helpers import *
from player import *
from heapq import *
# enemy ai and stats
nogoe = { 0 }
class Enemy():
    def __init__(self,r, c):
        self.r = r
        self.c = c
        pass
    def path(self,p):
        pancake = [P(self.r - p.r, self.c - p.c, 0)]
        bancake = {(self.r - p.r, self.c - p.c):None}
        while pancake:
            cur = heappop(pancake)
            for i in range(4):
                tpl = (cur.r+rr(i,0),cur.c+rr(i,1))
                if tpl not in bancake:
                    bancake[tpl]=(cur.r,cur.c)
                    if p.level.dungeon[tpl[0]+p.r][tpl[1]+p.c] not in nogoe:
                        if tpl==(0,0):
                            print(bancake)
                            return self.bpath(tpl,bancake,(p.r,p.c))
                        heappush(pancake,P(tpl[0],tpl[1],cur.l+1))
    def bpath(self, tpl, bancake, pc):
        t = (tpl[0]+pc[0], tpl[1]+pc[1])
        print(t)
        if t!=(self.r,self.c):
            return self.bpath(bancake[tpl], bancake, pc) + [t] 
        return []
class P():
    def __init__(self,r,c,l):
        self.r = r
        self.c = c
        self.l = l
    def __eq__(self, other):
        return abs(self.r) + abs(self.c) + self.l == abs(other.r) + abs(other.c) + other.l
    def __ne__(self, other):
        return abs(self.r) + abs(self.c) + self.l != abs(other.r) + abs(other.c) + other.l
    def __lt__(self, other):
        return abs(self.r) + abs(self.c) + self.l < abs(other.r) + abs(other.c) + other.l
    def __gt__(self, other):
        return abs(self.r) + abs(self.c) + self.l > abs(other.r) + abs(other.c) + other.l
    def __le__(self, other):
        return abs(self.r) + abs(self.c) + self.l <= abs(other.r) + abs(other.c) + other.l
    def __ge__(self, other):
        return abs(self.r) + abs(self.c) + self.l >= abs(other.r) + abs(other.c) + other.l
    
if __name__=="__main__":
    a = Enemy(1,1)
    p = Player()
    print(a.path(p))
