#
# Example file for variables
#

# Declare a variable and initialize it

f = 0
# print(f)


# # re-declaring the variable works
# f="abc"
# print(f)

# # ERROR: variables of different types cannot be combined
#print("String" + str(123))

# Global vs. local variables in functions
def someFunction():
    global f
    f = "DEF"
    print(f)


someFunction()
print(f)

del f
print(f)
