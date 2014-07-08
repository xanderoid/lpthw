name = 'Xander J. Taylor'
age = 32 # not a lie
height = 5 * 12 + 10 # 5'10" converted to inches
weight = 168 # pounds
eyes = 'Hazel'
teeth = 'White'
hair = 'Brown (plus a little salt)'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

# study drills
cm_per_in = 2.54
print '12 inches is equal to', 12 * cm_per_in