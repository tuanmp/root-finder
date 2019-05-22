import math

def function(x):
    y=math.log(x,math.e) - 1
    return y

import root_finding_routine as rf

x=rf.root_finder(function,0.00000001)

print(x)