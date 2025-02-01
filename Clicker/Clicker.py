from tkinter import *
from tkinter import messagebox
import os

# File to store progress
SAVE_FILE = "progress.txt"

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
def save_progress():
    with open(SAVE_FILE, "w") as file:
        file.write(str(count))

# Function to reset progress
def reset_progress():
    global count
    count = 0
    save_progress()
    lbl.configure(text="The button was clicked: 0 times")

# Function to handle exiting the application
def exit_app():
    save_progress()  # Ensure progress is saved before exit
    root.quit()  # Close the application

# Ensure the progress file exists before loading
initialize_file()

# Ask the user if they want to resume progress
resume = messagebox.askyesno("Resume Progress", "Do you want to resume your previous progress?")
count = load_progress() if resume else 0

# Create main window
root = Tk()
root.title("Click Counter")
root.geometry('350x250')

# Label to display count
lbl = Label(root, text=f"The button was clicked: {count} times", font=("Arial", 12))
lbl.grid(column=0, row=0, columnspan=2, pady=20)

# Function to handle button click
def clicked():
    global count
    count += 1
    lbl.configure(text=f"The button was clicked: {count} times")
    save_progress()  # Save progress after each click

# Button to click
btn = Button(root, text="Click Me", fg="red", command=clicked, font=("Arial", 12))
btn.grid(column=0, row=1, columnspan=2, pady=10)

# Button to reset progress
reset_btn = Button(root, text="Reset Progress", fg="blue", command=reset_progress, font=("Arial", 10))
reset_btn.grid(column=0, row=2, columnspan=2, pady=10)

# **Exit Button**
exit_btn = Button(root, text="Exit", fg="black", bg="lightgray", command=exit_app, font=("Arial", 10))
exit_btn.grid(column=0, row=3, columnspan=2, pady=10)

# Center align widgets
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Start the application
root.mainloop()

