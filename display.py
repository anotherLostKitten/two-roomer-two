import pygame
import pygame.locals
from player import Player

def get_textures(filename):
    m = pygame.image.load("textures/" + filename + ".png")
    mw, mh = m.get_size()
    textures = []
    for i in range(0, mh, 32):
        for j in range(0, mw, 32):
            print(i, ', ', j)
            textures.append(m.subsurface(j, i, 32, 32))
    return textures
walls = get_textures("walls")

def rr(i, rc):
    i %= 4
    return i-1-rc if (i+rc) % 2 == 0 else 0
def rb(i, rc):
    i = (i + 1 - rc) % 4
    return -1 if i < 2 else 1
def render_wall(p, r, c, s, x, y):
    for i in range(4):        
        if 0 <= r + rr(i,0) < p.level.r and 0 <= c + rr(i, 1) < p.level.c and p.level.dungeon[r + rr(i,0)][c + rr(i,1)] != 0: # and p.fow[r + (i-1 if i % 2 == 0 else 0)][c + (i-2 if i % 2 == 1 else 0)]:
            s.blit(pygame.transform.rotate(walls[1], -90 * i), (x, y))
    for i in range(4):
        if 0 <= r + rb(i, 0) < p.level.r and 0 <= c + rb(i, 1) < p.level.c:
            if p.level.dungeon[r + rr(i, 0)][c + rr(i, 1)] !=0 and p.level.dungeon[r + rr(i + 1, 0)][c + rr(i + 1, 1)] != 0:
                s.blit(pygame.transform.rotate(walls[2], - 90 * i), (x, y))
            if p.level.dungeon[r + rr(i, 0)][c + rr(i, 1)] == p.level.dungeon[r + rr(i + 1, 0)][c + rr(i + 1, 1)] == 0 and p.level.dungeon[r + rb(i,0)][c + rb(i,1)] != 0:
                s.blit(pygame.transform.rotate(walls[0], - 90 * i), (x, y))
  
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1200, 960))
    screen.fill((0,0,0))
    p = Player()
    for i in range(p.level.r):
        for j in range(p.level.c):
            if (p.level.dungeon[i][j] == 0):
                render_wall(p, i, j, screen, 32 * i, 32 * j)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.locals.QUIT:
        pass
