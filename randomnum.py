import random
randno=random.randint(1,100)
#print(randno)
guesses=None 
hisc=0
while randno!=guesses:
    guesses=int(input("Guess that no :"))
    hisc+=1
    if guesses==randno:
        print("Congratulations!! You guessed it right\n")
    else:
        print("Oopps!! You guessed it wrong try again...")
        if randno<guesses:
            print("Guess a smaller number")
        else:
            print("Guess a larger number")
print(f"You reached here in {hisc} guesses")
with open("guess_hiscore.txt") as f:
    highscore=int(f.read())

if highscore>hisc:
    print("You have just broken a high score!")
    with open("guess_hiscore.txt","w") as f:
        f.write(str(hisc))
