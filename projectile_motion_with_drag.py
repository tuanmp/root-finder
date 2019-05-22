import math
import root_finding_routine as rf
import numpy as np
import matplotlib.pyplot as plt

g = 9.8
theta_0 = float(input("Launch angle(degrees) : "))
launch_angle = math.radians(theta_0)
print(launch_angle)
mass = float(input("Projectile mass(kg): "))
b = float(input("Drag coefficient(kg.s^-2): "))
v_0 = float(input("Initial spped: "))
r_max = v_0**2/g
v_ter = mass*g/b
u = v_0/v_ter


def function(t):
    y = t*u**2*np.tan(launch_angle) + t*u/(np.cos(launch_angle)) + np.log(1 - t*u/(np.cos(launch_angle)))
    return y


x = rf.root_finder(function, 0.00000001)

range = x*r_max

print(range)
