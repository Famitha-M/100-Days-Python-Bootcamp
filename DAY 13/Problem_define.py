def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")


my_function()

# Describe the Problem - Write your answers as comments:
'''
the goal is to print you got it once the current index of for loop hits 20 means equals to 20
but here the current index wont hit 20 as the range function is build different
'''
# 1. What is the for loop doing?
"""
in for loop as we defined range start from 1,20 so it actually hits till 19 only
"""
# 2. When is the function meant to print "You got it"?
"""
once the current item i is equals to 20
"""
# 3. What are your assumptions about the value of i?
"""
so we can assume the current item i should have 20 so we gonna change the value of the range function so that we can get the output
"""

#solution
def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")


my_function()
