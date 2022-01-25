"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730359525"

word: str = input("Enter a 5-character word: ")

if len(word) == 5:
    pass
else:
    print("Error: Word must contain 5 characters")
    exit()

character: str = (input("Enter a single character: "))

if len(character) == 1:
    print("Searching for " + character + " in " + word)
else:
    print("Error: Character must be a single character.")
    exit()

character_match = int(0)

if character != word[0]:
    pass
else:
    print(character + " found at index 0")
    character_match = character_match + 1
if character != word[1]:
    pass
else:
    print(character + " found at index 1")
    character_match = character_match + 1
if character != word[2]:
    pass
else:
    print(character + " found at index 2")
    character_match = character_match + 1
if character != word[3]:
    pass
else:
    print(character + " found at index 3")
    character_match = character_match + 1
if character != word[4]:
    pass
else:
    print(character + " found at index 4")
    character_match = character_match + 1

if character_match > 1:
    print(str(character_match) + " instances of " + character + " found in " + word)
else:
    if character_match == 1:
        print("1 instance of " + character + " found in " + word)
    else:
        print("No instances of " + character + " found in " + word)