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

def render_wall(p, r, c, s, x, y):
    for i in range(4):        
        if 0 < r + (i-1 if i % 2 == 0 else 0) < p.level.r and 0 < c + (i-2 if i % 2 == 1 else 0) < p.level.c and p.level.dungeon[r + (i-1 if i % 2 == 0 else 0)][c + (i-2 if i % 2 == 1 else 0)] != 0 and p.fow[r + (i-1 if i % 2 == 0 else 0)][c + (i-2 if i % 2 == 1 else 0)]:
            s.blit(pygame.transform.rotate(walls[1], 90 * i - 90), (x, y))
            
  
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    screen.fill((0,0,0))
    p = Player()
    for i in range(p.level.r):
        for j in range(p.level.c):
            render_wall(p, i, j, screen, 32 * i, 32 * j)
    while pygame.event.wait().type != pygame.locals.QUIT:
        pass
