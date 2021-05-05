class Number:

    def sum(self,a,b):
        return a +b
    def difference(self,a,b):
        return a-b
    def product(self,a,b):
        return a*b
    def divide(self,a,b):
        return a/b    
    def remainder(self,a,b):
        return a%b    
    def power(self,a,b):
        return a**b  
    def unroot(self,a,b):
        return a**(1/b)     
 
choice="yes"
print("========Welcome to my Calculator==========")
while choice=="yes":

    print("METHODS\t\t\tBUTTONS\naddition\t\tpress (+)\nsubstractio\t\tpress (-)\ndivision\t\tpress (/)\nmultiplication\t\tpress (*)\nmodulus\t\t\tpress (%)\npowers\t\t\tpress (**)\nunderroots\t\tpress (**.)\n")
    choice=input("Enter your choice:")
    num=Number()
    if choice=="+":
        a=int(input("Enter the first number\n"))
        b=int(input("Enter the second number\n"))
        s=num.sum(a,b)
        print(f"Addition of {a} and {b} is",s)
    elif choice=="-":
        a=int(input("Enter the first number\n"))
        b=int(input("Enter the second number\n"))
        d=num.difference(a,b)
        print(f"Difference of {a} and {b} is",d)
    elif choice=="/":
        a=int(input("Enter the first number\n"))
        b=int(input("Enter the second number\n"))
        di=num.divide(a,b)
        print(f"Division of {a} and {b} is",di)  
    elif choice=="*":
        a=int(input("Enter the first number\n"))
        b=int(input("Enter the second number\n"))
        p=num.product(a,b)
        print(f"Product of {a} and {b} is",p)
    elif choice=="%":
        a=int(input("Enter the first number\n"))
        b=int(input("Enter the second number\n"))
        m=num.remainder(a,b)
        print(f"Division of {a} and {b} is",m) 
    elif choice=="**":
        a=int(input("Enter the number\n"))
        b=int(input("Enter the power you want to find\n"))
        pw=num.power(a,b)
        print(f"{a} to the power {b} is",pw)  
    elif choice=="**.":
        a=int(input("Enter the number\n"))
        b=int(input("Enter the root you want to find\n"))
        un=num.unroot(a,b)
        print("Root is",un)  
    else:
        print("Wrong button pressed \n see from chart") 
    choice=input("Do you want to access this calculator again(yes,no)")