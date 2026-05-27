import tkinter as tk
from tkinter import messagebox
import math

# Scientific Calculator

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("450x650")
        self.root.configure(bg="#1e1e1e")

        self.expression = ""

        # Display
        self.display = tk.Entry(
            root,
            font=("Consolas", 28),
            bd=10,
            relief=tk.FLAT,
            justify="right",
            bg="#2b2b2b",
            fg="white",
            insertbackground="white"
        )
        self.display.pack(fill="x", padx=15, pady=15, ipady=20)

        # Button Frame
        button_frame = tk.Frame(root, bg="#1e1e1e")
        button_frame.pack()

        buttons = [
            ['C', 'DEL', '(', ')', '/'],
            ['7', '8', '9', '*', 'sqrt'],
            ['4', '5', '6', '-', '^'],
            ['1', '2', '3', '+', 'log'],
            ['0', '.', 'pi', 'e', '='],
            ['sin', 'cos', 'tan']
        ]

        for r, row in enumerate(buttons):
            for c, text in enumerate(row):

                btn = tk.Button(
                    button_frame,
                    text=text,
                    width=8,
                    height=3,
                    font=("Segoe UI", 12, "bold"),
                    bg="#3a3a3a",
                    fg="white",
                    activebackground="#5a5a5a",
                    activeforeground="white",
                    relief=tk.FLAT,
                    command=lambda t=text: self.click(t)
                )

                btn.grid(row=r, column=c, padx=5, pady=5)

    # Button Logic
    def click(self, value):

        if value == "C":
            # Clear everything
            self.expression = ""
            self.update_display()

        elif value == "DEL":
            # Remove one character
            self.expression = self.expression[:-1]
            self.update_display()

        elif value == "=":
            # Calculate result
            self.calculate()

        else:
            replacements = {
                "sin": "math.sin(",
                "cos": "math.cos(",
                "tan": "math.tan(",
                "sqrt": "math.sqrt(",
                "log": "math.log10(",
                "^": "**",
                "pi": "math.pi",
                "e": "math.e"
            }

            self.expression += replacements.get(value, value)
            self.update_display()

    # Update Display
    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)

    # Calculate
    def calculate(self):
        try:
            result = eval(self.expression)

            self.expression = str(result)
            self.update_display()

        except Exception as e:
            messagebox.showerror(
                "Error",
                f"Invalid Expression\n\n{e}"
            )

# Run App

root = tk.Tk()
app = ScientificCalculator(root)
root.mainloop()