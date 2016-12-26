from sys import argv
def multiply(*args):
	a,b=args
	c=a*b
	return c
arg1,arg2,arg3=argv
arg2=int(arg2)
arg3=int(arg3)
d=multiply(arg2,arg3)
print "the result is=",d
