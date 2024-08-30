
# Day 31 #100daysofcodechallenge 
# 1. Convert radians into degrees
# Write a function in Python that accepts one numeric parameter. 

# This parameter will be the measure of an angle in radians.
# The function should convert the radians into degrees and then return that value.
# While you might find a Python library to do this for you, 
# you should write the function yourself. 
# One hint you get is that you'll need to use Pi in order to solve this problem. 
    #    pi=circunference/diametro
# You can import the value for Pi from Python's math module.
    # Import math Library
    # import math
    # Print the value of pi
    # print (math.pi)
    # 1rad = 57.2958 degree
    # Angle in Radians × 180°/π = Angle in Degrees. 
    # For example, consider an angle π/9 rad. 
    # Now, using the radians to degrees formula, we have π/9 rad × 180°/π = (Angle in Degrees).


# def convertion_rad_to_degree():
#     pi=22/7
#     radian = float(input("Input radians: "))
#     degree = radian*(180/pi)
#     print(degree)

# convertion_rad_to_degree()


def convertion_rad_to_degree(radian):
    import math
    pi=math.pi
    degree = radian*(180/pi)
    return degree

x = float(input("Input radians: "))
degree = convertion_rad_to_degree(x)
print(degree)