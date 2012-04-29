
from threading import Thread
from Queue import Queue

class QueuedDataSource(Thread):
	def __init__(self, proc, converter):
		self._converter = converter
		self._proc = proc
		self._queue = Queue()
		Thread.__init__(self)

	def run(self):
		self.collect_data(self._converter)

	def collect_data(self, converter):
		# While the process is alive
		while self._proc.poll() is None:
			for data in converter(self._proc):
				# do something clever with the data
				self._queue.put(data)

	def get(self, block = True, timeout = None):
		return self._queue.get(block, timeout)
