# a = 15
# b = 10
# c = 5

# if(a>b):
#     print("a greater than b")
# if(b<c):
#     print("b greater than c")
# if(a>c):
#     print("a greater than c")


import random

# Define the options
option_left = "Next Option"
option_right = "Game Over"

# Randomly decide the placement of choices
if random.choice([True, False]):
    option_left, option_right = option_right, option_left

# Print the result
print(f"Left: {option_left}")
print(f"Right: {option_right}")
