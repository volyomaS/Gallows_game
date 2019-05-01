#                ©Daniil Samoylov               #
#                   @volyomaS                   #

from random import randint
from sys import platform
import os


def print_letter_not_in_alph():
    print('Word:', mask)
    print('Your lifes:', life)
    if len(done) != 0:
        print("Letters used :", end=' ')
        for j in range(len(done)):
            print(done[j], end=' ')
        print()
    print("Not a letter")
    print("Type a letter: ", end='')


def print_letter_in_done():
    print('Word:', mask)
    print('Your lifes:', life)
    if len(done) != 0:
        print("Letters used :", end=' ')
        for j in range(len(done)):
            print(done[j], end=' ')
        print()
    print('Already used')
    print("Type a letter: ", end='')


def lose():
    global loses
    print("You lose")
    print("Your word was", word)
    loses += 1
    print("Wins:", wins, "\nLoses:", loses)
    print(wins, "\n", loses, file=open("data/saves.txt", "w"), sep='')


def win():
    global wins
    print(mask)
    print("You win!!")
    wins += 1
    print("Wins:", wins, "\nLoses:", loses)
    print(wins, "\n", loses, file=open("data/saves.txt", "w"), sep='')


def print_type_letter():
    print('Word:', mask)
    print('Your lifes:', life)
    if len(done) != 0:
        print("Letters used :", end=' ')
        for j in range(len(done)):
            print(done[j], end=' ')
        print()
    print("Type a letter: ", end='')


def my_exit():
    print("Thanks for playing")
    print("Bye")
    print(wins, "\n", loses, file=open("data/saves.txt", "w"), sep='')


def greetings():
    print("Welcome to my game 'Gallows'")


def instructions():
    print("Your previous stats:\nWins:", wins, "\nLoses:", loses)
    print("To clear your history type 'clear'")


if platform == 'linux' or platform == 'linux2':
    clear = lambda: os.system('clear')
else:
    clear = lambda: os.system('cls')

alph = 'йцукенгшщзхъфывапролджэячсмитьбюё'

data = open("data/data.txt", 'r', encoding='utf-8').readlines()

wins, loses = map(int, open("data/saves.txt", "r").readlines())

greetings()

instructions()
while True:
    print("Type 'start', 'exit' or 'clear'")
    cmd = input()
    if cmd == "exit" or cmd == "e":
        clear()
        my_exit()
        break
    elif cmd == "start" or cmd == "s":
        num = randint(0, len(data) - 1)
        word = data[num].strip()
        mask = '*' * len(word)
        done = []
        life = 5
        while True:
            clear()
            print_type_letter()
            letter = input().strip()
            while len(letter) != 1 or letter not in alph or letter in done:
                clear()
                if len(letter) != 1 or letter not in alph:
                    print_letter_not_in_alph()
                    letter = input().strip()
                else:
                    print_letter_in_done()
                    letter = input().strip()
            done.append(letter)
            checker = 0
            for i in range(len(word)):
                if word[i] == letter:
                    checker = 1
                    mask = mask[:i] + letter + mask[i + 1:]
            if checker == 0:
                life -= 1
                if life == 0:
                    clear()
                    lose()
                    break
            if '*' not in mask:
                clear()
                win()
                break
    elif cmd == "clear" or cmd == "c":
        wins, loses = 0, 0
        clear()
        print("Wins:", wins, "\nLoses:", loses)
        print(wins, "\n", loses, file=open("data/saves.txt", "w"), sep='')
    else:
        clear()
        print("Not a command")

print("'Enter' button to close")
input()
