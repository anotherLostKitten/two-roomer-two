import pygame
import pygame.locals
from helpers import *
from animate import Animate
from display import get_textures

rtypes={"basic", "shop", "enemy", "loot"}
walls = get_textures("walls")
door = get_textures("door")
player = get_textures("pp_hed")
dictadd = ('a', 'm')
animdict = { i: get_textures(i) for i in dictadd }

movs = (pygame.K_ESCAPE, pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_UP, pygame.K_LEFT, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_SPACE)

class Room():
    def __init__(self, name, rtype, r, c, etc):
        self.name = name
        self.type = rtype
        self.r = r if r > c else c
        self.c = c if r > c else r
        self.room = [x[:] for x in ([[0] * self.c] * self.r)]
        self.etc = etc
        self.cr = self.cc = 0
    def __str__(self):
        txt = "" + self.name + "\n" + self.type + "\n" + str(self.r) + "x" + str(self.c) + "\n"
        for i in self.room:
            for j in i:
                txt += str(j) + ' '
            txt += "\n"
        return txt + "\n" + self.etc if len(etc) > 0 else txt
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

def render_wall(p, r, c, s, x, y):
    for i in range(4):
        if 0 <= r + rr(i,0) < p.r and 0 <= c + rr(i, 1) < p.c and p.room[r + rr(i,0)][c + rr(i,1)] != 0:
            s.blit(pygame.transform.rotate(walls[1], 90 * i - 90), (x, y))
    for i in range(4):
        if 0 <= r + rb(i, 0) < p.r and 0 <= c + rb(i, 1) < p.c:
            if p.room[r + rr(i, 0)][c + rr(i, 1)] !=0 and p.room[r + rr(i + 1, 0)][c + rr(i + 1, 1)] != 0:
                s.blit(pygame.transform.rotate(walls[2], 90 * i), (x, y))
            if p.room[r + rr(i, 0)][c + rr(i, 1)] == p.room[r + rr(i + 1, 0)][c + rr(i + 1, 1)] == 0 and p.room[r + rb(i,0)][c + rb(i,1)] != 0:
                s.blit(pygame.transform.rotate(walls[0], 90 * i), (x, y))

def cinput(room, mov):
    if mov == pygame.K_ESCAPE:
        return False
    elif mov == pygame.K_w or mov == pygame.K_UP and room.cr > 0:
        room.cr -= 1
    elif mov == pygame.K_a or mov == pygame.K_LEFT and room.cc > 0:
        room.cc -= 1
    elif mov == pygame.K_s or mov == pygame.K_DOWN and room.cr < room.r - 1:
        room.cr += 1
    elif mov == pygame.K_d or mov == pygame.K_RIGHT and room.cc < room.c - 1:
        room.cc += 1
    return True
if __name__ == "__main__":
    name=input("name |")
    rtype=""
    while rtype not in rtypes:
        rtype=input("type |")
        r = c = 0
        
    while r%2==0 or c%2==0:
        try:
            r = int(input("rows |"))
            c = int(input("cols |"))
        except ValueError:
            pass
    etc = input("etc. |")
    room = Room(name, rtype, r, c, etc)
    print(r)
    pygame.init()
    screen = pygame.display.set_mode((32*room.r, 32*room.c))
    playin = True
    clock = pygame.time.Clock()    
    while playin:
        screen.fill((0,0,0))
        for i in range(room.r):
            for j in range(room.c):
                render_wall(room, i, j, screen, j*32, i*32)
        screen.blit(player[0], (room.cc*32, room.cr*32))
        pygame.display.flip()
        clock.tick(15)
        for e in pygame.event.get():
            if e.type == pygame.locals.QUIT:
                playin = False
        pr = pygame.key.get_pressed()
        for k in (ke for ke in movs if pr[ke]):
            playin = cinput(room, k)
                        
