#!/usr/bin/env python

for fb in range (1,101):
    if (fb % 3 == 0 and fb % 5 == 0):
        print ("FizzBuzz")
    elif (fb % 3 == 0):
        print ("Fizz")
    elif (fb % 5 == 0):
        print ("Buzz")
    else:
        print ("none")