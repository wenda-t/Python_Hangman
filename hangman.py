import randomization
import messages
import random

# Where the magic happens

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


def word_gussed(word: str, secret: str) -> bool:
    """Returns T/F depending if our word is the same as secret."""
    return word == secret


def player_turn(unchosen: list, chosen: list, word: str, secret:str) -> tuple[bool, str]:
    """Handing players turn"""
    player_input = input("Guess a letter: ")
    already_guessed = False

    # Checking if the player input is already guessed
    for i in chosen:
        if player_input == i:
            already_guessed = True
            break

    # Loop until we get a single letter guess that hasn't already been guessed.
    while len(player_input) != 1 or (already_guessed == True):
        player_input = input("Invalid input. Guess another letter: ")
        for i in unchosen:
            if player_input == i:
                already_guessed = False
    
    # update lists, and check if letter is in word once we get a valid word input.
    chosen.append(player_input)
    unchosen.remove(player_input)
    in_word = letter_in_word(word, player_input)

    return in_word, player_input


def computer_turn(unchosen: list, chosen: list, word: str) -> tuple[bool, str]:
    """Handling computers turn. We'll just randomize a letter from the unchosen words list."""
    print("Computer Guessing...")
    letter_guess = unchosen[random.randint(0,len(unchosen) - 1)]

    chosen.append(letter_guess)
    unchosen.remove(letter_guess)
    in_word = letter_in_word(word, letter_guess)

    return in_word, letter_guess


def main():
    """The main function. Runs the game using other functions until user decides to stop playing."""

    playing_game = True
    
    # Outer: Will keep going as long as player wants to play, Inner: For 1 game of hangman 
    while playing_game:
        unchosen_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        chosen_letters = []
        player_lives, computer_lives = 8, 8
        player_wins, computer_wins, game_ties = 0, 0, 0
        game_word = randomization.generate_random_word()
        game_word_secret = hide_word(game_word)
        starter = starting_user()
        current_player = starter

        print("Starting player:", starter)
        print(f"Your word is:\n{game_word_secret}")

        while True:
            winner = str # for score count after game ends
            if current_player == "player":
                correct_guess, letter_guessed = player_turn(unchosen_letters, chosen_letters, game_word, game_word_secret)

                if correct_guess:
                    print("Correct letter guessed! Good Job")

                    # Check if the word has been guessed.
                    game_word_secret = update_secret(game_word, game_word_secret, letter_guessed)
                    full_word = word_gussed(game_word, game_word_secret)
                    
                    if full_word:
                        print(f"Congratulations, you got the word {game_word_secret}")
                        winner = "player"
                        break
                    else:
                        print("Here is the remaining list of letters to guess:")
                        print_remaining_letters(unchosen_letters)
                        print("\nHere is the word with current guesses so far:")
                        print(game_word_secret)
                    
                else:
                    player_lives -= 1
                    print(f"Sorry!, {letter_guessed} was not a letter in the word.")
                    print(f"You have {player_lives} guesses remaining. \nSwitching sides\n")
            
                    if computer_lives > 0:
                        current_player = "computer"
                    elif computer_lives == 0 and player_lives > 0:
                        print("Computer is out of lives, continue guessing.")
                        continue
                    else: 
                        print("Player and Computer out of lives, game over.")
                        winner = "tie"
                        break
                    

            elif current_player == "computer":
                correct_guess, letter_guessed = computer_turn(unchosen_letters, chosen_letters, game_word)

                if correct_guess:
                    print(f"Computer guessed {letter_guessed} and it was in the word.")

                    game_word_secret = update_secret(game_word, game_word_secret, letter_guessed)
                    full_word = word_gussed(game_word, game_word_secret)

                    if full_word:
                        print(f"Computer has gussed the word{game_word}")
                        winner = "computer"
                        break
                    else:
                        print("\nHere is the word with current guesses so far:")
                        print(game_word_secret)
                        print("Computer guessing again..")
                else: 
                    computer_lives -= 1
                    print(f"Computer has guessed {letter_guessed} and it was NOT in the word.")
                    print(f"Computer has {computer_lives} gusses remaining.\nSwitching sides\n")

                    if player_lives > 0:
                        current_player = "player"
                    elif player_lives == 0 and computer_lives > 0:
                        print("Player is out of lives, continue guessing.")
                        continue
                    else: 
                        print("Player and Computer out of lives, game over.")
                        winner = "tie"
                        break

        # Now that the game is over, we need to update stats
        if winner == "player":
            player_wins += 1
        elif winner == "computer":
            computer_wins += 1
        else: 
            game_ties += 1
        
        # Now ask if player wants to play again.
        play_again = input("Do you want to play another game? Yes/No:\n").lower()

        while (play_again != "yes") and (play_again != "no"):
            play_again = input("Invalid answer, do you wish to play again? Answer yes or no\n").lower
        
        if play_again == "no":
            messages.end_game_calculate_stats(player_wins, computer_wins, game_ties)
            playing_game = False
