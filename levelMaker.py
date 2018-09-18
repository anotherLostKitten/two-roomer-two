# Procedural Dungeon generation

from random import randint, choice
import roomMaker

basic = ["exit", "spawn"]
boss = []
shop = []
enemy = []

class Level():
    """ Level Creation Algo:
        0. Generate dungeon array
        1. populate dungeon with rooms
            a. exit, spawn
            b. boss
            c. shop
            d. <n> enemy rooms
        2. generate mazes in unfilled space
        3. create spanning tree of rooms and mazes
        4. add extra connections
        5. remove dead ends in corridor
        6. texture rooms
    """
    def __init__(self, r, c, n):
        # 0
        dungeon = []
        for i in range(0, r):
            dungeon.append([])
            for j in range(0, c):
                dungeon[i].append(0)
        # 1a
        
        
