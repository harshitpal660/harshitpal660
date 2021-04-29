#conditional statements in python
'''they are of three types
1. If statement
2. If else statement
3. If elif else statement
'''
#if statements
#(If the number is positive, we print an appropriate 
# message)

# nf num>0:
#  um=5
# i    print(num,"is a positive number.")
# print("This is always printed.")

# num=-7
# if num>0:
#      print(num, "is a positive number.")
# print("This is also always printed.")

#If else statements
#(Program checks if the number is positive or negative
# And displays an appropriate message)
# num=int(input("enter a number\n"))
# if num>=0:
#      print("Positive or Zero")
# else:
#      print("Negative number")

#If elif else statement
'''In this program, 
we check if the number is positive or
negative or zero and 
display an appropriate message'''
# num=int(input("enter a number\n"))
# if num>0:
#      print("positive number")
# elif num<0:
#      print("negative number")
# else:
#      print("negative")

#Nested if statement
'''In this program, we input a number
check if the number is positive or
negative or zero and display
an appropriate message
This time we use nested if statement'''

# num=float(input("Enter a number: "))
# if num>=0:
#      if num>0:
#           print("Positive number")
#      else:
#           print("Zero")
# else:
#      print("Negative number") 

#WAP to print yes when the age entered by the user is greater than or equal
#to 18

# age=int(input("Enter your age\n"))

# if age>=18:
#     print("yes")
# else:
#     print("no")