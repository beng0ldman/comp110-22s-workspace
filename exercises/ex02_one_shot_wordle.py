"""EX02 - One-Shot Wordle - Getting a bit closer to the real thing."""

__author__ = "730359525"

secret_word: str = "python"
guess: str = input(f"What is your {len(secret_word)}-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# checking guess length
while len(guess) != len(secret_word):
    guess: str = input(f"That was not {len(secret_word)} letters! Try again: ")

i: int = 0
game_output: str = ""
n: int = len(secret_word)
yet_found: bool = False
alt_indices: int = 0

# indexing and evaluating for accuracy of guess
while i < len(guess):
    if guess[i] == secret_word[i]:
        game_output += GREEN_BOX
        i += 1
    else:
        alt_indices = 0
        yet_found = False
        while not yet_found and alt_indices < n:
            if guess[i] == secret_word[alt_indices]:
                game_output += YELLOW_BOX
                yet_found = True
            alt_indices += 1

        if not yet_found:
            game_output += WHITE_BOX
        i += 1

print(game_output)
# appeasing the user's humanity.
if guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")