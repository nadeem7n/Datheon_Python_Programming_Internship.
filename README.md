# Datheon Python Internship — Task 1: Hangman

A command-line Hangman game built with Python's standard library.

## Features
- Random word selection from `words.txt`
- Masked word display and ASCII gallows stages
- Six-incorrect-guess limit
- Tracks guesses and does not penalize repeated letters
- Input validation for English letters A–Z
- Win/loss messages and replay option
- Built-in fallback words if `words.txt` is unavailable

## Run
Requires Python 3.8+; no third-party packages are needed.

```bash
python hangman.py
```
On Windows, `py hangman.py` may also work. Keep `hangman.py` and `words.txt` in the same folder. Blank lines, Markdown fence lines, and words outside 4–12 alphabetic characters are ignored.
