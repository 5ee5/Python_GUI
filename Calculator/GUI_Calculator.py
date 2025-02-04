from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout, QTextEdit, QHBoxLayout
)
from PyQt6.QtGui import QFont, QKeyEvent
import sys

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Advanced PyQt6 Calculator")
        self.setGeometry(100, 100, 500, 500)  # Set window size

        self.history = []  # Store calculation history
        self.initUI()

    def initUI(self):
        # Main Layout
        main_layout = QHBoxLayout()

        # Left side: Calculator UI
        calc_layout = QVBoxLayout()

        # Entry box
        self.entry = QLineEdit(self)
        self.entry.setFont(QFont("Arial", 24))
        self.entry.setStyleSheet("background: #222; color: white; border: 2px solid #555; border-radius: 10px; padding: 10px;")
        self.entry.setReadOnly(True)
        calc_layout.addWidget(self.entry)

        # Grid layout for buttons
        grid_layout = QGridLayout()
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('C', 3, 0), ('0', 3, 1), ('=', 3, 2), ('+', 3, 3)
        ]

        for text, x, y in buttons:
            button = QPushButton(text)
            button.setFont(QFont("Arial", 18))
            button.setStyleSheet(
                """
                QPushButton {
                    background: #444; color: white; border: 1px solid #666; border-radius: 10px; padding: 10px;
                }
                QPushButton:hover {
                    background: #666;
                }
                QPushButton:pressed {
                    background: #888;
                }
                """
            )
            button.clicked.connect(self.on_click)
            grid_layout.addWidget(button, x, y)

        calc_layout.addLayout(grid_layout)

        # Right side: History Panel
        self.history_box = QTextEdit(self)
        self.history_box.setFont(QFont("Arial", 14))
        self.history_box.setReadOnly(True)
        self.history_box.setStyleSheet("background: #111; color: #aaa; border: 2px solid #333; border-radius: 10px; padding: 10px;")

        main_layout.addLayout(calc_layout, 3)
        main_layout.addWidget(self.history_box, 2)

        self.setLayout(main_layout)

    def on_click(self):
        sender = self.sender().text()
        if sender == "=":
            try:
                expression = self.entry.text()
                result = str(eval(expression))
                self.entry.setText(result)

                # Add to history
                self.history.append(f"{expression} = {result}")
                self.update_history()

            except:
                self.entry.setText("Error")
        elif sender == "C":
            self.entry.setText("")
        else:
            self.entry.setText(self.entry.text() + sender)

    def update_history(self):
        """Update history box with previous calculations"""
        self.history_box.setPlainText("\n".join(self.history[-5:]))  # Show last 5 calculations

    def keyPressEvent(self, event: QKeyEvent):
        key = event.text()
        if key in "0123456789+-*/":
            self.entry.setText(self.entry.text() + key)
        elif key == "\r" or key == "=":
            self.on_click()
        elif key == "\x08":  # Backspace
            self.entry.setText(self.entry.text()[:-1])

# Run the application
app = QApplication(sys.argv)
win = Calculator()
win.show()
sys.exit(app.exec())

