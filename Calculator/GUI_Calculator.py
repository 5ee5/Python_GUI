import tkinter as tk

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(entry_var.get()))
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    elif text == "C":
        entry_var.set("")
    else:
        entry_var.set(entry_var.get() + text)

# Main GUI Window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvar=entry_var, font="Arial 20 bold", justify="right")
entry.pack(fill="both", ipadx=8, ipady=8, pady=10)

# Calculator Buttons
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for btn_text in row:
        btn = tk.Button(frame, text=btn_text, font="Arial 15 bold", width=5, height=2)
        btn.pack(side="left", expand=True, fill="both")
        btn.bind("<Button-1>", on_click)

root.mainloop()

