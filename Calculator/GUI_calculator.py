from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout, QHBoxLayout, QListWidget
)
from PyQt6.QtGui import QFont, QKeyEvent
from PyQt6.QtCore import Qt
import sys
import math

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Advanced PyQt6 Calculator")
        self.setGeometry(100, 100, 500, 500)
        self.history = []  # Store calculation history
        self.initUI()

    def initUI(self):
        # Main Layout
        main_layout = QHBoxLayout()
        calc_layout = QVBoxLayout()

        # Entry box
        self.entry = QLineEdit(self)
        self.entry.setFont(QFont("Arial", 24))
        self.entry.setStyleSheet("background: #222; color: white; border: 2px solid #555; border-radius: 10px; padding: 10px;")
        calc_layout.addWidget(self.entry)

        # Grid layout for buttons
        grid_layout = QGridLayout()
        buttons = {
            '7': (0, 0), '8': (0, 1), '9': (0, 2), '/': (0, 3),
            '4': (1, 0), '5': (1, 1), '6': (1, 2), '*': (1, 3),
            '1': (2, 0), '2': (2, 1), '3': (2, 2), '-': (2, 3),
            'C': (3, 0), '0': (3, 1), '=': (3, 2), '+': (3, 3),
            '⌫': (4, 0), '(': (4, 1), ')': (4, 2), '√': (4, 3)
        }

        for text, (x, y) in buttons.items():
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
        self.history_box = QListWidget(self)
        self.history_box.setFont(QFont("Arial", 14))
        self.history_box.setStyleSheet("background: #111; color: #aaa; border: 2px solid #333; border-radius: 10px; padding: 10px;")
        main_layout.addLayout(calc_layout, 3)
        main_layout.addWidget(self.history_box, 2)

        self.setLayout(main_layout)

    def on_click(self):
        sender = self.sender().text()
        if sender == "=":
            result = self.evaluate_expression()
            self.entry.setText(result)
            if result != "Error":
                self.history.append(f"{self.entry.text()} = {result}")
                self.update_history()
        elif sender == "C":
            self.entry.setText("")
        elif sender == "⌫":
            self.entry.setText(self.entry.text()[:-1])
        elif sender == "√":
            try:
                expression = self.entry.text()
                result = str(math.sqrt(float(expression)))
                self.entry.setText(result)
                self.history.append(f"√({expression}) = {result}")
                self.update_history()
            except:
                self.entry.setText("Error")
        else:
            self.entry.setText(self.entry.text() + sender)

    def evaluate_expression(self):
        try:
            expression = self.entry.text()
            result = str(eval(expression, {"__builtins__": None}, math.__dict__))
            return result
        except:
            return "Error"

    def update_history(self):
        self.history_box.clear()
        for item in self.history[-5:]:
            self.history_box.addItem(item)

    def keyPressEvent(self, event: QKeyEvent):
        key = event.key()
        if key in (Qt.Key_Enter, Qt.Key_Return):
            self.on_click()
        elif key == Qt.Key_Backspace:
            self.entry.setText(self.entry.text()[:-1])
        elif key == Qt.Key_Escape:
            self.entry.setText("")
        elif event.text() in "0123456789+-*/().":
            self.entry.setText(self.entry.text() + event.text())
        elif event.text() == "\r":  # Handle enter key
            self.on_click()
        elif event.text() == "√":
            self.on_click()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Calculator()
    win.show()
    sys.exit(app.exec())

