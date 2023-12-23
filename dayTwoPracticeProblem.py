
# Question 1

# strs = input("")
# new_num1 = int(strs[0])
# new_num2 = int(strs[1])
# addNum1 = new_num1 + new_num2
# print(addNum1)

# # can be done with taking integer as input also

# num = input( )
# new_num1 = int(num[0])
# new_num2 = int(num[1])
# addNum2 = new_num1 + new_num2
# print(addNum2)

#Question 2

# Tip calculator
print("Welcome to Tip calculator.") 
bill = float(input("What is cost of bill? $"))
print("$",bill)
tip = int(input("What percent of tip you would like to give 10, 12 or 15? "))
print(tip)
totalPeople = int(input("Total Number of people for slipting bill? "))
print(totalPeople)
newBill = bill + (tip*bill)/100
slipt = round(newBill/totalPeople,2)
print(f"Each person should pay {slipt}")