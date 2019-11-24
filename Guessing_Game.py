from random import randint
# randint(1,100)
num = randint(1,100)
print('Welcome to my Guessing Game!')
print('In this game you will have to guess any number form 1 to 100.')
print('If your guess is same as what I am thinking, You win !')
print("If your guess is closer than 10 digits, I will say 'excellent'")
print("if your guess is farther than 10 digits, I'll say 'good'")
print("If your guess is farther than your most recent guess, I'll say you're getting away")
print("If your guess is closer than your most recent guess, I'll say you're getting closer")
print("LET'S PLAY!")

x = [0]

while True:
    guess = int(input("I'm thinking of a number between 1 and 100.\n  What is your guess? "))

    if guess==num:
        print(f"Congratulation ! You've guessed it right in just {len(x)} guesses!")    

    x.append(guess)
    
   
    if x[-2]:
        if abs(num-guess) < abs(num-(x[-2])):
            print('You are getting closer')
        else:
            print('You are getting away')
   

    else:
        if abs(num-guess)<=10:
            print("Excellent!")
        else:
            print("Good")
    
  
    


print('Game Over')
