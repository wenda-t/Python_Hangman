import random


def generate_random_word() -> str:
    """Generates a random word from words.txt using a random number."""

    with open("words.txt", "r") as file:
        list_of_words = file.readlines()
        words = list_of_words[0].split()

    return random.choice(words)


def starter_player() -> bool:
    """Generates a random number 0 or 1 to decide who goes first.
        0: player goes first, returns true
        1: bot goes first, returns false. """

    num = random.randint(0, 1)
    if num == 0:
        return True
    else:
        return False