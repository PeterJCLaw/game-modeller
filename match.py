
class Match(object):

	def __init__(self):
		# Game start lock
		self._game_start = Event()

		robots = []

		for i in range(4):
			r = Robot(i, self._game_start)
			robots.append(r)
			t = Thread( target = r.run, args = (i, ) )
			t.start()

		for r in robots:
			r.addOpponents(robots)

	def start(self)
		"Start the game"
		self._game_start.set()
