"""A more complete attempt at wordle."""


__author__ = "730359525"


def contains_char(searched_str: str, searched_char: str) -> bool:
    """Searching for character matches between the user's guess and the secret word."""
    assert len(searched_char) == 1
    i: int = 0
    while i < len(searched_str):
        if searched_str[i] == searched_char:
            return True
        else:
            i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Returning emojis to indicate the accuracy of the user's guess."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    i: int = 0
    game_output: str = ""
    while i < len(secret):
        if guess[i] == secret[i]:
            game_output += GREEN_BOX
            i += 1
        elif contains_char(secret, guess[i]):
            game_output += YELLOW_BOX
            i += 1
        else:
            game_output += WHITE_BOX
            i += 1
    return game_output


def input_guess(expected_length: int) -> str:
    """Recieving the user guess and checking its length."""
    guess: str = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    secret_word: str = "codes"
    won: bool = False
    while turn <= 6 and not won:
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(len(secret_word))
        print(emojified(guess, secret_word))
        if guess == secret_word:
            won = True
            print(f"You won in {turn}/6 turns!")
        else:
            turn += 1
    if not won:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()