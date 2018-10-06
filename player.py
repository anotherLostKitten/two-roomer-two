from levelMaker import Level

nogo = { 0 }
door = 7

class Player:
    def __init__(self):
        self.hp = 10
        self.newLevel()

    def newLevel(self):
        self.level = Level(255, 255, 100)
        self.r = self.level.spr
        self.c = self.level.spc
        self.fow = [[False] * self.level.c] * self.level.r
    def move(self, dr, dc):
         if self.level.dungeon[self.r + dr][self.c + dc] not in nogo:
            self.r += dr
            self.c += dc
            if self.level.dungeon[self.r][self.c] == door:
                self.level.dungeon[self.r][self.c] = 1
