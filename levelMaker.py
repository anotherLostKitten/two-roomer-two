#0 Procedural Dungeon generation

from random import choice, randrange
from roomMaker import Room

basic = ["exit", "spawn"]
boss = ["boss"]
shop = ["shop"]
enemy = ["enemy1", "benis"]

nogo = { 0 }

class Level():
    """ Level Creation Algo:
        0. Generate dungeon array
        1. populate dungeon with rooms
            a. exit, spawn
            b. boss
            c. shop
            d. <n> enemy rooms
        2. generate maze nodes in empty space
        3. create spanning tree of rooms and maze nodes
        4. add extra connections (?)
        5. remove dead ends in corridor
        6. texture rooms
    """
    def __init__(self, r, c, n):
        # 0
        self.r = r
        self.c = c
        self.spr = -1
        self.spc = -1
        self.dungeon = []
        self.rooms = []
        for i in range(0, r):
            self.dungeon.append([])
            for j in range(0, c):
                self.dungeon[i].append(0)
        # 1a
        for rn in basic:
            if not self.addRoom(rn, 200):
                raise ValueError("Dungeon size too small.")
        # 1b
        if not self.addRoom(choice(boss), 200):
            raise ValueError("Dungeon size too small..")
        # 1c
        if not self.addRoom(choice(shop), 200):
            raise ValueError("Dungeon size too small...")
        # 1d
        for rmrf in range(n):
            self.addRoom(choice(enemy))
        # 2
        for i in range(1, r, 2):
            for j in range(1, c, 2):
                if self.pointFits(i, j):
                    self.dungeon[i][j] = 2
        # 3
        usedRooms = set()
        ssr, ssc = (1,1)
        self.rcons = []
        while ssr < self.c:
            ssc += 2
            if ssc >= self.r:
                ssc = 1
                ssr += 2
            if self.dungeon[ssr][ssc] != 0:
                if self.dungeon[ssr][ssc] == 2:
                    self.dungeon[ssr][ssc] = 1
                    cons = self.pointCons(ssr, ssc)
                else:
                    usedRooms.add(self.dungeon[ssr][ssc])
                    cons = self.roomCons(self.rooms[self.dungeon[ssr][ssc] - 3])
                break
        while len(cons) > 0:
            cons = cons ^ self.connect(choice(tuple(cons)), usedRooms)
        # 4
        
        for cur in self.rcons:
            if randrange(3) == 0:
                if cur[1] % 2 == 0 and self.dungeon[cur[0]][cur[1] + 1] > 0 and self.dungeon[cur[0]][cur[1] - 1] > 0: # --
                    self.dungeon[cur[0]][cur[1]] = 1 if self.dungeon[cur[0]][cur[1] - 1] + self.dungeon[cur[0]][cur[1] + 1] == 2 else 7
                elif self.dungeon[cur[0] + 1][cur[1]] > 0 and self.dungeon[cur[0] - 1][cur[1]] > 0: # |
                    self.dungeon[cur[0]][cur[1]] = 1 if self.dungeon[cur[0] - 1][cur[1]] + self.dungeon[cur[0] + 1][cur[1]] == 2 else 7
        # 5
        for i in range (1, r, 2):
            for j in range(1, c, 2):
                if randrange(201) > 1:
                    self.deadEnd(i, j)
        # 6
        for r in self.rooms:
            if r.name == "spawnRoom":
                self.spr = r.rs + 2
                self.spc = r.cs + 2
            self.fill(r.rs, r.cs, r.full())
        print(self)
    def addRoom(self, roomName, attempts = 50):
        room = Room(roomName)
        for a in range(attempts):
            room.rs = randrange(1, self.r - room.r, 2)
            room.cs = randrange(1, self.c - room.c, 2)
            f = True
            if self.fits(room):
                self.fill(room.rs, room.cs, room.basic(len(self.rooms) + 3))
                self.rooms.append(room)
                return True
        return False
    def pointFits(self, r, c):
        for k in self.rooms:
             if k.rs <= r <= k.rs + k.r and k.cs <= c <= k.cs + k.c:
                 return False
        return True
    def fits(self, room):
        for i in self.rooms:
            if (i.rs <= room.rs <= i.rs + i.r or room.rs <= i.rs <= room.rs + room.r) and (i.cs <= room.cs <= i.cs + i.c or room.cs <= i.cs <= room.cs + room.c):
                return False
        return True
    def fill(self, r, c, ray):
        for i in range(len(ray)):
            for j in range(len(ray[0])):
                self.dungeon[r + i][c + j] = ray[i][j]
    def __str__(self):
        txt = ""
        for i in self.dungeon:
            for j in i:
                txt += '##' if j == 0 else ('  ' if j == 1 else ('>' if j<10 else '') + str(j))
            txt += '\n'
        return txt[:-1]
    def __repr__(self):
        return self.__str__()

    def roomCons(self, room):
        cons = set()
        # ||
        for i in range(room.rs, room.rs + room.r, 2):
            if self.dungeon[i][room.cs] > 0 and room.cs - 2 > 0 and self.dungeon[i][room.cs - 2] > 0:
                cons.add((i, room.cs - 1))
            if self.dungeon[i][room.cs + room.c - 1] > 0 and room.cs + room.c + 1 < self.c and self.dungeon[i][room.cs + room.c + 1] > 0:
                cons.add((i, room.cs + room.c))
        # =
        for i in range(room.cs, room.cs + room.c, 2):
            if self.dungeon[room.rs][i] > 0 and room.rs - 2 > 0 and self.dungeon[room.rs - 2][i] > 0:
                cons.add((room.rs - 1, i))
            if self.dungeon[room.rs + room.r - 1][i] > 0 and room.rs + room.r + 1 < self.r and self.dungeon[room.rs + room.r + 1][i] > 0:
                cons.add((room.rs + room.r, i))
        for i in range(randrange(5)):
            self.rcons.append(choice(tuple(cons)))
        return cons
    def pointCons(self, r, c):
        cons = set()
        for i in range(-1, 2, 2):
            for j in range(2):
                if 0 < r + 2*i*j < self.r and 0 < c + 2*i*(1 - j) < self.c and self.dungeon[r + 2*i*j][c + 2*i*(1 - j)] > 0 and self.dungeon[r][c] > 0:
                    cons.add((r + i*j, c + i*(1 - j)))
        if randrange(30) == 0:
            self.rcons.append(choice(tuple(cons)))
        return cons
    def connect(self, cur, usedRooms):
        if cur[1] % 2 == 0 and self.dungeon[cur[0]][cur[1] + 1] > 0 and self.dungeon[cur[0]][cur[1] - 1] > 0: # --
            self.dungeon[cur[0]][cur[1]] = 1 if self.dungeon[cur[0]][cur[1] - 1] + self.dungeon[cur[0]][cur[1] + 1] == 3 else 7
            if self.dungeon[cur[0]][cur[1] + 1] == 2:
                self.dungeon[cur[0]][cur[1] + 1] = 1
                return self.pointCons(cur[0], cur[1] + 1)
            elif self.dungeon[cur[0]][cur[1] - 1] == 2:
                self.dungeon[cur[0]][cur[1] - 1] = 1
                return self.pointCons(cur[0], cur[1] - 1)
            elif self.dungeon[cur[0]][cur[1] + 1] > 1 and self.dungeon[cur[0]][cur[1] + 1] not in usedRooms:
                usedRooms.add(self.dungeon[cur[0]][cur[1] + 1])
                return self.roomCons(self.rooms[self.dungeon[cur[0]][cur[1] + 1] - 3])
            elif self.dungeon[cur[0]][cur[1] - 1] > 1 and self.dungeon[cur[0]][cur[1] - 1] not in usedRooms:
                usedRooms.add(self.dungeon[cur[0]][cur[1] - 1])
                return self.roomCons(self.rooms[self.dungeon[cur[0]][cur[1] - 1] - 3])
        elif self.dungeon[cur[0] + 1][cur[1]] > 0 and self.dungeon[cur[0] - 1][cur[1]] > 0: # |
            self.dungeon[cur[0]][cur[1]] = 1 if self.dungeon[cur[0] - 1][cur[1]] + self.dungeon[cur[0] + 1][cur[1]] == 3 else 7
            if self.dungeon[cur[0] + 1][cur[1]] == 2:
                self.dungeon[cur[0] + 1][cur[1]] = 1
                return self.pointCons(cur[0] + 1, cur[1])
            elif self.dungeon[cur[0] - 1][cur[1]] == 2:
                self.dungeon[cur[0] - 1][cur[1]] = 1
                return self.pointCons(cur[0] - 1, cur[1])
            elif self.dungeon[cur[0] - 1][cur[1]] > 1 and self.dungeon[cur[0] - 1][cur[1]] not in usedRooms:
                usedRooms.add(self.dungeon[cur[0] - 1][cur[1]])
                return self.roomCons(self.rooms[self.dungeon[cur[0] - 1][cur[1]] - 3])
            elif self.dungeon[cur[0] + 1][cur[1]] > 1 and self.dungeon[cur[0] + 1][cur[1]] not in usedRooms:
                usedRooms.add(self.dungeon[cur[0] + 1][cur[1]])
                return self.roomCons(self.rooms[self.dungeon[cur[0] + 1][cur[1]] - 3])
        return {cur}
    def deadEnd(self, r, c):
        if 0 < r < self.r and 0 < c < self.c and self.dungeon[r][c] == 1 or 7:
            count = 0
            for i in range(-1, 2, 2):
                for j in range(2):
                    if self.dungeon[r + i*j][c + i*(1-j)] not in nogo:
                        nr = r + i*j
                        nc = c + i*(1-j)
                        count += 1
            if count <= 1:
                self.dungeon[r][c] = 0
                if count == 1:
                    self.deadEnd(nr, nc)
                
if __name__ == "__main__":
    a = Level(61,101,100)
    print(a)
