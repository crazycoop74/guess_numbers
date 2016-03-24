import random

print('----------------------------------')
print('        The Numbers Game')
print('----------------------------------')
print()


the_number = random.randint(0,100)

guess=-1
name= input('What is your Name? ')


print()
while guess != the_number:
    guess_text = input('Guess a number between 0 and 100: ')

    guess = int(guess_text)

    if guess < the_number:
        print('{} your guess of {} was too low'.format(name,guess))
    elif guess > the_number:
        print('{} your guess of {} was too high'.format(name,guess))

    else:
        print('winner')

print('done')