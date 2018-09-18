# Reads rooms from file.


class Room():
    def __init__(self, fileName):
        f = open("rooms/" + fileName + ".room")
        l = f.readlines()
        f.close()
        self.name = l[0][:-1]
        self.type = l[1][:-1]
        self.r = int(l[2][:l[2].index('x')])
        self.c = int(l[2][l[2].index('x') + 1:-1])
        self.room = []
        i = 0
        while(i < self.r):
            self.room.append([])
            for j in l[i + 3][:-1].split(' '):
                self.room[i].append(int(j))
            i+=1
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
        walls = {0}
        a = []
        for i in self.room:
            a.append([])
            for j in i:
                a[-1].append(0 if j in walls else r)
        return a
    def full(self):
        return self.room

