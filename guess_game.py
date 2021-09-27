#!/usr/bin/env python3

# Created by: Daria Bernice Calitis
# Created on: Sept 2021
# This program is the number guessing game

import random


def main():
    # This function is the number guessing game
    answer = random.randint(0, 9)
    guess_number = input("Enter a number as your guess (0-9): ")
    try:
        # input
        guess_number = int(guess_number)

        # process & output
        if guess_number == answer:
            print("You guessed correctly!")
        else:
            print("You guessed incorrectly.")
            print("The correct answer is {0}.".format(answer))
    except Exception:
        print("Invalid Input.")

    print("\nDone.")


if __name__ == "__main__":
    main()
