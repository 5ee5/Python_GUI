import random
import tkinter as tk
from tkinter import messagebox

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("400x450")

        self.target_number = random.randint(1, 100)
        self.attempts = 0
        self.lower_bound = 1
        self.upper_bound = 100
        self.guess_history = []

        self.label = tk.Label(root, text="Guess a number between 1 and 100:", font=("Arial", 12))
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, font=("Arial", 12))
        self.entry.pack()

        self.button = tk.Button(root, text="Submit Guess", command=self.check_guess, font=("Arial", 12))
        self.button.pack(pady=10)

        self.feedback_label = tk.Label(root, text="", font=("Arial", 12))
        self.feedback_label.pack()

        self.attempts_label = tk.Label(root, text="Attempts: 0", font=("Arial", 12))
        self.attempts_label.pack()

        self.history_label = tk.Label(root, text="Previous Guesses:", font=("Arial", 12))
        self.history_label.pack()

        self.history_box = tk.Listbox(root, font=("Arial", 12), height=1)
        self.history_box.pack(pady=5, fill=tk.BOTH, expand=True)

        self.restart_button = tk.Button(root, text="Restart", command=self.restart_game, font=("Arial", 12))
        self.restart_button.pack(pady=5)
        self.restart_button.config(state=tk.DISABLED)

        # Exit button
        self.exit_button = tk.Button(root, text="Exit", command=self.root.quit, font=("Arial", 12), fg="white", bg="red")
        self.exit_button.pack(pady=5)

        # Bind Enter key to submit guess
        self.root.bind("<Return>", self.check_guess_event)

    def check_guess_event(self, event):
        """Handles Enter key press."""
        self.check_guess()

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            if guess < self.lower_bound or guess > self.upper_bound:
                self.feedback_label.config(text=f"Please enter a number between {self.lower_bound} and {self.upper_bound}.")
                return
            
            self.attempts += 1
            self.guess_history.append(guess)
            self.history_box.insert(tk.END, f"Guess {self.attempts}: {guess}")

            if guess == self.target_number:
                self.feedback_label.config(text="Correct! You won!")
                if self.attempts <= 3:
                    messagebox.showinfo("Result", f"Wow! Super player, you won in {self.attempts} guesses!")
                elif self.attempts <= 10:
                    messagebox.showinfo("Result", f"Nice! You won in {self.attempts} guesses!")
                else:
                    messagebox.showinfo("Result", f"You won, but {self.attempts} guesses is a bit much!")

                self.entry.config(state=tk.DISABLED)
                self.button.config(state=tk.DISABLED)
                self.restart_button.config(state=tk.NORMAL)

            elif guess < self.target_number:
                self.feedback_label.config(text="Guess higher!")
                self.lower_bound = guess + 1
            else:
                self.feedback_label.config(text="Guess lower!")
                self.upper_bound = guess - 1

            self.attempts_label.config(text=f"Attempts: {self.attempts}")
            self.entry.delete(0, tk.END)

        except ValueError:
            self.feedback_label.config(text="Please enter a valid number!")

    def restart_game(self):
        self.target_number = random.randint(1, 100)
        self.attempts = 0
        self.lower_bound = 1
        self.upper_bound = 100
        self.guess_history.clear()

        self.feedback_label.config(text="")
        self.attempts_label.config(text="Attempts: 0")
        self.history_box.delete(0, tk.END)
        self.entry.config(state=tk.NORMAL)
        self.button.config(state=tk.NORMAL)
        self.restart_button.config(state=tk.DISABLED)
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()

