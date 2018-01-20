"""
s18019 - Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day


Converting some of Maeda's Design by Number
dbnletters.dbn code -> Processing
"""

from dbn_letters import *

def setup():
    size(200, 200)
    noLoop()

def draw():
    dbn_test()

def dbn_test():
    for y in range(0, 5):
        for x in range(1, 6):
            dbn_letter[x + y * 5](x * 12, -20 - y * 12)
    dbn_letterZ(x * 12 + 12, -32 - y * 12)
