# Reads rooms from file.
from random import randint

nogo = { 0 }

class Room():
    def __init__(self, fileName):
        f = open("rooms/" + fileName + ".room")
        l = f.readlines()
        f.close()
        rotation = randint(0,3)
        self.name = l[0][:-1]
        self.type = l[1][:-1]
        self.r = int(l[2][:l[2].index('x')])
        self.c = int(l[2][l[2].index('x') + 1:-1])
        self.room = [x[:] for x in ([[0] * self.c] * self.r if rotation % 2 == 0 else [[0] * self.r] * self.c)]
        for i in range(self.r):
            e = l[i+3].split(' ')
            for j in range(self.c):
                if rotation == 0:
                    self.room[i][j] = int(e[j])
                elif rotation == 1:
                    self.room[j][self.r-i-1] = int(e[j])
                elif rotation == 2:
                    self.room[self.r - i - 1][self.c - j - 1] = int(e[j])
                else:
                    self.room[self.c - j - 1][i] = int(e[j])
        self.rotation = rotation
        if rotation % 2 == 1:
            tmp = self.r
            self.r = self.c
            self.c = tmp
            
    def __str__(self):
        txt = ""
        for i in self.room:
            for j in i:
                txt += str(j) + ' '
            txt += "\n"
        return txt[:-1]
    def __repr__(self):
        return self.__str__()
    def basic(self, r):
        a = []
        for i in self.room:
            a.append([])
            for j in i:
                a[-1].append(0 if j in nogo else r)
        return a
    def full(self):
        return self.room

if __name__ == "__main__":
    a = Room("enemy1")
    print(a)
    print(a.basic(3))
