#!usr/bin/python
#matt96beckman@gmail.com
def plus25(argument):
    print "I'm in the function plus25"
    return argument + 25

print "Start..."
variable1 = True
variable2 = 18
for z in range (variable2, 252, 9):
    print "hello there" ,
    quarters = plus25(z)
    print "quarters = " + str(z)
    variable2 = variable2 + 1
print "End."
