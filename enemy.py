# enemy ai and stats
class Enemy():
    def __init__(r, c):
        self.r = r
        self.c = c
        pass
    def path(pancake, level, cur, end):
        if cur == end:
            return True
class P():
    def __init__(c,l):
        self.r = c[0]
        self.c = c[1]
        self.l = l
    def __eq__(self, other):
        return self.r + self.c + self.l == other.r + other.c + other.l
    def __ne__(self, other):
        return self.r + self.c + self.l != other.r + other.c + other.l
    def __lt__(self, other):
        return self.r + self.c + self.l < other.r + other.c + other.l
    def __gt__(self, other):
        return self.r + self.c + self.l > other.r + other.c + other.l
    def __le__(self, other):
        return self.r + self.c + self.l <= other.r + other.c + other.l
    def __ge__(self, other):
        return self.r + self.c + self.l >= other.r + other.c + other.l
    
