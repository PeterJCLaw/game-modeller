#!/usr/bin/env python

from threading import Thread, Event
from time import sleep

from robot import Robot

def main():
	threads = []

	# Game start lock
	game_start = Event()

	for i in range(4):
		r = Robot(i, game_start)
		t = Thread( target = r.run, args = (i, ) )
		threads.append(t)
		t.start()

	# Start the game
	game_start.set()

	sleep(180)	# 3 minute match

	exit()

if __name__ == '__main__':
	main()
