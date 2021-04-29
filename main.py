'''# my first python program
import cv2
import math


this is a multiline comment ,syntax differs from other programming 
language but need not to worry (:

print("Hello world\n")

print(math.gcd(80,100))

#print(5+8)

a=56
b="HARSHIT"
c=45.867
print(a+c)
print(b)

# function to print the data type of a variable
typeA=type(a)  
print(typeA)

# function  to check a particular class of a variable
print(isinstance(c,int))
#output=false

#type casting- converting data from one data type to other
d="54"
d=int(54)
print(type(d))
print(d+2)
#you can do this same step by another way too
d=int(d)
print(type(d))
print(d+2)
e=45
e=float(e)
print(e+4)
#a=87
#b="65"
#c=34.9999
#a=float(a)
#print(a)
#a=str(a)
#print("87")
#c=str(c)
#print(c)
#c=int(c)
#print(c)
#b=float(b)
#print(b)
#b=int(b)
#print(b)'''


#complex numbers
#c=6+2j
#print(8+c)
#print(isinstance(c,complex))
#output=14+2j and true

#multiline comments can also be use to 
#store group of strings or a sentence

#name='''my name is harshit I studied in gyan ganga college of technology''' 
#print(name)

#print(name[8])   #print the alpabet of a string wich is at 7th index
#output = i
#print(name[7:24])  #slicing operator(:) used to slice an give string
#print(name.strip())  #atumatically delete extraa space left before and after strind
#print(len(name)) #length function

#name="harshit"
#name=name.upper() #converts string to upper case letters
#print(name)       
#name=name.lower() #converts string to lower case letters
#print(name)
#var=name.replace("r","s") #replace to alphabets of a string
#print(var)
#var=name.replace("arsh","s")
#print(var)
#name='shivani ,harshit ,shreya ,golu'
#print(type(name))
#var=name.replace(",","\n")
#print(var)

#stri1='hello eveyone, '  #cancatenation adding two string
#stri2='I am Harshit'
#print(stri1+stri2)

#n1="harshit"
#n2="python"
#sent="i am {1} and i am {0} learner".format(n1,n2)
#sent=f"i am {n2} and i am {n1} learner"
#print(sent)

#some basic operations
#a=845
#b=20
#c=a/b
#c=int(c)
#d=a**b      #exponential operator
#e=a//b      #floor division operator   
#print(a+b)
#print(a-b)
#print(a*b)
#print(c)
#print(type(c))
#print(a%b)

#some advance operations(**,//,%)
#print(d)          
#print(type(d)) 
#print(e) 

#skip character
# name="harshit pal is a good boy"
# print(name[0::2])      #output : hrhtpli  odby
# print(name[0:25:1])    #output : harshit pal is a good boy
# print(name[0:25:4])    #output : hhpi dy
'''
Python Collections:
1. List
2. Tuple
3. set
4. Dictionary

'''

#LIST
'''Python offers a range of compound datatypes often reffered to as 
sequesnces.List is one of the most frequently used and very versatile
data types used in Python'''

#HOW TO CREATE A LIST
#lst=[]
#print("empty list",lst)                        #empty list
#lst=[1,2,3,4,]
#print("list of integers",lst)                  #list of integers
#lst=[3,"hello",4.8]
#print("list with mixed data types",lst)        #list with mixed data types
#lst1=["mouse",[3,5,6],['python']]
#lst2=["mouse",[3,5,6],'python']
#print("nested list",lst)                       #nested list

#lst=[34,5,4,2,214,6]
#ACCESS OF LIST ELEMENTS
#var=type(lst)
#print(var)
#print(lst)
#print(lst1[2])                                   #for printing a particular element
#output=['python']
#print(lst1[0][3])
#output=s
#print(lst1[2][2])
#output=error cuz there is only one element wich is ['python']
#print(lst1[2][0][2])
#output=t
#print(lst2[2][3])

#NEGATIVE INDEXING
#lst=[3,'e',4,'r',2,'lol','fish',]
#print(lst[-1][3])
#output=h
#print(lst[-2])
#output=lol

#SLICING THE LIST
#lst=['p','r','o','g','r','a','m']
#print(lst[1:4])                                #slicing operator(:)
#output=['r','o','g']
#print(lst[:-5])
#output=['p','r']
#print(lst[-5:])
#output=['o','g','r','a','m']
#print(lst[5:])
#output=['a','m']
#print(lst[:])

#ADD/CHANGE AND DELETE THE LIST ELEMNTS
# lst=[43,51,71,5,14,42]
# lst[4]=95
# print(lst)
# del lst[3]                 #deletes the element from a particular positions
# print(lst)
# print(lst[2:7])
#output=[71, 95, 42]

#PYTHON METHODS
#print(len(lst))
#lst.append(100)            #insert 100 at last position of the list
#print(lst)
#lst.extend([132,145,154])
#print(lst+[21,54,626,533])  #concatenating operator
#print(["harshit"]*5)        #(*) operator repeates the lists
#print(lst)
#lst.insert(0,33)           #insert 100 at 1st position
#print(lst)
#lst.pop()                  #deletes the last element of the list 
#print(lst)            
#lst.clear()
#var=lst
#print(var)



#TUPLE
'''A Tuple in python is similar to a list. The difference between the 
two is that we cannot change the element of a tuple once it is assigned
whereas we can change the elements of a list.'''
#CREATING THE TUPLE

#t=()                         #empty tuple
#print("empty tuple",t)
#t=(1,2,3,4)                  #integer tuple
#print("integer tuple",t)
#t=(3,'hii how are you',66.7)  #mixed tuple
#print("mixed data types",t)
#print(type(t[1][3]))
#t=("mouse",[3.31,53,51,867],(2,5,7,1))
#print("nested tuple",t)           #nested tuple  

#t=3,4.6,"dog"
#print(type(t))
#print(t)

#t=("Harshit",)
#t[1]="vikrant"         #cannot do this cuz tuple cannot be allowed to change
#t=list(t)
#t[2]="Vikrant"
#print(type(t))
#print(t)

#INDEXING
#nested tuple
#n=("mouse",[8,7,0,3],[6,3,1])

#nested index
#print(n[0][4])
#print(n[2][1])
#print(n[-1][-3])     #negative indexing

#SLICING
#my_tuple = ('p','r','o','g','r','a','m','i','z')
#print(my_tuple[1:4])
#print(my_tuple[0:2])
#print(my_tuple[:-7])
#print(my_tuple[7:])
#print(my_tuple[:])

#CHANGING TUPLE 
#t=(2,4,1,[7,6])
#t[2]=5
# TypeError: 'tuple' object does not support item assignment
#t[3][0]=9
#print(t)                   # Output: (4, 2, 3, [9, 5]
# However, item of mutable element can be changed
#t=('p','r','o','g','r','a','m')
#tuples can be reassigned
#print(t)

#concatenation
#print((1,6,3)+(8,5,3))
#output=(1,6,3,8,5,3)
#print(('Repeat')*5)
# Output: ('Repeat', 'Repeat', 'Repeat','Repeat','Repeat)

#DELETING A TUPLE
#t=('p','r','o','g','r','a','m')
#del t[5]
# can't delete items
# TypeError: 'tuple' object doesn't support item deletion
# del my_tuple[3]
#del t
# Can delete an entire tuple
#print(t)

#TUPLE METHODS
#count operations
#t=('p','r','o','g','r','a','m')
#print(t.count('p'))      #output=1
#print(t.count('r'))      #output=2

#tuple membership test 
#print('c'in t)
#print('m'in t)

#iterating through tuple
#using for loop to iterate through touple
#for name in('john','kate'):   
     #print("hello",name)


#SETS
'''A set is  a collection of items. Every set element is unique 
(no duplicates) and must immutable(cannot be changed). 

However,
a set itself is mutable. We can add or remove items from it.

Sets can also be used to perform mathematical set operations like
union,intersection,symmetric difference,etc.'''

#CREATING PYTHON SET 

#different types of set in python
# s=set()                      #empty set
# print(type(s))
#adding values to an empty set
# s.add(4)
# s.add(5)
# s.add(5)
# s.add(4)
# s.add(4)
# s.add(5)
# print(s)
#set of integer
#s={2,6,23,2,6,42,4}
#print(s)                         #output={2,4,6,23,42}
#set of mixed datatypes
#s={31.5,"Hello",(4,3,2,1)}
#print(s)                        #output={"Hello",(4,3,2,1),31.5}

#We can make set from a list using set() function
#s=set([43,66,1,7286,53,6])
#print(s)

# set cannot have mutable items
# here [3, 4] is a mutable list
# this will cause an error.
#s = {1, 2, [3, 4]}

# Distinguish set and dictionary while creating empty set
# initialize a with {}
#a = {}                       #Output=<class 'dict'>
# check data type of a
#print(type(a))
# initialize a with set()
#a = set()
# check data type of a
#print(type(a))               #Output=<class 'set'>

#modifying a set in python
#s={4,21,6}
#print(s)

# s[0]
# if you uncomment the above line
# you will get an error
# TypeError: 'set' object does not support indexing

#s.add('harshit')
#print(s)

#s.update(["shreya","golu"])
#print(s)
#s.update([5,6],{7,8})
#print(s)

#s=set("helloworld")
#print(s)
#s.discard(8)
#print(s)
#s.remove(9)
# not present in my_set
# you will get an error.
# Output: KeyError
#s.pop()
#print(s)

#s.clear()
#print(s)

#SET OPERATION
#union(|)
#A=set([3,5,6,3,7,8])
#B=set([1,2,5,6,4,7])

#print(A|B)
#print(B.union(A))
 
#print(A&B)
#print(A.intersection(B))

# Difference of two sets
#A = {1, 2, 3, 4, 5}
#B = {4, 5, 6, 7, 8}

# use - operator on A
# Output: {1, 2, 3}
#print(A - B)
#print( A.difference(B))

# Symmetric difference of two sets
# use ^ operator
# Output: {1, 2, 3, 6, 7, 8}
#print(A ^ B)
#print(A.symmetric_difference(B))

#s=set("apple")

#print('s'  in s)
#print('a' in s)


#DICTIONARY
'''Python dictionary is an unorderd collection of items. Each item of 
a dictionary has a key/value pair

Dictionaries are optimized to retrieve values when the key is known.'''

#creating python dictionaries
#d={}              #empty dictionary
#print(d)
#d={1:'apple',2:'banana'}         #dictionaries with integers
#print(d[1])
#d={'name':'John',1:[3,5,62,4]}        
#print(d)
'''values can be of any data types and can repeat,keys must be of 
immutable type(string,number or tuple with immutable ellements) and
must be unique.'''
#d=dict({1:"apple",2:"banana"})
#print(d)
#d=dict([('a',43),('b',53),('c',63)])
#print(d)

#accessing elements from dictionary
# d=dict({1:"apple",2:"banana"})
# print(d[1],d[2])
# print(d.get(2))
'''If we use the square brackets [], KeyError is raised in case a key
 is not found in the dictionary. On the other hand, the get() method 
 returns None if the key is not found. '''
#print(d.get(3))                 # Output None
#print(d[3])                     # KeyError

#changing and adding dictionary elements
#d={
# 'name':'Harshit pal',
#  'age': 19,
#   'studies':'B.Tech',
#    'location': 'jabalpur',
#     'h.no': 941
#}
#d['age']=20
#print(d)
#d['address']='kanchghar'
#print(d)

#Removing elements from a dictionary
#ksquares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# print(squares.pop(4))
# print(squares)
# print(squares.popitem())              # Output: (5, 25)
# remove all items
#squares.clear()
# Output: {}
#print(squares)

# delete the dictionary itself
#del squares
# Throws Error
#print(squares)

#Dictionary methods
#squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# print(list(squares.keys()))
# print(tuple(squares.keys()))
# print(set(squares.keys()))
# print(list(squares.values()))
# print(tuple(squares.keys()))
# print(set(squares.items()))

# updatesquares={6: 36,7: 49}
# squares.update(updatesquares)
#uppdate the dictionary by adding key-value pairs from updateDict
# print(squares)
# print(squares.get(8)) #not throw error return none

#import keyword
#print(keyword.kwlist)     
#it will print all the key word present in this version of python

'''IS AND IN statements in python'''
# a=None
# if(a is None):
#      print("Yes")
# else:
#      print("No")

# lst=[43,5,2,64,2,6,36,5]
# print(3 in lst)