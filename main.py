#!/usr/bin/env python3
import re, sys, os, time
import itertools

# --load-anim
n_points = 5
points_l = [ '.' * i + ' ' * (n_points - i) + '\r' for i in range(n_points) ]
cond = True



class Path(object):
	def __init__(self):
		self.user = os.environ.get("USER") # user
		

	def search(self, i1: str, i2: str): # dir, str to search

		# checks if is binary file
		textchars = bytearray({7,8,9,10,12,13,27} | set(range(0x20, 0x100)) - {0x7f})
		is_binary_string = lambda bytes: bool(bytes.translate(None, textchars))

		diros = os.listdir(i1)
		diros = diros.remove('.DS_Store')

		for filename in diros:
			with open(filename, 'rb') as rf:
				if is_binary_string(rf.read(1024)) == False:
					print(f"Searching {filename} for substring...")
					content = rf.readlines()
					for index, line in enumerate(content):
						for x in [f"Found at index {m.start()} on line {line}" for m in re.finditer(i2, line)]:
							print(x)
				elif is_binary_string(rf.read(1024)) == True:
					print(f"{filename} is a binary file. Skipping...")

	def types(self, i1: str): # importing directory through types
		i2 = input("What string are you looking for all occurrences of in this entire directory?: ")
		if i2 is not None:
			print(f"You are looking for {i2} in your files.")
			self.search(i1, i2)

	def propogate(self):
		pass

	def find(self, keyword: str):
		pass


# init
p = Path()

def main():
	print("[ grepPy is starting ]")
	i1 = input("Enter absolute path of parent directory: ")
	if os.path.exists(f"{i1}"):
		print(f"Found {i1}")
		p.types(i1)
	else:
		print(f"Couldn't find {i1}.")

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("\n")
		try:
			sys.exit(0)
		except SystemExit:
			os._exit(0)

