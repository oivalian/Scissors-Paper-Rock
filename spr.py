import random
import time as t
import os

def game(score, cpu_score):
    while True:
        print(f'\nYour score is: {score}\nThe computers score is: {cpu_score}\n')
        print('\n[P] Paper\n[S] Scissors\n[R] Rock\n')
        player_move = input('Make a selection > ')
        match player_move:
            case 'p' | 'P':
                cpu_move = random.randrange(1, 4)
                if cpu_move == 1:
                    print("Computer used paper. It's a tie game!")
                    t.sleep(1.3)
                    os.system('cls')
                elif cpu_move == 2:
                    print("Computer used scissors. You lose! ")
                    t.sleep(1.3)
                    os.system('cls')
                    cpu_score += 1
                elif cpu_move == 3:
                    print("Computer used rock. You win!")
                    t.sleep(1.3)
                    os.system('cls')
                    score += 1
            case 's' | 'S':
                cpu_move = random.randrange(1, 4)
                if cpu_move == 1:
                    print("Computer used paper. You win!")
                    t.sleep(1.3)
                    os.system('cls')
                    score += 1
                elif cpu_move == 2:
                    print("Computer used scissors. It's a tie game! ")
                    t.sleep(1.3)
                    os.system('cls')
                elif cpu_move == 3:
                    print("Computer used rock. You lose!")
                    t.sleep(1.3)
                    os.system('cls')
                    cpu_score += 1
            case 'r' | 'R':
                cpu_move = random.randrange(1, 4)
                if cpu_move == 1:
                    print("Computer used paper. You lose!")
                    t.sleep(1.3)
                    os.system('cls')
                    cpu_score += 1
                elif cpu_move == 2:
                    print("Computer used scissors. You win! ")
                    t.sleep(1.3)
                    os.system('cls')
                    score += 1
                elif cpu_move == 3:
                    print("Computer used rock. It's a tie game!")
                    t.sleep(1.3)
                    os.system('cls')
            case _:
                os.system('cls')


score = 0
cpu_score = 0
game(score, cpu_score)
