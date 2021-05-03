'''my second game chota Pubg'''
import random
class Game:
    game="COD"
    def __init__(self,Nation,guns,health,sound):
        self.Nation=Nation
        self.guns=guns
        self.health=health
        self.sound=sound
    # def motion(self,river,gun,mountain):
    #     self.gun=gun
    #     self.river=river
    #     self.mountain=mountain
    # def buttons(self,r_Pressed,g_Pressed,m_Pressed):
    #     self.r_Pressed=r_Pressed
    #     self.g_Pressed=g_Pressed
    #     self.m_Pressed=m_Pressed
    
    def show_skills(self):
        print(f"COUNTRY :{self.Nation}\t GUNS :{self.guns}\t HEALTH :{self.health}\t SOUND:{self.sound}\t")

def chose():
    t=input("Chose your team(India,Pakistan)\n")
    if t=="India":
        print("YOU are awesome and you always win!\n")
    else:
        print("Abe cuhtiya harega\n")
        
   
print("\n Loading........")
p1=Game("India","IMI Negev","100%","Vande Matram")
p2=Game("Pakistan","AK 47","100","Tatti hai hmm")
print("COMPARISON player1 vs player2\n")
p1.show_skills()
p2.show_skills()
print(chose())
print("\n================Welcome to the World of fight================")
rand_choice=random.randint(1,3)        #gives a random value of between 1 to 3

if rand_choice==1:                               #converting 1=s,2=w,3=g
    rand_choice="r"
elif rand_choice==2:
    rand_choice="p"
else:
    rand_choice="s"
    
choice=input("Make your choice(rock(r),paper(p),scissor(s))\n")
print("you chose",choice)
print("opponent chose",rand_choice)
def game(rand_choice,choice):
    if rand_choice==choice:
        print("its a tie!")
    elif rand_choice=="r":
        if choice=="s":
            print("Opponent wins")
        else:
            print("You Win")
    elif rand_choice=="p":
        if choice=="r":
            print("Opponent Win")
        else:
            print("You Win")
    else:
        if choice=="p":
            print("Opponent Win")
        else:
            print("You Win")

print(game(rand_choice,choice))