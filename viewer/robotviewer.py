
import pyglet
import Queue

import glutils
from queueddatasource import QueuedDataSource

ARENA_SIZE = 800
ROBOT_SIZE = 50

def limit(n, bottom, top):
    return min(top, max(n, bottom))

def colour_from_id(rid):
    colour = [ 0, 0, 0 ]
    colour[rid % 3] = 255
    if rid > 2:
        colour[(1 + rid) % 3] = 255

    return tuple(colour)

class RobotViewer(pyglet.window.Window):
    def __init__(self, data_source,
                 duration = 180,
                 width  = ARENA_SIZE,
                 height = ARENA_SIZE,
                ):
        super(RobotViewer, self).__init__(caption = "Robot Viewer",
                                          width = width,
                                          height = height)
        self._batch = pyglet.graphics.Batch()

        self._ds = data_source

        self._robots = dict()

        pyglet.clock.schedule_interval(self._update, 0.01)
        pyglet.clock.schedule_interval(self._end, duration)

    def on_draw(self):
        self.clear()
        self._batch.draw()

    def _batch_robot(self, rid, center):
        colour = colour_from_id(rid)
        self._robots[rid] = glutils.batch_sqaure2(self._batch, center, ROBOT_SIZE, colour)

    def _update(self, dt):
        data = None
        try:
            data = self._ds.get(timeout = 0.01)
        except Queue.Empty:
            return

        if data['type'] != 'robot':
            return

        rid = data['id']

        x = data['pos']['x']
        y = data['pos']['y']

        x = int(x * 100)
        y = int(y * 100)

#        print "Updating robot '%d': %s" % ( rid, (x,y) )

        if not self._robots.has_key(rid):
            self._batch_robot(rid, (x,y))
        else:
            origin = glutils.make_origin((x,y), ROBOT_SIZE)
            (idx, verts) = glutils.sqaure_vertices(origin, ROBOT_SIZE)
            self._robots[rid].vertices = verts

    def _end(self, dt):
        self.close()
