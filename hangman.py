import randomization

# One game of hangman. 


def hide_word(word: str) -> str:
    """Takes the word and replaces letters with "-" for our game"""
    secret_word = ""
    for i in range(len(word)):
        secret_word += "-"

    return secret_word


def starting_user() -> str:
    """Deciding who is going first"""
    result = randomization.starter_player()

    if result:
        return "player"
    else:
        return "computer"


def print_remaining_letters(unchosen: list) -> None: 
    """Prints the remaining letters for user to guess from after they get a correct guess."""
    for i in unchosen:
        print(f"{i}, ", end="")
    print()


def update_secret(word: str, secret: str, letter: str) -> str:
    """Once a user guesses a correct letter, update our secret to show that."""
    new_word = ""

    for i in range(len(word)):
        if word[i] == letter: 
            new_word += letter
        else:
            new_word += secret[i]
    
    return new_word


def letter_in_word(word: str, letter: str) -> bool:
    """Checking if the guessed letter is in word"""
    in_word = False

    # Check if it's in the letter, will change in_word to true if it is.
    for i in word:
        if i == letter:
            in_word = True

    return in_word


def player_turn(unchosen: list, chosen: list, word: str, secret:str) -> bool:
    """Handing players turn"""
    player_input = input("Guess a letter: ")
    already_guessed = bool

    # Checking if the player input is already guessed
    for i in unchosen:
        if player_input == i:
            already_guessed = True

    # Loop until we get a single letter guess that hasn't already been guessed.
    while len(player_input) != 1 and already_guessed:
        player_input = input("Invalid input. Guess another letter: ")
        for i in unchosen:
            if player_input == i:
                already_guessed = True

    chosen.append(player_input)
    unchosen.remove(player_input)

    in_word = letter_in_word(word, player_input)

    return in_word, player_input


def computer_turn() -> str:
    pass


def main():
    # Variables: default lives set to 8
    unchosen_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "j", "l", "m",
                        "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    chosen_letters = []
    user_lives = 8
    bot_loves = 8
    game_word = randomization.generate_random_word()
    game_word_secret = hide_word(game_word)
    starter = starting_user()

    #debug
    print(game_word)
    print(game_word_secret)

    print("Deciding who will be going first.")
    print("Starting player:", starter)

    if starter == "player":
        print("\nPlayer goes first.")
        result = player_turn(unchosen_letters, chosen_letters, game_word, game_word_secret)

        correct_guess = result[0]
        letter_guessed = result[1]

        if correct_guess:
            print("Correct letter guessed! Good Job")
            print("Here is the remaining list of letters to guess.")
            print_remaining_letters(unchosen_letters)
            print("Here is the word with current guesses.")
            game_word_secret = update_secret(game_word, game_word_secret, letter_guessed)
            print(game_word_secret)
        else:
            user_lives -= 1
            print(f"Sorry!, {letter_guessed} was not a letter in the word.")
            print(f"You have {user_lives} guesses remaining. \nSwitching sides")
            

    elif starter == "computer":
        print("\nComputer goes first")
