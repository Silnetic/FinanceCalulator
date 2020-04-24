import tkinter
from tkinter import ttk


def main():
    win = tkinter.Tk()
    App(win)
    win.mainloop()


class App:
    def __init__(self, master):
        # Configeration
        self.master = master
        self.style = ttk.Style()
        self.style.configure("BW.TLabel", foreground="black")
        self.master.title("Login")

        # Text Variables
        self.username = tkinter.StringVar()
        self.password = tkinter.StringVar()

        # Username
        self.user_label = ttk.Label(text="Username", style="BW.TLabel",
                                    font=("Open Sans", 20))
        self.user_label.grid(row=0, column=0, padx=8, pady=20)

        self.user_entry = ttk.Entry(textvariable=self.username,
                                    font=("Open Sans", 20))
        self.user_entry.grid(row=0, column=1, padx=8, pady=20)

        # Password
        self.password_label = ttk.Label(text="Password", style="BW.TLabel",
                                        font=("Open Sans", 20))
        self.password_label.grid(row=1, column=0, padx=8, pady=20)

        self.user_entry = ttk.Entry(textvariable=self.password,
                                    font=("Open Sans", 20), show="*")
        self.user_entry.grid(row=1, column=1, padx=8, pady=20)
    







if __name__ == "__main__":
    main()
