import random
def guess():
    print('Hello! What is your name?')
    name = input()
    print('Well,' , name,'I am thinking of a number between 1 and 20.')
    
    num = random.randrange(1,21)
    
    cnt=0

    while True:
        print("Take a guess")
        guessn=int(input())
        if num == guessn:
            print('Good job, KBTU! You guessed my number in' , cnt ,'guesses')
            break
        elif guessn < num:
            print('Your guess is too low.')
            cnt+=1
        else:
            print('Your guess is too high')
            cnt+=1

print(guess())