from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox
import sys
import os

# File to store progress
SAVE_FILE = "progress"

# Function to check and create the file if it doesn't exist
def initialize_file():
    if not os.path.exists(SAVE_FILE):  # Check if the file exists
        with open(SAVE_FILE, "w") as file:
            file.write("0")  # Initialize with 0

# Function to load progress
def load_progress():
    with open(SAVE_FILE, "r") as file:
        try:
            return int(file.read().strip())  # Read and convert to int
        except ValueError:
            return 0  # Default if file is corrupted

# Function to save progress
def save_progress(count):
    with open(SAVE_FILE, "w") as file:
        file.write(str(count))

class ClickCounter(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Click Counter - PyQt6")
        self.setGeometry(100, 100, 350, 250)  # Window size
        self.setStyleSheet("background-color: #222; color: white;")  # Dark theme

        # Ask if user wants to resume previous progress
        initialize_file()
        resume = QMessageBox.question(self, "Resume Progress", "Do you want to resume your previous progress?",
                                      QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        self.count = load_progress() if resume == QMessageBox.StandardButton.Yes else 0

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Label to display count
        self.label = QLabel(f"The button was clicked: {self.count} times", self)
        self.label.setStyleSheet("font-size: 18px; color: white; padding: 10px;")
        layout.addWidget(self.label)

        # Click button
        self.click_btn = QPushButton("Click Me", self)
        self.click_btn.setStyleSheet("""
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
        self.click_btn.clicked.connect(self.clicked)
        layout.addWidget(self.click_btn)

        # Reset button
        self.reset_btn = QPushButton("Reset Progress", self)
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
        self.reset_btn.clicked.connect(self.reset_progress)
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
        self.exit_btn.clicked.connect(self.exit_app)
        layout.addWidget(self.exit_btn)

        self.setLayout(layout)

    def clicked(self):
        self.count += 1
        self.label.setText(f"The button was clicked: {self.count} times")
        save_progress(self.count)

    def reset_progress(self):
        self.count = 0
        save_progress(self.count)
        self.label.setText("The button was clicked: 0 times")

    def exit_app(self):
        save_progress(self.count)  # Save progress before exiting
        self.close()

# Run the application
app = QApplication(sys.argv)
window = ClickCounter()
window.show()
sys.exit(app.exec())

