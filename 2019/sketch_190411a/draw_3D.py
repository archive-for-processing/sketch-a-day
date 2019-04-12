from debug import *

def draw_3d(box_w, box_d, ab_i, cd_i):
    """
    main 3D drawing procedure, this also calculates some 3D point positions
    from 2 lists of heights (ab_i and cd_i) that will then be returned
    and used by the 2D procedure
    """
    # calculates upper 3D points from heights
    num_i = len(cd_i)
    cd_pts = tuple([(box_w, box_d - box_d * i / (num_i - 1), cd_i[::-1][i])
                    for i in range(num_i)])
    ab_pts = tuple([(0, box_d * i / (num_i - 1), ab_i[::-1][i])
                    for i in range(num_i)]) 
    # draw faces   
    stroke(0)
    fill(255, 200)
    # floor face
    poly_draw(((0, 0, 0),
               (box_w, 0, 0),
               (box_w, box_d, 0),
               (0, box_d, 0)))
    # face 0
    poly_draw(((0, 0, ab_i[-1]),
               (box_w, 0, cd_i[0]),
               (box_w, 0, 0),
               (0, 0, 0)))
    # face 1
    poly_draw(cd_pts + (
        (box_w, 0, 0),
        (box_w, box_d, 0)))
    # face 2
    poly_draw(((box_w, box_d, cd_i[-1]),
               (0, box_d, ab_i[0]),
               (0, box_d, 0),
               (box_w, box_d, 0)))
    # face 3
    poly_draw(ab_pts + (
        (0, box_d, 0),
        (0, 0, 0)))
    # top faces - using calculated the 3D points 
    face_data = []
    for i in range(1, len(ab_pts)):
        p = i - 1
        a = PVector(*ab_pts[p])
        b = PVector(*ab_pts[i])
        c = PVector(*cd_pts[::-1][i])
        d = PVector(*cd_pts[::-1][p])
        triangulated_face(a, b, c, d)
        face_data.append((a, b, c, d))
    # debug text
    debug_text("cd", cd_pts[::-1], enum=True)
    debug_text("ab", ab_pts[::-1], enum=True)
    debug_text("DAad", ((box_w, box_d, cd_i[-1]),
                            (0, box_d, ab_i[0]),
                            (0, box_d, 0),
                            (box_w, box_d, 0)))
    return face_data # returns to be used by the 2D procedure

def poly_draw(points, closed=True):
    """ sugar for face drawing """
    beginShape()
    for p in points:
        vertex(*p)
    if closed:
        endShape(CLOSE)
    else:
        endShape()

def triangulated_face(a, b, c, d):
    # two triangles - could be with a diferent diagonal!
    # TODO: let one choose diagonal orientation
    poly_draw((a, b, d))
    poly_draw((b, d, c))
