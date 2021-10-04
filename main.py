#!/usr/bin/env python3
import re, sys, os, time
import itertools

# --load-anim
n_points = 5
points_l = [ '.' * i + ' ' * (n_points - i) + '\r' for i in range(n_points) ]
cond = True

class Path(object):
	def __init__(self, path: str, arg=None):
		self.arg = arg
		self.path = path
		
	def propogate(self):
		pass

	def find(self, keyword: str):
		pass


print("[ grepPy is starting ]")
i1 = input("Enter absolute path of parent directory: ")
if os.path.exists(f"{i1}"):
	print(f"Found {i1}")
	i2 = input("What path are you looking for in this entire directory?: ")
	pass
if i2:
	while True:
		for points in itertools.cycle(points_l):
			print(points, end='')
			time.sleep(0.1)
			if not cond:
				break
else:
	pass
