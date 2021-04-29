'''Q1 WAP to create a dictionary of words with values as 
 their as their english translation provide user with 
 an option to look it up!
 myDict={'kapda':'cloth','dabba':'box','dandi':'stick',
         'jute':'shoes','bistar':'bed' 
}'''

# print("The options are:\n",myDict.keys())
# w=input("Enter the word in hindi\n")
# print("The meaning of your word is:",myDict[w])

'''Q2 WAP to input 8 numbers from the user and display 
all the unique(set) number once'''
# num1=int(input("Enter Number 1"))
# num2=int(input("Enter Number 2"))
# num3=int(input("Enter Number 3"))
# num4=int(input("Enter Number 4"))
# num5=int(input("Enter Number 5"))
# num6=int(input("Enter Number 6"))
# num7=int(input("Enter Number 7"))
# num8=int(input("Enter Number 8"))
# s={num1,num2,num3,num4,num5,num6,num7,num8}
# print(s)

'''Q3 Can we have a set with 18(int) and "18"(string) as a
value in it?'''
# s={18,"18"}
# print(s)              #output: {'18', 18}

'''Q4 whatwill be the length of the following set s
   s=set()
   s.add(20)
   s.add(20.0)
   s.add("20")'''
# s=set()
# s.add(20)
# s.add(20.0)
# s.add("20")
# print(len(s))              #output: 2

'''Q5 What is the tpe of s'''
# print(type(s))             #output: <class 'set'>

'''Q6 Create an empty dictionary allow 4 freinds to enter their 
favourite language as values and use keys as their names.Assume
that the name are unique'''

# mydict={}
# f1=input('Ramesh enter your fav language\n')
# f2=input('Suresh enter your fav language\n')
# f3=input('Dinesh enter your fav language\n')
# f4=input('Ganesh enter your fav language\n')
# mydict['Ramesh']=f1
# mydict['Suresh']=f2
# mydict['Dinesh']=f3        
# mydict['Ganesh']=f4      
# print(mydict) 

'''Q7 if names of 2 freinds are same ; what will
happen to the program in problem 6'''
#ans in such a case the key will overwrite and will
#consider the latest value 

'''Q8 if languages of 2 freinds are same ; what will
happen to the program in problem 6'''
# #ans in such case it will print the sam language 
# for both the names

'''Q9 Can you change the values inside a list which is 
 contained in a set s ={8,7,12,"harshit",[1,4,3]}'''
# s ={8,7,12,"harshit",[1,4,3]}
# print(s)                    #Output: throws an error and we cannot change 
                              #the list inside it
