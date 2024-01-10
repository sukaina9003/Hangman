import tkinter as tk
from tkinter import messagebox
import random

class HangmanGame:
    def __init__(self, wordlist):
        self.wordlist = wordlist
        self.word_to_guess = ""
        self.guesses_left = 6
        self.guesses_made = []
        self.word_with_spaces = ""
        self.initialize_game()

    def initialize_game(self):
        self.word_to_guess = random.choice(self.wordlist).upper()
        self.word_with_spaces = " ".join("_" * len(self.word_to_guess))
        self.guesses_left = 6
        self.guesses_made = []

    def make_guess(self, letter):
        if letter in self.guesses_made:
            return  # Ignore duplicate guesses

        self.guesses_made.append(letter)

        if letter not in self.word_to_guess:
            self.guesses_left -= 1

        self.update_word_with_spaces()

        if "_" not in self.word_with_spaces:
            self.end_game("You win! The word was {}".format(self.word_to_guess))
        elif self.guesses_left == 0:
            self.end_game("Game over! The word was {}".format(self.word_to_guess))

    def update_word_with_spaces(self):
        new_word = ""
        for char in self.word_to_guess:
            if char in self.guesses_made:
                new_word += char
            else:
                new_word += "_"
        self.word_with_spaces = " ".join(new_word)

    def end_game(self, message):
        messagebox.showinfo("Game Over", message)
        self.initialize_game()

class HangmanGUI:
    def __init__(self, root, hangman_game):
        self.root = root
        self.hangman_game = hangman_game

        self.setup_ui()

    def setup_ui(self):
        self.root.title("Hangman Game")

        self.word_label = tk.Label(self.root, text=self.hangman_game.word_with_spaces, font=("Helvetica", 16))
        self.word_label.pack(pady=20)

        self.guess_entry = tk.Entry(self.root, font=("Helvetica", 14))
        self.guess_entry.pack(pady=10)

        self.guess_button = tk.Button(self.root, text="Make Guess", command=self.make_guess)
        self.guess_button.pack()

        self.restart_button = tk.Button(self.root, text="Restart Game", command=self.restart_game)
        self.restart_button.pack()

    def make_guess(self):
        guess = self.guess_entry.get().upper()
        if guess.isalpha() and len(guess) == 1:
            self.hangman_game.make_guess(guess)
            self.update_ui()
        else:
            messagebox.showwarning("Invalid Guess", "Please enter a valid single letter guess.")

    def update_ui(self):
        self.word_label.config(text=self.hangman_game.word_with_spaces)
        if self.hangman_game.guesses_left == 0 or "_" not in self.hangman_game.word_with_spaces:
            self.guess_button.config(state=tk.DISABLED)
        else:
            self.guess_button.config(state=tk.NORMAL)

    def restart_game(self):
        self.hangman_game.initialize_game()
        self.update_ui()


if __name__ == "__main__":
    wordlist = ["PYTHON", "JAVA", "CPLUSPLUS", "JAVASCRIPT", "HTML", "CSS", "PYTHONIC"]
    root = tk.Tk()
    hangman_game = HangmanGame(wordlist)
    hangman_gui = HangmanGUI(root, hangman_game)
    root.mainloop()
