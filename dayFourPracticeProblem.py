#Question 1
#Heads or Tails
import random
int_random = random.randint(0,1)
print(int_random)


#Question 2
#BANKER ROULETTE
names_string = ["tejas","shweta","kanha","anvi","abhi"]
names = names_string.split(", ")
# The code above converts the input into an array separating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
import random
# len_name = len(names)
# random_name = random.randint(0,len_name)

bill_name = names[random.randint(0,len(names)-1)]
print(f"{bill_name} is going to buy the meal today!")


#Question 3
#Treasure Map
