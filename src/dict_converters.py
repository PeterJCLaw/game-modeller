
def point_to_dict(p):
    return dict(type = 'point', x = p.x, y = p.y)

def robot_to_dict(r):
    pos = point_to_dict(r.location)
    return dict(type = 'robot', id = r.id, pos = pos)
