from random import shuffle

def rr(i, rc):
    i %= 4
    return i-1-rc if (i+rc) % 2 == 0 else 0
def rb(i, rc):
    i = (i + 1 - rc) % 4
    return -1 if i < 2 else 1
def rc(i, dp): # converting polar coords to rectangular
    return (dp[0] * rr(i, 0) + dp[1] * rr(i, 1), dp[0] * rr(i-1, 0) + dp[1] * rr(i-1, 1))

class P(): # path length comparison class for pathfinding.
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

def cattack(cord, attacks, rot, level, targets*): # check if location can attack anything in targets
    if 'o' in attacks and 'm' in attacks['o'] and attacks['o'].index('m') < attacks['o'].index('a'):
        for m in attacks['m']:
            tst =  tuple(cord[i] + rc(rot, m)[i] for i in range(2))
            if not cmove(tst, level, targets, e):
                break
            cord = tst
    for t in shuffle(targets):
        for a in attacks['a']:
            if t[0] == rc(rot, a)[1] and t[1] == rc(rot, a)[1]: # TODO account for different sized targets
                return True
    return False
def cmove(cord, level, occupy, noogoo):
    return 0 < cord[0] < level.r and 0 < cord[1] < level.c and level.dungeon[cord[0]][cord[1]] not in noogoo and cord not in occupy
    
    
if __name__ == "__main__":
    print((rr(0, 0), rr(0, 1)))
    print((rr(1, 0), rr(1, 1)))
    print((rr(2, 0), rr(2, 1)))
    print((rr(3, 0), rr(3, 1)))

    print(rc(0, (1, 0)))
    print(rc(1, (1, 0)))
    print(rc(2, (1, 0)))
    print(rc(3, (1, 0)))
    
    print(rc(0, (1, 1)))
    print(rc(1, (1, 1)))
    print(rc(2, (1, 1)))
    print(rc(3, (1, 1)))
