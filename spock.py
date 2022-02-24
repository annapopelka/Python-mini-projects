from random import randrange

human = input(str("Do you choose rock, paper, scissors, lizard, or spock? "))

number = randrange(0,4)
if number == 0:
    print('The computer chose the rock')
    if human == 'rock':
        print('Draw!')
    elif human == 'scissors':
        print('You lost!')
    elif human == 'paper':
        print('You won!')
    elif human == 'lizard':
        print('You lost!')
    elif human == 'spock':
        print('You won!')    
    else:
        print('I do not understand what you wrote :(')
elif number == 1:
    print('The computer chose the scissors')
    if human == 'paper':
        print('You lost!')
    elif human == 'scissors':
        print('Draw!')
    elif human == 'rock':
        print('You won!')
    elif human == 'lizard':
        print('You lost!')
    elif human == 'spock':
        print('You won!')
    else:
        print('I do not understand what you wrote :(')
elif number == 2:
    print('The computer chose the paper')
    if human == 'rock':
        print('You lost!')
    elif human == 'scissors':
        print('You won!')
    elif human == 'paper':
        print('Draw')
    elif human == 'lizard':
        print('You won!')
    elif human == 'spock':
        print('You lost!')
    else:
        print('I do not understand what you wrote :(')
elif number == 3:
    print('The computer chose the lizard')
    if human == 'rock':
        print('You won!')
    elif human == 'scissors':
        print('You won!')
    elif human == 'paper':
        print('You lost!')
    elif human == 'lizard':
        print('Draw!')
    elif human == 'spock':
        print('You lost!')
    else:
        print('I do not understand what you wrote :(')
else:
    print('The computer chose the spock')
    if human == 'rock':
        print('You lost!')
    elif human == 'scissors':
        print('You lost!')
    elif human == 'paper':
        print('You won!')
    elif human == 'lizard':
        print('You won!')
    elif human == 'spock':
        print('Draw!')
    else:
        print('I do not understand what you wrote :(')


