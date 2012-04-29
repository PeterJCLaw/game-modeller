
import pyglet
import Queue

import glutils
from glutils import ARENA_SIZE, ROBOT_SIZE
from queueddatasource import QueuedDataSource

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

#		print "Updating robot '%d': %s" % ( rid, (x,y) )

		if not self._robots.has_key(rid):
			colour = colour_from_id(rid)
			self._robots[rid] = glutils.batch_robot(self._batch, (x, y), colour)
		else:
			(idx, verts) = glutils.sqaure_vertices((x,y), ROBOT_SIZE)
			self._robots[rid].vertices = verts

	def _end(self, dt):
		self.close()
