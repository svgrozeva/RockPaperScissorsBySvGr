import random

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'

player_move = input('Choose [R]ock, [P]aper or [S]cissors: ')

if player_move == 'R':
    player_move = rock
elif player_move == 'P':
    player_move = paper
elif player_move == 'S':
    player_move = scissors
else:
    raise SystemExit('Invalid Input. Try again...')

computer_random_number = random.randint(1, 3)
computer_move = ''

if computer_random_number == 1:
    computer_move = rock
elif computer_random_number == 2:
    computer_move = paper
elif computer_random_number == 3:
    computer_move = scissors

print(f'The computer chose {computer_move}.')

if (player_move == rock and computer_move == scissors) or \
        (player_move == paper and computer_move == rock) or \
        (player_move == scissors and computer_move == paper):
    print('Congrats, you win!')
elif (player_move == rock and computer_move == paper) or \
        (player_move == paper and computer_move == scissors) or \
        (player_move == scissors and computer_move == rock):
    print('Sorry, you lose!')
else:
    print("Looks like it's a draw!")


