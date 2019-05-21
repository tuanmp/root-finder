import math

def root_finder(function, precision):
	print("Make a guess of the surrounding values")
  	upper = input("Upper guess: ")
  	lower = input("Lower guess: ")
  
  	While function(upper)*function(lower) > 0:
    	print("Please make a different guess")
    	upper = input("Upper guess: ")
    	lower = input("Lower guess: ")
    
  	x=(lower+upper)/2.0
  	While abs(function(x)) > precision:
    	If function(x)>0:
      		upper = x
      		x = (lower+upper)/2.0
    	Else: 
			lower=x
			x=(lower+upper)/2.0
	Return(x)
		
