from levelMaker import Level
from random import choice
from helpers import *
from skills import *
from os import system, name
nogo = { 0 }
door = 7

class Player:
    def __init__(self):
        self.hp = 10
        self.newLevel()
        self.toAnim = {'a':((1,0),(1,1),(1,-1))}
    def newLevel(self):
        self.level = Level(45, 101, 100)
        self.r = self.level.spr
        self.c = self.level.spc
        self.fow = [x[:] for x in [[False] * self.level.c] * self.level.r]
        self.discover(self.r, self.c)
        self.rot = 0
        self.sp = choice(list(sp))
    def move(self, dr):
        if self.level.dungeon[self.r + dr[0]][self.c + dr[1]] not in nogo:
            self.r += dr[0]
            self.c += dr[1]
            if self.level.dungeon[self.r][self.c] == door:
                self.fow[self.r][self.c] = False
                self.level.dungeon[self.r][self.c] = 1
                self.discover(self.r, self.c)
    def movp(self, dp):
        self.move(rc(self.rot, dp))
    def discover(self, r, c):
        if not self.fow[r][c]:
            self.fow[r][c] = True
            if self.level.dungeon[r][c] != door and self.level.dungeon[r][c] not in nogo:
                for i in range(-1,2):
                    for j in range(-1,2):
                        self.discover(r + i, c + j)

    def pbox(self, r):
        out = [x[:] for x in [[-1] * (2 * r + 1)] * (2 * r + 1)]
        for i in range(self.r, self.r + 2 * r + 1):
            for j in range(self.c, self.c + 2 * r + 1):
                if -1 < i - r < self.level.r and -1 < j - r < self.level.c and self.fow[i - r][j - r]:
                    out[i - self.r][j - self.c] = self.level.dungeon[i - r][j - r]
        return out
    def __str__(self):
        system('clear')
        out = ""
        for r in range(self.level.r):
            for c in range(self.level.c):
                d = '#' if self.level.dungeon[r][c] == 0 else (' ' if self.level.dungeon[r][c] == 1 else str(self.level.dungeon[r][c]))
                out += ('p' if r == self.r and c == self.c else (d if self.fow[r][c] else '?')) + (d if self.fow[r][c] else '?')
            out += '\n'
        return out

def binput(p, mov):
    if mov == chr(27):
        return False
    elif mov == 'w':
        p.move((-1,0))
    elif mov == 'a':
        p.move((0,-1))
    elif mov == 's':
        p.move((1,0))
    elif mov == 'd':
        p.move((0,1))
    elif mov == ' ':
        p.movp((1,0))
    elif mov == chr(273): # arrow keys
        p.rot = 0
    elif mov == chr(276):
        p.rot = 1
    elif mov == chr(274):
        p.rot = 2
    elif mov == chr(275):
        p.rot = 3
    return True
def ppox(pboc):
    system('clear')
    pr = int((len(pboc) - 1) / 2)
    out = ""
    pboc[pr][pr] = 'p'
    for r in pboc:
        for c in r:
            d = '#' if c == 0 else (' ' if c == 1 else str(c))
            out += (d if c != -1 else '?') + (d if c != -1 else '?')
        out += '\n'
    return out

if __name__ == "__main__":
    p = Player()
    while(binput(p)):
        print(ppox(p.pbox(10)))
