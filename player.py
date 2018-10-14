from levelMaker import Level
from os import system, name
nogo = { 0 }
door = 7

class Player:
    def __init__(self):
        self.hp = 10
        self.newLevel()

    def newLevel(self):
        self.level = Level(45, 101, 100)
        self.r = self.level.spr
        self.c = self.level.spc
        self.fow = [x[:] for x in [[False] * self.level.c] * self.level.r]
        self.discover(self.r, self.c)

    def move(self, dr, dc):
         if self.level.dungeon[self.r + dr][self.c + dc] not in nogo:
            self.r += dr
            self.c += dc
            if self.level.dungeon[self.r][self.c] == door:
                self.fow[self.r][self.c] = False
                self.level.dungeon[self.r][self.c] = 1
                self.discover(self.r, self.c)

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
    if mov == 'q':
        return False
    elif mov == 'w':
        p.move(-1, 0)
    elif mov == 'a':
        p.move(0, -1)
    elif mov == 's':
        p.move(1,0)
    elif mov == 'd':
        p.move(0,1)
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
