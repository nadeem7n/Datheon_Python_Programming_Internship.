import random
from pathlib import Path

MAX_WRONG = 6
FALLBACK_WORDS = ["python", "hangman", "developer", "computer", "programming", "keyboard", "function", "database", "internet", "variable", "software", "terminal", "algorithm", "project", "practice"]
STAGES = [
" +---+\n |   |\n     |\n     |\n     |\n     |\n=========",
" +---+\n |   |\n O   |\n     |\n     |\n     |\n=========",
" +---+\n |   |\n O   |\n |   |\n     |\n     |\n=========",
" +---+\n |   |\n O   |\n/|   |\n     |\n     |\n=========",
" +---+\n |   |\n O   |\n/|\\  |\n     |\n     |\n=========",
" +---+\n |   |\n O   |\n/|\\  |\n/    |\n     |\n=========",
" +---+\n |   |\n O   |\n/|\\  |\n/ \\  |\n     |\n=========",
]

def load_words():
    """Load eligible words from words.txt; use built-in words if unavailable."""
    path = Path(__file__).with_name("words.txt")
    try:
        with path.open("r", encoding="utf-8") as file:
            words = [line.strip().lower() for line in file
                     if line.strip().isascii() and line.strip().isalpha()
                     and 4 <= len(line.strip()) <= 12]
        if words:
            print(f"Loaded {len(words):,} words.")
            return words
    except OSError:
        pass
    print("Using built-in words (words.txt unavailable or empty).")
    return FALLBACK_WORDS.copy()

def show_word(word, guessed):
    return " ".join(letter.upper() if letter in guessed else "_" for letter in word)

def get_guess(guessed):
    while True:
        guess = input("Guess one letter (A-Z): ").strip().lower()
        if len(guess) != 1 or not guess.isascii() or not guess.isalpha():
            print("Invalid input. Enter one English letter.")
        elif guess in guessed:
            print("You already guessed that letter. No penalty; try another.")
        else:
            return guess

def play(words):
    word = random.choice(words)
    guessed, wrong = set(), set()
    print("\n=== HANGMAN ===")
    print(f"Guess the hidden word. You have {MAX_WRONG} incorrect guesses.")
    while True:
        print(STAGES[len(wrong)])
        print("\nWord: ", show_word(word, guessed))
        print("Incorrect letters:", ", ".join(sorted(x.upper() for x in wrong) or "None"), f"({len(wrong)}/{MAX_WRONG})")
        if all(letter in guessed for letter in word):
            print("\nYOU WIN! The word was:", word.upper())
            return
        if len(wrong) >= MAX_WRONG:
            print("\nGAME OVER! The word was:", word.upper())
            return
        guess = get_guess(guessed)
        guessed.add(guess)
        if guess in word:
            print("Correct!")
        else:
            wrong.add(guess)
            print("Sorry, that letter is not in the word.")

def main():
    words = load_words()
    while True:
        play(words)
        if input("\nPlay again? (y/n): ").strip().lower() not in {"y", "yes"}:
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
