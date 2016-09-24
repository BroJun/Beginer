print "Please input your sentence"
sentence = raw_input(">")
print "What do you want your sentense split with?"
word = raw_input(">")

a = sentence.count(word)

print "Now there is the result:"

for i in range(0, a+1):
	print sentence.split(word)[i]


	
