from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox, QLineEdit, QTextEdit
import sys
import random

class NumberGuessGame(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Number Guessing Game - PyQt6")
        self.setGeometry(100, 100, 400, 350)  # Window size
        self.setStyleSheet("background-color: #222; color: white;")  # Dark theme

        self.target_number = random.randint(1, 100)  # Generate a random number
        self.previous_guesses = []
        self.total_guesses = 0

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Label for instructions
        self.label = QLabel("Guess a number between 1 and 100", self)
        self.label.setStyleSheet("font-size: 18px; color: white; padding: 10px;")
        layout.addWidget(self.label)

        # Input field for number guessing
        self.input_box = QLineEdit(self)
        self.input_box.setPlaceholderText("Enter your guess")
        self.input_box.setStyleSheet("""
            QLineEdit {
                font-size: 16px; padding: 8px; border-radius: 8px; 
                background: #333; color: white; border: 2px solid #555;
            }
        """)
        self.input_box.returnPressed.connect(self.check_guess)  # Enter key to submit
        layout.addWidget(self.input_box)

        # Box to display previous guesses
        self.guess_history = QTextEdit(self)
        self.guess_history.setReadOnly(True)
        self.guess_history.setStyleSheet("""
            QTextEdit {
                font-size: 14px; padding: 8px; border-radius: 8px; 
                background: #111; color: white; border: 2px solid #555;
            }
        """)
        self.guess_history.setPlaceholderText("Previous guesses will appear here...")
        layout.addWidget(self.guess_history)

        # Guess button
        self.guess_btn = QPushButton("Guess", self)
        self.guess_btn.setStyleSheet("""
            QPushButton {
                font-size: 16px; background: #444; color: white; padding: 10px;
                border-radius: 10px; border: 2px solid #666;
            }
            QPushButton:hover {
                background: #555;
            }
            QPushButton:pressed {
                background: #777;
            }
        """)
        self.guess_btn.clicked.connect(self.check_guess)
        layout.addWidget(self.guess_btn)

        # Reset button
        self.reset_btn = QPushButton("Reset Game", self)
        self.reset_btn.setStyleSheet("""
            QPushButton {
                font-size: 14px; background: #007acc; color: white; padding: 8px;
                border-radius: 10px; border: 2px solid #005a9e;
            }
            QPushButton:hover {
                background: #008be6;
            }
            QPushButton:pressed {
                background: #005a9e;
            }
        """)
        self.reset_btn.clicked.connect(self.reset_game)
        layout.addWidget(self.reset_btn)

        # Exit button
        self.exit_btn = QPushButton("Exit", self)
        self.exit_btn.setStyleSheet("""
            QPushButton {
                font-size: 14px; background: #888; color: black; padding: 8px;
                border-radius: 10px; border: 2px solid #666;
            }
            QPushButton:hover {
                background: #999;
            }
            QPushButton:pressed {
                background: #555;
            }
        """)
        self.exit_btn.clicked.connect(self.close)
        layout.addWidget(self.exit_btn)

        self.setLayout(layout)

    def check_guess(self):
        guess_text = self.input_box.text()
        
        if not guess_text.isdigit():
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid number between 1 and 100.")
            return

        guess = int(guess_text)
        self.total_guesses += 1
        self.previous_guesses.append(str(guess))

        if guess < self.target_number:
            QMessageBox.information(self, "Hint", "Too low! Try again.")
        elif guess > self.target_number:
            QMessageBox.information(self, "Hint", "Too high! Try again.")
        else:
            QMessageBox.information(self, "Congratulations!", f"Correct! You guessed the number in {self.total_guesses} attempts.")
            self.reset_game()
            return

        self.update_guess_history()
        self.input_box.clear()  # Clear input after each guess

    def update_guess_history(self):
        self.guess_history.setPlainText(", ".join(self.previous_guesses))

    def reset_game(self):
        self.target_number = random.randint(1, 100)  # Generate a new number
        self.total_guesses = 0
        self.previous_guesses = []
        self.input_box.clear()
        self.label.setText("Guess a number between 1 and 100")
        self.guess_history.clear()

# Run the application
app = QApplication(sys.argv)
window = NumberGuessGame()
window.show()
sys.exit(app.exec())

