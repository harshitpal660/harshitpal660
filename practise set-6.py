'''Q1 WAP to find greatest of four numbers entered by user'''
# num1 =int(input("Enter the number 1"))
# num2 =int(input("Enter the number 2"))
# num3 =int(input("Enter the number 3"))  
# num4 =int(input("Enter the number 4"))  

# if (num1>num2):
#     f1=num1
# else:
#     f1=num2

# if (num3>num4):
#     f2=num3
# else:
#     f2=num4

# if(f1>f2):
#     print(f1,"is greatest")
# else:
#     print(f2,"is greatest")

'''Q2 WAP to find out whether a student is pass or fail,if it requires total
40% and at least 33% in each subject to pass. Assume 3 subjects and take 
marks as an input from the user'''

# sub1=int(input("Enter marks\n"))
# sub2=int(input("Enter marks\n"))
# sub3=int(input("Enter marks\n"))

# if(sub1<33 or sub2<33 or sub3<33):
#     print('''You are fail because you have less than 33% in one of the subjects''')
# elif(sub1+sub2+sub3)/3<40:
#     print('''You are fail due to total percentage less than 40''')
# else:
#     print('''Congratulation! You have passed the exam''')

'''Q3 A spam comment is defined as a text containing following keyword
"make a lot of money","buy now","subscribe this","click this".Write a 
program to detect these spams.'''

# text=input("Enter the text")
# spam=False
# if("make a lot of money"):
#     spam=True
# elif("buy now"):
#     spam=True
# elif("subscribe this"):
#     spam=True
# elif("click this"):
#     spam=True
# else:
#     spam=False

# if (spam):
#     print("This text is a spam")
# else:
#      print("This text is not a spam")

'''Q4 WAP to find whether a given username contains less than 10 characters 
or not'''
# username=input("Enter your Username\n")
# if(len(username)<10):
#     print("Username is less than 10 character")
# else:
#     print("Username is more or equal 10 character")

'''Q5 WAP to find out whether a given name is present in a list or not'''
# namelst=['shivani','gaurav','harshit','shreya','divyanshi','golu','dittu']
# name=input("Enter the name of your choice\n")
# for i in range(len(namelst)):
#     if(name==namelst[i]):
#         print(name,"is present in the list")
#     else:
#        continue
#EASY WAY TO DO THE SAME PROGRAM
# namelst=['shivani','gaurav','harshit','shreya','divyanshi','golu','dittu']
# name=input("Enter the name of your choice\n")
# if name in namelst:
#      print("Your name is present in the list \n")
# else:
#     print("Your name is present in the list \n")

'''Q6 WAP to calculate the grade of a student from his marks from the following
scheme
     90-100 ->Ex
     80-90 ->A 
     70-80 ->B 
     60-70 ->C 
     50-60 ->D
      <50  ->F'''
                
# marks=int(input("Enter the marks of the student\n"))

# if(90<marks<=100):
#     print("You are excellent\n")
# elif(80<marks<=90):
#     print("You got A")
# elif(70<marks<=80):
#     print("You got B")
# elif(60<marks<=70):
#     print("You got C")
# elif(50<marks<=60):
#     print("You got D")
# else:
#     print("failed")

'''Q7 WAP to find out whether a given post is talking about 
"Harshit or not" '''

