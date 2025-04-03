def print_welcome() -> None:
    print("Welcome to Hangman! "
          "\n-------------------------------"
          "\nWe will start by generating a random word and then decide who goes first.\n")
    

def end_game_calculate_stats(player_wins: int, computer_wins: int, ties: int) -> None:
    print("Thank you for playing Hangman! Your stats are below")
    print(f"Games Won: {player_wins}")
    print(f"Games Loss: {computer_wins}")
    print(f"Games Tied: {ties}")
    print(f"Total Games Palyed: {player_wins + computer_wins + ties}")