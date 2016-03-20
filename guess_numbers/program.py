import random

print('----------------------------------')
print('        The Numbers Game')
print('----------------------------------')
print()


the_number = random.randint(0,100)


guess_text = input('Guess a number between 0 and 100: ')

guess =int(guess_text)

if guess < the_number:
    print('to low')
elif guess > the_number:
    print('too high')
else:
    print('winner')

