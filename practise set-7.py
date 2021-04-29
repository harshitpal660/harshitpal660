'''Q1 WAP to print multiplication table of a given number
using for loop'''

# num=int(input("Enter a number\n"))
# for i in range(0,num*10+1,num):
#     print(i)

# #Another way to do that
# num=int(input("Enter a number\n"))
# for i in range(1,11):
#     print(str(num)+"x"+str(i)+"="+str(i*num))

# num=int(input("Enter a number\n"))
# for i in range(1,11):
#      print(f"{num}x{i}={num*i}")

'''Q2 WAP to greet all the person names stored in a list l1
and wich starts with s
l1=['harshit','sohan','sachin','rahul']'''

# l1=['harshit','sohan','sachin','rahul']

# for name in l1:
#     if name.startswith("s"):
#         print("Hello "+name)

'''Q3 WAP to print multiplication table of a given number
using for loop'''

# num=int(input("Enter a number\n"))
# i=1
# while i<=10:
#     print(f"{num}x{i}={num*i}")
#     i=i+1

'''Q4 WAP to find weather a given number is prime or not'''

# num=int(input("Enter a number"))
# prime=True
# for i in range(2,num-1):
#     if(num%i==0):
#         print(f"{num} is divisible by {i}")
#         prime=False
#         break
# if prime:
#      print(f"{num} is a prime")
# else:
#      print(f"{num} is not a prime number")

'''Q5 WAP to find the sum of first n natural numbers using
while loop'''

# n=int(input("Enter the limit of natural number"))
# i=1
# sum=0
# while i<=n:
#     i=i+1
#     sum=sum+i
# print("the sum is",sum)

'''Q6 WAP to calculate the factorial of a given number 
using for loop'''

# num=int(input("Enter an number\n"))
# fact=1
# for i in range(1,num+1):
#     fact=fact*i
# print(f"Factorial of {num} is",fact)

''' Q7 WAP to print the following star pattern
*
* * 
* * * '''
    
# n=int(input("Enter the value of n\n"))
# for i in  range(1,n+1):
#     print("*"*(i))

'''Q8 WAP to print the following star pattern
  *
 ***
*****'''

# n=int(input("Enter the value of n\n"))
# for i in  range(0,n):
#      print(" "*(n-i-1),end="")
#      print("*"*(2*i+1),end="")
#      print(" "*(n-i-1))

'''WAP to print multiplication table in reverse order'''
# num=int(input("Enter the number whose table you want to print"))
# for i in range(10,1):
#      print(f"{num}x{i}={num*i}")
 