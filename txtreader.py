import linecache

def printall(filename):
	print "There is the hole file:"
	data = open(filename,"r")
	print data.read()
	data.close()

print "input the filename"
filename = raw_input(">")
printall(filename)

data = open(filename,"r")
data.seek(0)
linecount = len(data.readlines()) #get the number of lines

while 1:
	print "The file has %r lines. Which one do you want?" % linecount
	WantedLine = int(raw_input(">"))
	if (WantedLine > 0 and (WantedLine  < linecount + 1) ) : break

linecache.clearcache()
data.seek(0)
print linecache.getline(filename,WantedLine),
data.close()

	
	




