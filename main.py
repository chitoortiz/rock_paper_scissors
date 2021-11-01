import random

moves = ['rock', 'paper', 'scissors']

rounds = int(input("How many rounds do you want to play? "))

while rounds > 0:
    enemy_move = random.choice(moves)
    player_move = 'cum'
    while player_move not in moves:
        print("Please use [rock], [paper] or [scissors]")
        player_move = input("rock, paper, scissors, shoot! ")

    if player_move == 'rock':
        if enemy_move == 'rock':
            print("Tie!")
        elif enemy_move == 'paper':
            print("You lose!")
        elif enemy_move == 'scissors':
            print("You win!")
    elif player_move == 'paper':
        if enemy_move == 'rock':
            print("You win!")
        elif enemy_move == 'paper':
            print("Tie!")
        elif enemy_move == 'scissors':
            print("You lose!")
    elif player_move == 'scissors':
        if enemy_move == 'rock':
            print("You lose!")
        elif enemy_move == 'paper':
            print("You win!")
        elif enemy_move == 'scissors':
            print("Tie!")
    else:
        print("WTF happened here?!")

    rounds -= 1
