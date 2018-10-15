import pygame
import pygame.locals
from player import Player, binput

def get_textures(filename):
    m = pygame.image.load("textures/" + filename + ".png")
    mw, mh = m.get_size()
    textures = []
    for i in range(0, mh, 32):
        for j in range(0, mw, 32):
            textures.append(m.subsurface(j, i, 32, 32))
    return textures
walls = get_textures("walls")
door = get_textures("door")
player = get_textures("pp_hed")
def rr(i, rc):
    i %= 4
    return i-1-rc if (i+rc) % 2 == 0 else 0
def rb(i, rc):
    i = (i + 1 - rc) % 4
    return -1 if i < 2 else 1
def render_wall(p, r, c, s, x, y):
    for i in range(4):
        if 0 <= r + rr(i,0) < p.level.r and 0 <= c + rr(i, 1) < p.level.c and p.level.dungeon[r + rr(i,0)][c + rr(i,1)] != 0 and p.fow[r + (i-1 if i % 2 == 0 else 0)][c + (i-2 if i % 2 == 1 else 0)]:
            s.blit(pygame.transform.rotate(walls[1], 90 * i - 90), (x, y))
    for i in range(4):
        if 0 <= r + rb(i, 0) < p.level.r and 0 <= c + rb(i, 1) < p.level.c:
            if p.level.dungeon[r + rr(i, 0)][c + rr(i, 1)] !=0 and p.level.dungeon[r + rr(i + 1, 0)][c + rr(i + 1, 1)] != 0 and p.fow[r + rr(i, 0)][c + rr(i, 1)] and p.fow[r + rr(i + 1, 0)][c + rr(i + 1, 1)]:
                s.blit(pygame.transform.rotate(walls[2], 90 * i), (x, y))
            if p.level.dungeon[r + rr(i, 0)][c + rr(i, 1)] == p.level.dungeon[r + rr(i + 1, 0)][c + rr(i + 1, 1)] == 0 and p.level.dungeon[r + rb(i,0)][c + rb(i,1)] != 0 and p.fow[r + rb(i,0)][c + rb(i,1)]:
                s.blit(pygame.transform.rotate(walls[0], 90 * i), (x, y))

def renderp(p, s, r):
    s.fill((0,0,0))
    for i in range(p.r, p.r + 2 * r + 1):
        for j in range(p.c, p.c + 2 * r + 1):
            if -1 < i - r < p.level.r and -1 < j - r < p.level.c and p.fow[i - r][j - r]:
                if p.level.dungeon[i - r][j - r] == 0:
                    render_wall(p, i-r, j-r, s, (j - p.c) * 32, (i - p.r) * 32)
                elif p.level.dungeon[i - r][j - r] == 7:
                    s.blit(door[0], ((j - p.c) * 32, (i - p.r) * 32))
    s.blit(player[0], (r * 32, r * 32))
    pygame.display.flip()
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((672, 672))
    screen.fill((0,0,0))
    p = Player()
    dradius = 10
    playin = True
    renderp(p, screen, dradius)
    clock = pygame.time.Clock()
    while playin:

        clock.tick(15)
        for e in pygame.event.get():
            if e.type == pygame.locals.QUIT:
                playin = False
            elif e.type == pygame.locals.KEYDOWN:
                playin = binput(p, chr(e.key))
        renderp(p, screen, dradius)
