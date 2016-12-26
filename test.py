from sys import argv
from os.path import exists
a,b=argv
if exists(b):
	print "file",b,"exists"
else:
	print "file",b,"doesnt exists"

