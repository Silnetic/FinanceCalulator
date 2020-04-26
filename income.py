import tkinter as tk
from tkinter import StringVar, DoubleVar, messagebox
from tkinter import ttk


def main():
    win = tk.Tk()
    App(win)
    win.mainloop()


class App:
    def __init__(self, master):
        # Configeration
        self.master = master
        self.master.title("Income")

        # Keyboard Shortcuts
        self.master.bind('<Return>', self.onEnterPress)
        self.master.bind('<F5>', self.finishFunction)

        # Variables
        self.income = [[], []]

        # Styling
        lbl_style = ttk.Style()
        lbl_style.configure("BW.TLabel", font=("Arial", 20))

        btn_style = ttk.Style()
        btn_style.configure("BW.TButton", font=("Arial", 20), width=12)

        # Entry Variables
        self.income_name = StringVar()
        self.income_amount = DoubleVar()

        # Income Name Label
        self.income_name_lbl = ttk.Label(text="Income Name:",
                                         style="BW.TLabel")
        self.income_name_lbl.grid(row=0, column=0, padx=8, pady=20)

        # Income Name Entry
        self.income_name_entry = ttk.Entry(textvariable=self.income_name,
                                           font=("Arial", 20), width=20)
        self.income_name_entry.grid(row=0, column=1, padx=8, pady=20)

        # Income Amount Label
        self.income_amount_lbl = ttk.Label(text="Income Amount:",
                                           style="BW.TLabel")
        self.income_amount_lbl.grid(row=1, column=0, padx=8, pady=20)

        # Income Amount Entry
        self.income_amount_entry = ttk.Entry(textvariable=self.income_amount,
                                             font=("Arial", 20), width=20)
        self.income_amount_entry.delete(0, 'end')
        self.income_amount_entry.grid(row=1, column=1, padx=8, pady=20)

        # Finish Button
        self.finish_btn = ttk.Button(text="Finished", style="BW.TButton",
                                     command=self.finishFunction)
        self.finish_btn.grid(row=2, column=0, padx=(50, 8), pady=20)

        # Help Button
        self.help_btn = ttk.Button(text="Help", style="BW.TButton",
                                   command=self.helpFunciton)
        self.help_btn.grid(row=2, column=1, padx=8, pady=20)

    def onEnterPress(self, event):
        try:
            income_name = self.income_name.get()
            income_amount = self.income_amount.get()

            self.income[0].append(income_name)
            self.income[1].append(income_amount)

            self.income_name_entry.delete(0, 'end')
            self.income_amount_entry.delete(0, 'end')
            self.income_name_entry.focus()

        except tk.TclError as error_message:
            messagebox.showerror("Error", error_message)

    def finishFunction(self, event):
        # Add in the method to get to the next window using another file.
        for i in self.income:
            print(i)

    def helpFunciton(self):
        message = """Enter the income source name and the income source amount
                  \nPress enter key to save the values and input another value
                  \nClick on the finish button to finish the income inputs"""
        messagebox.showinfo("Help", message)


if __name__ == "__main__":
    main()
