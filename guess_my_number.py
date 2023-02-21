print('Computer Number Guesser')

upperbound = int(input('What is the upper range? '))
lowerbound = int(input('What is the lower range? '))
print(f'Think of a number between {lowerbound}-{upperbound}')
guess = round((upperbound+lowerbound)/2)
guessing = True

while guessing:
    guessed = input(f'Is your number higher(h), lower (h) or at (a) {guess}? ')
    if guessed=='h':
        lowerbound = guess
        guess = round((upperbound+lowerbound)/2)
    elif guessed=='l':
        upperbound = guess
        guess = round((upperbound+lowerbound)/2)
    else:
        print(f'Your number is {guess}!')
        guessing = False
    if(upperbound<=lowerbound+1):
        print('Cheater.')
        guessing = False
