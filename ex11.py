#first lesson to teach accepting input from users

print "How old are you?",
age = raw_input()

print "How tall are you?",
height = raw_input()

print "How much do you weigh?",
weight = int(raw_input())

print "So, you are %r old, %r tall, and %r heavy." % (
	age, height, weight)