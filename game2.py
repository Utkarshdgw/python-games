import random
n = random.randint(1, 100) 
a = 0
guesses = 1
while(a != n):
    a = int(input("Guess the number bitch: ")) 
    if(a >n):
        print("Lower number u dumb a** shit")
        guesses +=1
    elif(a<n):
        print("choose a Higher number, looser mentality")
        guesses +=1

print(f"You have guessed the number {n} correctly in {guesses} attempts")