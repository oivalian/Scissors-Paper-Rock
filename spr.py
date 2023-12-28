import random as r
import time as t
import os


def game(score, cpu_score):
    while True:
        print(f"\nYour score is: {score}\nThe computers score is: {cpu_score}")
        print("\nPaper\nScissors\nRock\n")
        player_move = input("Make a selection > ")
        player_move = player_move.lower()
        cpu_move = r.choice(choices)
        if cpu_move == player_move:
            print(f"It's a tie! You both entered in {player_move}!")
        elif (cpu_move == "rock" and player_move == "paper") or \
                (cpu_move == "scissors" and player_move == "rock") or \
                (cpu_move == "paper" and player_move == "scissors"):
            score += 1
            print(f"You win! {player_move} beats {cpu_move}!")
        else:
            cpu_score += 1
            print(f"You lose! Computer beat you with {cpu_move}!")
        t.sleep(1.3)
        os.system('cls')

choices = ["rock", "paper", "scissors"]
score = 0
cpu_score = 0
game(score, cpu_score)
