# def percentage(marks):
#     return((marks[0]+marks[1]+marks[2]+marks[3]+marks[4])/500)*100

# marks1=[45,78,86,77,85]
# percent1=percentage(marks1)

# marks2=[64,68,95,87,79]
# percent2=percentage(marks2)

# print(percent1)
# print(percent2)

# def greet():
#     return("Good Morning \n")
    

# name=input("Enter user Name\n")
# g=greet()
# print(g+name) 

'''RECURSION is a condition when function calls itself recursively(continuously)'''

# n=int(input("Enter the number whose factor we need to find\n"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)

'''RECURSION logic 
n!=1*2*3*4*5.......*n
n!=(1*2*3*4*5......n-1)*n
n!=(n-1)!*n'''

# def factorial_recursive(n):
#     if n==1 or n==0:
#         return 1
#     return n*factorial_recursive(n-1)
# n=int(input("Enter the number whose factor we need to find\n"))
# f=factorial_recursive(n)
# print(f)  

  