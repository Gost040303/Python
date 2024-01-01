# #Question 1
# #Heads or Tails
# import random
# int_random = random.randint(0,1)
# print(int_random)


# #Question 2
# #BANKER ROULETTE
# names_string = ["tejas","shweta","kanha","anvi","abhi"]
# names = names_string.split(", ")
# # The code above converts the input into an array separating
# #each name in the input by a comma and space.
# # 🚨 Don't change the code above 👆
# import random
# # len_name = len(names)
# # random_name = random.randint(0,len_name)

# bill_name = names[random.randint(0,len(names)-1)]
# print(f"{bill_name} is going to buy the meal today!")


# #Question 3    
# ///IMP  2 ways to do this question
#  i) list with 'ord' ii) dictionary
# #Treasure Map

# line1 = ["⬜️", "⬜️", "⬜️"]
# line2 = ["⬜️", "⬜️", "⬜️"]
# line3 = ["⬜️", "⬜️", "⬜️"]
# map = [line1, line2, line3]
# print("Hiding your treasure! X marks the spot.")
# position = input("Where do you want to put the treasure? ")  # Where do you want to put the treasure?


# Type 1 
# Define a dictionary to map letters to indices
# letter_to_index = {'A': 0, 'B': 1, 'C': 2}
# Use the dictionary to get the item index.
# Convert input position to indices
# list_index = int(position[1]) - 1  # Convert number to list index
# item_index = letter_to_index[position[0]]  
# # Place the treasure at the specified position
# map[list_index][item_index] = "X"
# # Display the updated map
# print(f"{line1}\n{line2}\n{line3}")


# Type 2
# Convert input position to indices
# list_index = int(position[1]) - 1  # Convert number to list index
# item_index = ord(position[0]) - ord('A') 
# # Place the treasure at the specified position
# map[list_index][item_index] = "X"
# # Display the updated map
# print(f"{line1}\n{line2}\n{line3}")

# Question 4 
# Rock, Paper, Scissor

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choose_list = [rock,paper,scissor]

player_choose = int(input("What do you choose?\n 0 for rock, 1 for paper, 2 for scissor\n"))
computer_choose = random.choice(choose_list)
print("Computer Choose: \n" + computer_choose)
if(computer_choose != player_choose):
    print(f"Player choose: \n{player_choose}")
    if(computer_choose==rock and player_choose==1):
        print(paper + "\n YOU WIN!!!")
    elif(computer_choose==rock and player_choose==2):
        print(scissor + "\n YOU LOSE!!!!!")
    elif(computer_choose==paper and player_choose==2):
        print(scissor + "\nYOU WIN!!!")
    elif(computer_choose==paper and player_choose==0):
        print(scissor + "\n YOU LOSE!!!!!")
    elif(computer_choose==scissor and player_choose==0):
        print(rock + "\n YOU WIN!!!")
    else:
        print(paper + "\n YOU LOSE!!!!!")
else:
    print(f"Player Choose: \n{player_choose}")
    print("Tie")