import random

print('Number Guessing Game')

number = random.randint(1,10)
score = 0
guess = 0
while(guess!=number):
    guess = int(input('Pick a Number between 1-10: '))
    if guess>number:
        print(f'Your guess of {guess} is too big!')
    elif guess<number:
        print(f'Your guess of {guess} is too small!')
print('You got the right answer!')