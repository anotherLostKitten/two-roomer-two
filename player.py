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


    def __str__(self):
        system('clear')
        out = ""
        for r in range(self.level.r):
            for c in range(self.level.c):
                d = '#' if self.level.dungeon[r][c] == 0 else (' ' if self.level.dungeon[r][c] == 1 else str(self.level.dungeon[r][c]))
                out += ('p' if r == self.r and c == self.c else (d if p.fow[r][c] else '?')) + (d if p.fow[r][c] else '?')
            out += '\n'
        return out

def binput(p):
    inputs = {'w', 'a', 's', 'd', 'q'}
    while True:
        mov = input(": ")
        if mov in inputs:
            break
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
if __name__ == "__main__":
    p = Player()
    while(binput(p)):
        print(p)
