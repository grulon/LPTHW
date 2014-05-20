name = 'Gavin Rulon'
age = 42
height = 69 # inches
weight = 188 # lbs
eyes = 'Brown'
teeth = 'white'
hair = 'gray-ish'

print "let's talk about %s." % name
print "he's %d inches tall." % height
print "he weighs %d pounds." % weight
print "he's got %s hair and %s eyes." % (hair, eyes)
print "his teeth are usually %r depending on coffee." % teeth

print "If I add up %d, %d, and %d I will get %d." % (age,height, weight, age+height+weight)


# playing around with math
inchesInFoot = 12
feetInYard = 3
yardsInMile = 1760

print "There are %d inches in a yard." % (inchesInFoot * feetInYard)
print "There are %d feet in a mile and %d inches in a mile." % (
feetInYard * yardsInMile, inchesInFoot * feetInYard * yardsInMile)