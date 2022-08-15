import tkinter as tk

from game import Wordle
from helpers import generate_word, setup_word_length

DIFFICULTIES = {
    "easy": 3,
    "normal": 5,
    "hard": 7,
}

import tkinter as tk

root = tk.Tk()
frame = tk.Frame(root)

WINDOW_BG = "white"
font = "Verdana, 38"


def window(letter_count, guess_count) -> None:

    for row in range(guess_count):
        for col in range(letter_count):
            btn = tk.Button(
                frame,
                text=" ",
                width=1,
                bg=WINDOW_BG,
                activebackground=WINDOW_BG,
                font=font,
            )
            btn.grid(row=row, column=col, padx=3, pady=5)

    menu = tk.Menu(root)
    root.config(menu=menu)
    new_game = tk.Menu(menu)
    menu.add_command(label="New Game", command=window)


if __name__ == "__main__":
    word_len = setup_word_length()
    word = generate_word(word_len)
    window(letter_count=word_len, guess_count=5)
    root.mai
    # print(f"Todays word is: {word}")
    # game = Wordle(word=word, max_guesses=5)  # TODO: update 5 here

    # while not game.has_game_finished:
    #     current_guess = input("Enter your guess: ")
    #     score = game.check_guess(current_guess)
