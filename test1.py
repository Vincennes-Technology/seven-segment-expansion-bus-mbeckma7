#!/usr/bin/python
#mbeckma: test functions for class
print "Hello World"
print "From the ELEC230 Class!"
var1s = raw_input("what is var1 ")
var1 = int(var1s)

var2s = raw_input("waht is var2 ")
var2 = float(var2s)
if var2 > 6:
    print "Bingo!"
    print "Var2 is more than six!"

var3 = var1 * var2
print "This answer is: ", var3

answer = raw_input("What do you want me to say?")
if len(answer) > 10:
    answer = "too long"
else:
    print "short answers are preffered"
#answer2 = answer.split()
print answer + str(var3)





