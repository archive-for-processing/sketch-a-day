from random import choice
from elementos import casinha
def setup():
    size(600, 600)
    noLoop()
    rectMode(CENTER)
    noStroke()

def draw():
    background(255)
    grade(300, 300, 3, 600.)

def grade(xo, yo, n, tw, e=None):
    cw = tw / n
    offset = (cw - tw) / 2.
    for i in range(n):
        x = xo + offset + cw * i
        for j in range(n):
            y = yo + offset + cw * j
            o = (i + j) % 3
            if e is not None:
                element(x, y, cw * 3, e)
            elif cw > 20 and random(10) < 5:
                grade(x, y, 3, cw)
            elif cw > 30:
                grade(x, y, 3, cw, o)


def element(x, y, w, option):
    noFill()
    stroke(0, 32)
    strokeWeight(10)
    casinha(x, y, choice((w/2, w*.9, w*.6)))


def keyPressed():
    saveFrame("####.png")
    redraw()
