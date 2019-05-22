import math

def root_finder(function,precision):
	print("Make a guess of the surrounding values")
	upper = float(input("Upper guess: "))
	lower = float(input("Lower guess: "))
	#print (type(upper))
	#print (function(upper))
	#
	while function(upper)*function(lower) > 0:
		print("Please make a different guess")
		upper = float(input("Upper guess: "))
		lower = float(input("Lower guess: "))

	x=(lower+upper)/2.0
	while abs(function(x)) > precision:
		if function(x)>0:
			upper = x
			x = (lower+upper)/2.0
		else:
			lower=x
			x=(lower+upper)/2.0
	return(x)
