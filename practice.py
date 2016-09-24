#practice
print "let's practice exerything"
print "you\'d need to know\'bout escapes with\\that do\n newlines and \t tabs"

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
\n\t\twhere there is none.
"""

print '-'*37
print poem
print '-'*37

five = 10 - 2 + 3 - 6
print "This should be five:%s" % five

def f(started):
	beans = started * 500
	jars = beans / 1000
	crates = jars / 1000
	return beans,jars,crates

StartPoint = int(raw_input('What\'s the start point?\n>'))
Beans, Jars, Crates = f(StartPoint)

print "With a starting point of: %d" % StartPoint
print "We'd have %d besns, %d jars, and %d crates." % (Beans , Jars , Crates)

StartPoint = StartPoint / 10

print "Now,we'd have %d besns, %d jars, and %d crates." % f(StartPoint)