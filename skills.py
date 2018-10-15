from random import randint, choice, randrange

#    1: +
#       ^ 
# 0: +  p  -
#
#       -

def basic_mov():
    return {'m':((1,0))}
def basic():
    return {'a':((1,0))}
def scythe():
    return{'a':((1,0), (1,1), (1,-1), (0,-1))}
def dash():
    return{'o':('m', 'a'), 'a':((0,1), (0,-1), (1,1), (1,-1)), 'm':((1,0), (1,0), (1,0))}
def pokers():
    return{'a':((2,0), (1,1), (3,1), (1,-1), (3,-1))}
def knight():
    return{'a':((1,0), (2,0)), 'm':((0,1), (1,0), (1,0)), 'o':('a', 'm')} 
def tp():
    d = ranint(1)
    s = randrange(-1, 2, 2)
    return{'m':((2*s*d,2*s*(1-d)))}
q = {'basic':basic,'scythe':scythe, 'dash':dash, 'pokers':pokers, 'knight':knight}
e = {'tp':tp}
sp = {'basic_mov':basic_mov}
