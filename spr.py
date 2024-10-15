from os import system
from random import choice
from time import sleep

def game(player, cpu):
    while True:
        print(f"\nYour score is: {player}\nThe computers score is: {cpu}")
        print("\nPaper\nScissors\nRock\n")
        player_move = input("Make a selection > ")
        player_move = player_move.lower()
        cpu_move = choice(choices)
        if cpu_move == player_move:
            print(f"It's a tie! You both entered in {player_move}!")
        elif (cpu_move == "rock" and player_move == "paper") or \
                (cpu_move == "scissors" and player_move == "rock") or \
                (cpu_move == "paper" and player_move == "scissors"):
            player += 1
            print(f"You win! {player_move} beats {cpu_move}!")
        else:
            cpu += 1
            print(f"You lose! Computer beat you with {cpu_move}!")
        sleep(1.3)
        system('cls')

choices = ["rock", "paper", "scissors"]
score, cpu_score = 0, 0
game(score, cpu_score)
