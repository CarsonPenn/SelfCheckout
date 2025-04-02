'''
start live feed opiton
view past transactions
settings
quit

'''
import tkinter as tk
from display import *
from runModel import *


class Menu:
    def __init__(self):

        self.root = tk.Tk()
        self.root.configure(bg="lightblue")
        self.root.geometry("400x450")
        self.root.title("Food Scanner")

        self.title = tk.Label(self.root, text="Food Scanner", font=("Times New Roman", 35), bg="lightblue")
        self.title.pack(padx=20, pady=40)

        self.start_button = tk.Button(self.root, text="Start", font=("Times New Roman", 16), command=self.StartScanner, bg="gray", fg="white")
        self.start_button.pack(padx=5, pady=5)

        self.history_button = tk.Button(self.root, text="Transactions", font=("Times New Roman", 16), command=self.ShowTransactions, bg="gray", fg="white")
        self.history_button.pack(padx=5, pady=5)

        self.settings_button = tk.Button(self.root, text="Settings", font=("Times New Roman", 16), command=self.DisplaySettings, bg="gray", fg="white")
        self.settings_button.pack(padx=5, pady=5)

        self.quit_button = tk.Button(self.root, text="Quit", font=("Times New Roman", 16), command=self.QuitProgram, bg="gray", fg="white")
        self.quit_button.pack(padx=5, pady=5)



        self.root.mainloop()

    def StartScanner(self):
        runModel(source=0)

    def ShowTransactions(self):
        display_transactions()

    def DisplaySettings(self):
        print("Look at all these cool settings!")

    def QuitProgram(self):
        self.root.destroy()

Menu()