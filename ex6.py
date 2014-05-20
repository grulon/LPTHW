# assign string to X with numeric (decimal?) formatter
x = "There are %d types of people." % 10
# set 2 strings
binary = "binary"
do_not = "don't"
# same as above using 2 formatters (strings)
y = "Those who know %s and those who %s." % (binary, do_not)

#printing the strings we pieced together above
print x
print y

#using a formatter to return the %r (raw) in one and a %s (string) in the other.
print "I said: %r." % x
print "I also said: '%s'." % y

#set binary / bit / boolean value
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."
# concatenation of string.
print w + e