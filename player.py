from os import system, name
from random import choice

import pygame
import pygame.locals

from levelMaker import Level
from helpers import *
import skills

nogo = { 0 }
door = 7

class Player:
    def __init__(self):
        self.hp = 10
        self.newLevel()
        self.toAnim = {'a':((1,0),(1,1),(1,-1))}
        self.movs = (pygame.K_ESCAPE, pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_UP, pygame.K_LEFT, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_SPACE, pygame.K_q)
        self.movecd = 0
        self.q = choice(list(skills.q))
        self.qcd = 0
        self.e = choice(list(skills.e))
        self.ecd = 0
    def newLevel(self):
        self.level = Level(45, 101, 100)
        self.r = self.level.spr
        self.c = self.level.spc
        self.fow = [x[:] for x in [[False] * self.level.c] * self.level.r]
        self.discover(self.r, self.c)
        self.rot = 0
    def cdd(self):
        if self.movecd > 0:
            self.movecd -= 1
        if self.qcd > 0:
            self.qcd -= 1
        if self.ecd > 0:
            self.ecd -= 1

    def qg(self):
        if self.qcd == 0:
            d = skills.q[self.q]()
            o = d['o'] if 'o' in d else list(d)
            for i in o:
                cur = d[i]
                if i == 'm':
                    for j in cur:
                        self.movp(j)
                elif i == 'a':
                    for j in cur:
                        self.aadd('a', rc(self.rot, j))
                elif i == 'c':
                    self.qcd = cur
    def aadd(self, t, dc):
        if t not in self.toAnim:
            self.toAnim[t] = ()
        self.toAnim[t] += ((dc[0] + self.r, dc[1] + self.c),)
    def bsc(self, dr):
        if self.movecd == 0:
            self.movecd = 5
            self.move(dr)
    def bscp(self, dr):
        if self.movecd == 0:
            self.movecd = 5
            self.movp(dr)
    def move(self, dr):
        if self.level.dungeon[self.r + dr[0]][self.c + dr[1]] not in nogo:
            self.aadd('m', (0,0))
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
    if mov == pygame.K_ESCAPE:
        return False
    elif mov == pygame.K_w:
        p.bsc((-1,0))
    elif mov == pygame.K_a:
        p.bsc((0,-1))
    elif mov == pygame.K_s:
        p.bsc((1,0))
    elif mov == pygame.K_d:
        p.bsc((0,1))
    elif mov == pygame.K_SPACE:
        p.bscp((1,0))
    elif mov == pygame.K_UP: # arrow keys
        p.rot = 0
    elif mov == pygame.K_LEFT:
        p.rot = 1
    elif mov == pygame.K_DOWN:
        p.rot = 2
    elif mov == pygame.K_RIGHT:
        p.rot = 3
    elif mov == pygame.K_q:
        p.qg()
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
