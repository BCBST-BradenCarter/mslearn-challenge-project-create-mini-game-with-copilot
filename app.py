# write 'hello world' to the console
print('Welcome to rock, paper, scissors!')

# I'm creating a rock paper scissors game, where the user can play against the computer, and the computer will randomly select rock, paper, or scissors.
# create constants for each rock, paper, and scissors
ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'

# print out the rules
print('Here are the rules:')
print('Rock beats scissors.')
print('Scissors beats paper.')
print('Paper beats rock.')

# boolean to keep playing
play = True

while play:
    while True:
        # ask the player to pick rock, paper, or scissors
        player_choice = input('Please pick rock, paper, or scissors: ').lower()

        # validate the player's choice
        if player_choice in [ROCK, PAPER, SCISSORS]:
            break
        else:
            print('Invalid choice. Please pick rock, paper, or scissors.')

    # randomly select rock, paper, or scissors for the computer
    import random
    computer_choice = random.choice([ROCK, PAPER, SCISSORS])

    # determine the winner
    if player_choice == computer_choice:
        print('It\'s a tie!')
    elif player_choice == ROCK and computer_choice == SCISSORS:
        print('You win! Rock beats scissors.')
    elif player_choice == PAPER and computer_choice == ROCK:
        print('You win! Paper beats rock.')
    elif player_choice == SCISSORS and computer_choice == PAPER:
        print('You win! Scissors beats paper.')
    else:
        print('You lose! ' + computer_choice + ' beats ' + player_choice + '.')

    #ask the player if they want to play again
    play_again = input('Do you want to play again? (yes or no): ')

    if play_again == 'yes':
        print('Great! Let\'s play again.')
    else:
        play = False;
        print('Thanks for playing! Goodbye.')

