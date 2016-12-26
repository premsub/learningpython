from sys import argv
def read_file(file_name):
	file_handle=open(file_name)
	file_handle.seek(0)
	return file_handle.read()

def append_file(file_name,file_con):
	file_handle=open(file_name,'a+')
	file_handle.seek(2)
	file_con="\n"+file_con
	file_handle.write(file_con)
	file_handle.close()
def copy_file(file_name1, file_name2):
	# fh1=read_file(file_name1)
	fh2=open(file_name2,'w+')
	fh2.seek(0)
	fh2.write(read_file(file_name1))
	fh2.close
arg0,arg1,arg2=argv
# append_file(arg1,arg2)
# read_file(arg1)
copy_file(arg1,arg2)
