
# # #Question 1
# # #BMI 2.o

# # # # Enter your height in meters e.g., 1.55
# # # height = float(input())
# # # # Enter your weight in kilograms e.g., 72
# # # weight = int(input())
# # # # 🚨 Don't change the code above 👆

# # # #Write your code below this line 👇
# # # Bmi = weight/(height**2)

# # # if(Bmi<18.5):
# # #   print(f"Your BMI is {Bmi}, you are underweight.")
# # # elif(Bmi<25):
# # #   print(f"Your BMI is {Bmi}, you have a normal weight.")
# # # elif(Bmi<30):
# # #   print(f"Your BMI is {Bmi}, you are slightly overweight.")
# # # elif(Bmi<35):
# # #   print(f"Your BMI is {Bmi}, you are obese.")
# # # else:
# # #   print(f"Your BMI is {Bmi}, you are clinically obese.")


# # #Question 2
# # # Leap Year

# # # Which year do you want to check?
# # # year = int(input())
# # # # 🚨 Don't change the code above 👆

# # # # Write your code below this line 👇

# # # if(year%4==0):
# # #   if(year%100 == 0):
# # #     if(year%400 == 0):
# # #       print("Leap year")
# # #     else:
# # #       print("Not leap year")
# # #   else:
# # #     print("Leap year")
# # # else:
# # #   print("Not leap year")
    

# # # Question 3
# # # Pizza Order

# # print("Thank you for choosing Python Pizza Deliveries!")
# # size = input() # What size pizza do you want? S, M, or L
# # add_pepperoni = input() # Do you want pepperoni? Y or N
# # extra_cheese = input() # Do you want extra cheese? Y or N
# # # 🚨 Don't change the code above 👆
# # # Write your code below this line 👇
# # total_bill = 0
# # if(size=='S'):
# #   total_bill = total_bill + 15
# #   if(add_pepperoni=='Y'):
# #     total_bill = total_bill + 2
# #   if(extra_cheese=='Y'):
# #     total_bill = total_bill + 1
# #   print(f"Your final bill is: ${total_bill}.")
# # if(size=='M'):
# #   total_bill = total_bill + 20
# #   if(add_pepperoni=='Y'):
# #     total_bill = total_bill + 3
# #   if(extra_cheese=='Y'):
# #     total_bill = total_bill + 1
# #   print(f"Your final bill is: ${total_bill}.")
# # if(size=='L'):
# #   total_bill = total_bill + 25
# #   if(add_pepperoni=='Y'):
# #     total_bill = total_bill + 3
# #   if(extra_cheese=='Y'):
# #     total_bill = total_bill + 1
# #   print(f"Your final bill is: ${total_bill}.")


# #Question 4
# #Love parameter

# print("The Love Calculator is calculating your score...")
# name1 = input() # What is your name?
# name2 = input() # What is their name?
# # 🚨 Don't change the code above 👆
# # Write your code below this line 👇

# def cal(name):
#   cal_ture = sum(name.count(letter) for letter in "TURE")
#   cal_love = sum(name.count(letter) for letter in "LOVE")
#   return cal_ture,cal_love

# p1_true,p1_love = cal(name1.upper())
# p2_true,p2_love = cal(name2.upper())

# result_true = p1_true + p2_true
# result_love = p1_love + p2_love

# result = int(str(result_true) + str(result_love))

# if(result<=10 or result>=90):
#   print(f"Your score is {result}, you go together like coke and mentos.")  
# elif(result>=40 and result<=50):
#   print(f"Your score is {result}, you are alright together.")
# else:
#   print(f"Your score is {result}.")

#Question 5
# Treasure Hunt
import secrets
import string
print("Wlecome to the Treasure Hunting...")

print("")
choices = int(input("Please select the given option \n \t1. left \t2. rigth \n"))

if(choices == 1):
    choices = int(input("Select one of action from below \n \t1. wait \t2. swim \n"))
    if(choices==1):
        choices = int(input("Select the treasure door \n \t1. Red \t2. Yellow \t3.Blue \n"))
        if(choices==1):
            print("Game Over")
        elif(choices == 2):
            print("YOU WON!!")
        else:
            print("Game Over")
    else:
        print("Game Over")
else:
    print("Game Over")