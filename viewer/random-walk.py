
import pyglet
from pyglet.graphics import Batch
from random import randint

from glutils import *

window = pyglet.window.Window(width=800, height=800)
batch = Batch()

x = y = 100
my_square = batch_sqaure(batch, (x, y), 20, (127, 0, 255))

@window.event
def on_draw():
#	print 'Draw'
	window.clear()
	batch.draw()

def limit(n, bottom, top):
	return min(top, max(n, bottom))

def update(dt):
	global x, y
	mov = 10
	x_mod = randint(-1 * mov, mov)
	y_mod = randint(-1 * mov, mov)

	x = limit(x + x_mod, 0, 780)
	y = limit(y + y_mod, 0, 780)

	(idx, verts) = sqaure_vertices((x,y), 20)
	my_square.vertices = verts

def end(dt):
	window.close()

pyglet.clock.schedule_interval(update, 0.01)

# Will close the demo in 20s.
pyglet.clock.schedule_interval(end, 20)

pyglet.app.run()
