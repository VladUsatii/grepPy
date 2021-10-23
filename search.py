#!/usr/bin/env python3
import re, sys, os, time
import itertools
import glob
from rich.console import Console

# init Rich
cons = Console()

user = os.environ.get("USER") # user

def search(dirs: str, string: str) -> list:
	matches = 0

	# supported file search -> release 1
	TXTFILES = [f for f in glob.glob(f"{dirs}/*.txt")]
	PYFILES = [f for f in glob.glob(f"{dirs}/*.py")]
	HTMLFILES = [f for f in glob.glob(f"{dirs}/*.html")]

	FILES = list(itertools.chain(TXTFILES, PYFILES, HTMLFILES))
	print(FILES)

	# search and document

	# TXTFILES
	for f in FILES:
		with open(f) as obj:
			# gather types
			if ".txt" in f:
				types = "*.txt"
			elif ".py" in f:
				types = "*.py"
			elif ".html" in f:
				types = "*.html"

			# enumerate
			for index, lines in enumerate(obj):
				if string in lines:
					matches += 1
					cons.print(f"[ file type '{types}' • file '{obj}' • line {index} ]", style="bold white")
	print(f"{matches} occurrences of the string '{string}'")



def main():
	dirs = input("Enter the directory to search for a string: ")
	if os.path.exists(dirs) and dirs[-1:] != "/":
		cons.print("[ Directory found ]", style="bold green")
		string = input("Enter the string to search for in the files: ")
		cons.print("[ String added ]", style="bold yellow")
		cons.print("[ Searching files ... ]", style="bold white")
		search(dirs, string)
		cons.print("[ All done! ]", style="bold green")
	elif dirs[-1:] == "/":
		cons.print("[ Enter directory without an ending slash ]", style="bold red")
	else:
		cons.print("[ A process aborted ]", style="bold red")


if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("\n")
		try: sys.exit()
		except SystemExit: os._exit(0)

