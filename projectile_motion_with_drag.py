import math
import root_finding_routine as rf

g = 9.8
theta_0 = float(input("Launch angle(degrees) : "))
launch_angle = math.radians(theta_0)
mass = float(input("Projectile mass(kg): "))
b = float(input("Drag coefficient(kg.s^-2): "))
v_0 = float(input("Initial spped: "))
precision = float(input("Precision goal: "))
r_max = v_0**2/g
v_ter = mass*g/b
u = v_0/v_ter


def function(x):
    y = x*u**2*math.tan(launch_angle) + x*u/(math.cos(launch_angle)) + math.log(1 - x*u/(math.cos(launch_angle)))
    return y


r = rf.root_finder(function, precision)

range = r*r_max

print(range)
