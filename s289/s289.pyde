# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s289"  # 20181014
OUTPUT = ".gif"

GRID_SIZE = 10
BORDER = 50

from random import seed
from random import choice
from node import Node

def setup():
    size(500, 500)
    # strokeWeight(2)
    rectMode(CENTER)
    frameRate(10)
    random_seed(1011)
    Node.init_grid(GRID_SIZE, BORDER)
            
def draw():
    translate(width/2, height/2)
    background(200)

    # if mousePressed:
    #     adv = 0
    # else: adv = 1
        
    if frameCount >= 50:
        adv = map(frameCount, 50, 100, 0, 1)
    else:
        adv = 0

    for node in Node.nodes:
        node.plot(0)
        
    # Node.nodes[0].rot0 = 0
    # Node.nodes[0].size_ = 2
    # Node.nodes[0].plot(0)
             
    # if frameCount < 150:
    #     pass
    #     # saveFrame("###.png")
    # else:
    #     noLoop()
 
def keyPressed():
    if key == "n":
        Node.init_grid(GRID_SIZE, BORDER)
    if key == "s": saveFrame("###.png")
    
    
def random_seed(s=None):
    global rnd_seed
    if s:
        rnd_seed = s
        seed(rnd_seed)
        randomSeed(rnd_seed)    
    else:
        seed(rnd_seed)
        randomSeed(rnd_seed)
    
# print text to add to the project's README.md             
def settings():
    println(
"""
![{0}]({0}/{0}{2})

{1}: [code](https://github.com/villares/sketch-a-day/tree/master/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(SKETCH_NAME, SKETCH_NAME[1:], OUTPUT)
    )
