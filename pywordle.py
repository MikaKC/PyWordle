import datetime
import random
import os

# required for saving date & time (but can be bypassed)
import pickle

from datetime import date
from re import match

# dict of words
all_words = ['these', 'there', 'theme']
word_to_guess = all_words[random.randint(0, len(all_words) - 1)]

today_date = date.today()


def save_date():
    try:
        with open("game_data.pickle", "wb") as file:
            pickle.dump(today_date, file, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as e:
        print(f"{today_date} - Error during pickling current time! Exception: {e}")


def load_date():
    try:
        with open("game_data.pickle", "rb") as file:
            return pickle.load(file)
    except Exception as e:
        print(f"{today_date} - Error during de-pickling current time! Exception: {e}")


def answer_correct():
    save_date()
    print("The answer is correct! It is " + word_to_guess + "!")
    os.system("pause")
    exit(0)


def cant_play():
    print("You already guessed the word today! You can't play!");
    os.system("pause")
    exit(0)


def get_input():
    guess = input("Input 5 letters:\n")
    if not match(r'^[a-zA-Z]{5}$', guess):
        print("Guess isn't valid, try again!")
        get_input()

    # wtf
    defunct_indexes = []
    for i, (a, b) in enumerate(zip(guess, word_to_guess)):
        if a != b:
            defunct_indexes.append(i)

    possible_indexes = []
    for idx, (x, y) in enumerate(zip(guess, word_to_guess)):
        if x != y and x in word_to_guess:
            if idx in defunct_indexes:
                possible_indexes.append(idx)
                defunct_indexes.remove(idx)

    if not defunct_indexes and not possible_indexes:
        answer_correct()
    else:
        if len(defunct_indexes) > 0:
            print(f'{"Letter:" if len(defunct_indexes) < 2 else "Letters:"}')

            # odd work-around my ass won't fix
            count = 0
            for i in defunct_indexes:
                print(guess[defunct_indexes[count]])
                count += 1

            print(f'{"is incorrect!" if len(defunct_indexes) < 2 else "are incorrect!"}')

        if len(possible_indexes) > 0:
            print(f'{"Letter:" if len(possible_indexes) < 2 else "Letters:"}')

            # odd work-around my ass won't fix
            count = 0
            for i in possible_indexes:
                print(guess[possible_indexes[count]])
                count += 1

            print(f'{"is in the word!" if len(possible_indexes) < 2 else "are in the word!"}')

        get_input()


if __name__ == "__main__":
    if load_date() == today_date:
        cant_play()

    print("Guess the 5 letter word!")
    get_input()
