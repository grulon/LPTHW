tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

# could use """ instead of '''  Typically use """ if using ' in text
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
'''
print "\b"  # makes a bell sound
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

print "\\ \' \" \a \f \n \001 "    #\xhh was invalid \x escape

# when it is running how do you make it false?  I used control + c as KeyboardInterrupt
while True:
	for i in ["/","-","|","\\","|"]:
		print "%s\r" % i,