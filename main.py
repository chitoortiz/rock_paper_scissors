import random

# Possible moves in rock, paper, scissors
moves = ['rock', 'paper', 'scissors']

# Asks player how many rounds to play
rounds = int(input("How many rounds do you want to play? "))

# Game loop
while rounds > 0:
    # Randomly chooses enemy move
    enemy_move = random.choice(moves)

    # Asks player's move until correct format
    player_move = 'cum'
    while player_move not in moves:
        print("Please use [rock], [paper] or [scissors]")
        player_move = input("rock, paper, scissors, shoot! ")

    # Player chooses rock
    if player_move == 'rock':
        if enemy_move == 'rock':
            print("Tie!")
        elif enemy_move == 'paper':
            print("You lose!")
        elif enemy_move == 'scissors':
            print("You win!")

    # Player chooses paper
    elif player_move == 'paper':
        if enemy_move == 'rock':
            print("You win!")
        elif enemy_move == 'paper':
            print("Tie!")
        elif enemy_move == 'scissors':
            print("You lose!")

    # Player chooses scissors
    elif player_move == 'scissors':
        if enemy_move == 'rock':
            print("You lose!")
        elif enemy_move == 'paper':
            print("You win!")
        elif enemy_move == 'scissors':
            print("Tie!")
    
    # In case something strange happens (it shouldn't)
    else:
        print("WTF happened here?!")

    # Reduces remaining rounds by one
    rounds -= 1
