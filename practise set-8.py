'''Q1 WAP using function to find the greatest of three numbers '''

# def greatest(a,b,c):
#     if a>b:
#         if a>c:
#             print(f"{a} is greatest\n")
#         else:
#             print(f"{c} is greatest\n")
#     elif b>a:
#         if b>c:  
#             print(f"{b} is greatest\n")
#         else:
#             print(f"{c} is greatest\n")   
 
# a=int(input("Enter first number\n"))
# b=int(input("Enter second number\n"))
# c=int(input("Enter third number\n"))
# print(greatest(a,b,c))

'''Q2 WAP using function to convert celsius to fahrenheit'''

# dfahrenheit(c):
#     f=(c * (9/5)) + 32 
#     return f

# c=int(input("Enter temperature in celsius\n"))
# print(fahrenheit(c),end="\n")
# print("Thank you")ef 

'''Q3 How do you prevent a python print() function to print
a new line at the end '''
# print("Hello",end=" ")
# print("How",end=" ")
# print("are",end=" ")
# print("you?",end=" ")

'''Q4 Write a recursive function to calculate the sum of first 
n natural numbers'''
# def sum(n):
#     if n==0:
#         return 0
#     return(n+sum(n-1))
# n=int(input("Enter the number \n"))
# print(sum(n))

'''Q5 Write a python function to print first n lines of the following pattern
****
***
**
*'''

# def pattern(n):
#     for i in range(n):
#         print("*"*(n-i))

# n=int(input("Enter no of stars you want to print\n"))
# print(pattern(n))

'''Q6 Write a python function which converts inches to cms'''
#multiply the length value by 2.54

# def convert(n):
#     return(n*2.54)

# n=int(input("Enter the value you want to convert\n"))
# print("After converting inches to centimeter we get",convert(n))

'''Q7 Write a python function to remove a given word from a list
and strip it at the same time'''

# def remove_strip(string,word):
#     newstr=string.strip()
#     return newstr.replace(word," ")

# word=(input("Enter the word you want to remove\n"))
# string="     harshit is a good boy   "
# print(remove_strip(string,word))

'''Q8 Write a python function to print multiplication table of a given 
number'''
# def multiplication(n):
#     for i in range(1,11):
#         print(f"{n}x{i}={n*i}")
# num=int(input("Enter a number\n"))
# print(multiplication(num))