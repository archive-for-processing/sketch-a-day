# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s295"  # 20181020
OUTPUT = ".gif"

NUM = 6 
BORDER = 50
SPACING = 15

def setup():
    global poly
    size(500, 500)
    frameRate(5 )
    poly = create_points(True)
    
def create_points(non_intersecting=True):
    background(200)
    done = False
    while not done:
        points = [PVector(random(BORDER, width - BORDER),
                          random(BORDER, height - BORDER))
                  for _ in range(NUM)]
        edges = pairwise(points) + [(points[-1], points[0])]
        done = True
        if non_intersecting:
            for p1, p2 in edges:
                for p3, p4 in edges:
                    # test only non consecutive edges
                    if (p1 != p3) and (p2 != p3) and (p1 != p4):
                        if line_instersect(Line(p1, p2), Line(p3, p4)):
                            # stroke(255, 51)
                            # strokeWeight(2)
                            # line(p1.x, p1.y, p2.x, p2.y)
                            done = False
                            break
    return points
    

def draw():
    noStroke()
    
    fill(200, 0, 0)
    for p in poly:
       ellipse(p.x, p.y, SPACING/2, SPACING/2)
       
    fill(0, 0, 200)
    for x in range(0, width, SPACING):
        for y in range(0, height, SPACING):
            draw_if_inside(poly, x, y)
    stroke(0)
    strokeWeight(2) 
    edges = pairwise(poly) + [(poly[-1], poly[0])]    
    for p1, p2 in edges:
        line(p1.x, p1.y, p2.x, p2.y)       
   
   
def draw_if_inside(points, x, y):   
    a = PVector(x, 0)
    b = PVector(x, height)
    inter_points_x = inter_line_points(points, Line(a, b))
    if  not inter_points_x: return
    v_lines = inter_lines(inter_points_x)
        
    a = PVector(0, y)
    b = PVector(width, y)
    inter_points_y = inter_line_points(points, Line(a, b))
    if not inter_points_x: return
    h_lines = inter_lines(inter_points_y)
            
    for v in v_lines:
        for h in h_lines:
            p = line_instersect(v, h)
            if p:
                ellipse(p.x, p.y, SPACING/2, SPACING/2)
    return
            
     
         


def inter_line_points(points, L):                         
    edges = pairwise(points) + [(points[-1], points[0])]
    inter_points = []
    
    for p1, p2 in edges:
        # strokeWeight(2)
        # line(p1.x, p1.y, p2.x, p2.y)
        inter = line_instersect(Line(p1, p2), L)
        if inter:
            inter_points.append(inter)
    return inter_points   


def inter_lines(inter_points):
    inter_lines = []
    if inter_points and len(inter_points) > 1:
        inter_points.sort()
        pairs = zip(inter_points[::2], inter_points[1::2])
        for p1, p2 in pairs:
            if p2:
                inter_lines.append(Line(PVector(p1.x, p1.y),
                                        PVector(p2.x, p2.y))) 
    return inter_lines

    
def keyPressed():
    global poly
    if key == " ": 
        poly = create_points(True)
    if key == "s": saveFrame("###.png")
        
class Line():
    """ I should change this to a named tuple... """
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
def line_instersect(line_a, line_b):     
    """
    code adapted from Bernardo Fontes 
    https://github.com/berinhard/sketches/
    """
       
    x1, y1 = line_a.p1.x, line_a.p1.y
    x2, y2 = line_a.p2.x, line_a.p2.y
    x3, y3 = line_b.p1.x, line_b.p1.y
    x4, y4 = line_b.p2.x, line_b.p2.y
        
    try:
        uA = ((x4-x3)*(y1-y3) - (y4-y3)*(x1-x3)) / ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1));
        uB = ((x2-x1)*(y1-y3) - (y2-y1)*(x1-x3)) / ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1));
    except ZeroDivisionError:
        return 
        
    if not(0 <= uA <= 1 and 0 <= uB <= 1):
        return
        
    x = line_a.p1.x + uA * (line_a.p2.x - line_a.p1.x)
    y = line_a.p1.y + uA * (line_a.p2.y - line_a.p1.y)
        
    return PVector(x, y)


def pairwise(iterable):
    import itertools
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b) 

# print text to add to the project's README.md             
def settings():
    println(
"""
![{0}]({0}/{0}{2})

{1}: [code](https://github.com/villares/sketch-a-day/tree/master/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(SKETCH_NAME, SKETCH_NAME[1:], OUTPUT)
    )
