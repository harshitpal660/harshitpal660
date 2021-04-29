'''my first game project on python'''
import random
def game(comp,user):
    if comp==user:
        print("its a tie!")
    elif comp=="s":
        if user=="w":
            print("Computer Win")
        else:
            print("User Win")
    elif comp=="w":
        if user=="g":
            print("Computer Win")
        else:
            print("User Win")
    else:
        if user=="s":
            print("Computer Win")
        else:
            print("User Win")
    
print("\n================Welcome to the World of fight================")
randno=random.randint(1,3)    #gives a random value of between 1 to 3

if randno==1:                 #converting 1=s,2=w,3=g
    comp="s"
elif randno==2:
    comp="w"
else:
    comp="g"

#user will enter his choice
user=input("Chose between Snake(s),Water(w)and Gun(g)??\n")
#printing the random choice selected by computer            
print("Computer choice:",comp)
print(game(comp,user))

    