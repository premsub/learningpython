# This file reads a CSV of integers and converts into an array for processing
from fileman import *
from sys import argv
for i in read_file(argv[1]).split(','):
	print i