from os.path import isfile

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

movs = (pygame.K_ESCAPE, pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_UP, pygame.K_LEFT, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_SPACE, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9, pygame.K_0)

class Room():
    def __init__(self, name, rtype = None, r = None, c = None, etc = None):
        if rtype != None:
            self.name = name
            self.type = rtype
            self.r = r if r > c else c
            self.c = c if r > c else r
            self.room = [x[:] for x in ([[1] * self.c] * self.r)]
            self.etc = etc + '\n'
        else:
            self.read(name)
        self.cr = self.cc = 0
    def read(self, fileName):
        f = open("rooms/" + fileName + ".room", 'r')
        l = f.read().split('\n')
        print(l)
        f.close()
        self.name = l[0]
        self.type = l[1]
        self.r = int(l[2][:l[2].index('x')])
        self.c = int(l[2][l[2].index('x') + 1:])
        self.room = [[int(j) for j in l[i+3].split(' ')[:self.c]] for i in range(self.r)]
        self.etc = ''
        for i in l[self.r+3:]:
            self.etc += i
        '''
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
        '''
    def __str__(self):
        txt = "" + self.name + "\n" + self.type + "\n" + str(self.r) + "x" + str(self.c) + "\n"
        for i in self.room:
            for j in i:
                txt += str(j) + ' '
            txt += "\n"
        return txt + self.etc
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
    if p.room[r][c] == 0:
        for i in range(4):
            if 0 <= r + rr(i,0) < p.r and 0 <= c + rr(i, 1) < p.c and p.room[r + rr(i,0)][c + rr(i,1)] != 0:
                s.blit(pygame.transform.rotate(walls[1], 90 * i - 90), (x, y))
        for i in range(4):
            if 0 <= r + rb(i, 0) < p.r and 0 <= c + rb(i, 1) < p.c:
                if p.room[r + rr(i, 0)][c + rr(i, 1)] != 0 and p.room[r + rr(i + 1, 0)][c + rr(i + 1, 1)] != 0:
                    s.blit(pygame.transform.rotate(walls[2], 90 * i), (x, y))
                if p.room[r + rr(i, 0)][c + rr(i, 1)] == p.room[r + rr(i + 1, 0)][c + rr(i + 1, 1)] == 0 and p.room[r + rb(i,0)][c + rb(i,1)] != 0:
                    s.blit(pygame.transform.rotate(walls[0], 90 * i), (x, y))

def cinput(room, mov):
    if mov == pygame.K_ESCAPE:
        return False
    elif (mov == pygame.K_w or mov == pygame.K_UP) and room.cr > 0:
        room.cr -= 1
    elif (mov == pygame.K_a or mov == pygame.K_LEFT) and room.cc > 0:
        room.cc -= 1
    elif (mov == pygame.K_s or mov == pygame.K_DOWN) and room.cr < room.r - 1:
        room.cr += 1
    elif (mov == pygame.K_d or mov == pygame.K_RIGHT) and room.cc < room.c - 1:
        room.cc += 1
    elif mov == pygame.K_0:
        room.room[room.cr][room.cc] = 0
    elif mov == pygame.K_1:
        room.room[room.cr][room.cc] = 1
    elif mov == pygame.K_2:
        room.room[room.cr][room.cc] = 2
    elif mov == pygame.K_3:
        room.room[room.cr][room.cc] = 3
    elif mov == pygame.K_4:
        room.room[room.cr][room.cc] = 4
    elif mov == pygame.K_5:
        room.room[room.cr][room.cc] = 5
    elif mov == pygame.K_6:
        room.room[room.cr][room.cc] = 6
    elif mov == pygame.K_7:
        room.room[room.cr][room.cc] = 7
    elif mov == pygame.K_8:
        room.room[room.cr][room.cc] = 8
    elif mov == pygame.K_9:
        room.room[room.cr][room.cc] = 9
    elif mov == pygame.K_SPACE:
        room.room[room.cr][room.cc] = 0 if room.room[room.cr][room.cc] == 1 else 1
    return True
if __name__ == "__main__":
    name=input("name |")
    if isfile("rooms/"+name+".room") and input("'o' to overwrite existing file |") != 'o':
        room = Room(name)
    else:
        rtype=''
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
    print(room)
    pygame.init()
    screen = pygame.display.set_mode((32*room.c, 32*room.r))
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
                        
    print("saving to rooms/", room.name, ".room ...", sep='')
    f = open("rooms/" + room.name + ".room", 'w')
    f.write(str(room))
    f.close()
