
import pyglet.gl

ARENA_SIZE = 800
ROBOT_SIZE = 50

def quad_vertices(origin, size):
	idx = [0, 1, 2, 0, 2, 3]
	verts = ( origin[0]          , origin[1],
	          origin[0] + size[0], origin[1],
	          origin[0] + size[0], origin[1] + size[1],
	          origin[0]          , origin[1] + size[1] )

	return ( idx, verts )

def sqaure_vertices(origin, size):
	return quad_vertices(origin, (size, size))

def quad_colours(colour):
	colours = ( colour[0], colour[1], colour[2],
	            colour[0], colour[1], colour[2],
	            colour[0], colour[1], colour[2],
	            colour[0], colour[1], colour[2] )

	return colours

def batch_quad(batch, origin, size, colour = (255, 255, 255)):
	(idx, verts) = quad_vertices(origin, size)
	colours = quad_colours(colour)
	quad = batch.add_indexed(4, pyglet.gl.GL_TRIANGLES, None,
	                         idx, ('v2f', verts ),
	                         ('c3B', colours )
	                        )

	return quad

def batch_sqaure(batch, origin, size, colour):
	return batch_quad(batch, origin, (size, size), colour)

def batch_robot(batch, center, colour):
	hrs = ROBOT_SIZE / 2
	origin = ( center[0] - hrs, center[1] - hrs )
	return batch_sqaure(batch, origin, ROBOT_SIZE, colour)
