class Animate():
    def __init__(self, cord, textureList, frame, repeat):
        self.cord = cord
        self.textureList = textureList
        self.frame = frame
        self.repeat = repeat
    def nxt(self):
        if self.frame == len(self.textureList):
            self.frame %= len(self.textureList)
            if self.repeat == 0:
                return None
            self.repeat -= 1
        self.frame += 1
        return self.textureList[self.frame - 1]
