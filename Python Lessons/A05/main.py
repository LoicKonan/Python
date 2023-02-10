# This program randomly generates a number between [1, 100],
# then prompts the user to guess a number in that range.

# If they guessed wrong, then they will be notified, and tries again
# until they guess right.

# Each time they get a guess wrong, a counter will increment, and
# will be shown to the guesser.

# The program uses common escape characters to make the terminal
# update and refresh its values to make the output cleaner


from random import randint
from typing import Tuple


def guess(actual_number: int, guess_number: int) -> Tuple[bool, bool]:
    is_correct = guess_number == actual_number
    hint = guess_number > actual_number
    return is_correct, hint


def input_guess() -> int:
    # Receives user input for guess
    # if the guess is not in range or not an int
    # then exit program
    try:
        guess = int(input("Enter your guess: "))
        assert guess in range(1, 101)
        return guess
    except ValueError:
        _extracted_from_input_guess_10("\nYour guess needs to be an integer...")
    except AssertionError:
        _extracted_from_input_guess_10(
            "\nYour guess needs to be in the range [1, 100]"
        )


# TODO Rename this here and in `input_guess`
def _extracted_from_input_guess_10(arg0):
    print("\033[2A", end="")
    print(arg0)
    exit(0)


def print_winning_message(tries: int):
    print("\033[2A", end="")
    print("🥳🥳 You got it right!! 🥳🥳")
    print(f"It took you {tries} tries to win.", " " * 3)


def print_retry_prompt(hint: bool):
    if hint:
        print("\033c", "Go lower...", sep="")
    else:
        print("\033c", "Go higher...", sep="")


def print_intro():
    print("\t\t 🕵️ Number Guessing Game 🕵️")
    print("\t\t\t By Jamil Bousquet\n")
    print("Enter a number between 1 and 100 (**inclusive**).")
    print("We'll keep track of how many wrong guesses you made with a counter.\n\n")
    print("If you guessed wrong, this counter will increment ", end="")
    print("until you get the answer is correct.\n\n")


def run_guessing_game():
    actual_number = randint(1, 100)
    guess_number = 0
    incorrect_guess_counter = 0

    print_intro()

    print(f"Incorrect guess counter: {incorrect_guess_counter}\n")
    while True:
        guess_number = input_guess()
        print("\033[3A", end="")
        # evaluates this guess, and gives the guesser a hint (go higher/lower)
        # if they are incorrect, otherwise it informs the
        # the guesser that they're correct
        is_correct, hint = guess(actual_number, guess_number)
        if not is_correct:
            incorrect_guess_counter += 1
            print_retry_prompt(hint)
            print(f"Incorrect guess counter: {incorrect_guess_counter}")
        else:
            print_winning_message(incorrect_guess_counter)
            break


run_guessing_game()
