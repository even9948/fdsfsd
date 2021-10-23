import random
print("Number Gussing Game")
number=random.randint(1,9)
chances=0



print("Guess a num between 1 and 9")

while chances < 5:
    guess=int(input("Enter your guess: "))

    if guess == number :
        print("HURRAY YOU WON!!")
        break
    
    elif guess < number:
        print("Your guess is too small")

    else :
        print("Your guess is too big")
    chances +=1
    if not chances < 5:
        print("YOU LOST!!! The number is",number)
   