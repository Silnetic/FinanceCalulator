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

        # Label Style
        self.label_style = ttk.Style()
        self.label_style.configure("BW.TLabel", foreground="black",
                                   font=("Open Sans", 20))

        self.btn_style = ttk.Style()
        self.btn_style.configure("BW.TButton", font=("Open Sans", 20),
                                 width=20)

        self.master.title("Login")

        # Text Variables
        self.username = tkinter.StringVar()
        self.password = tkinter.StringVar()

        # Username
        self.user_label = ttk.Label(text="Username", style="BW.TLabel")
        self.user_label.grid(row=0, column=0, padx=8, pady=20)

        self.user_entry = ttk.Entry(textvariable=self.username,
                                    font=("Open Sans", 20))
        self.user_entry.grid(row=0, column=1, padx=8, pady=20)

        # Password
        self.password_label = ttk.Label(text="Password", style="BW.TLabel")
        self.password_label.grid(row=1, column=0, padx=8, pady=20)

        self.user_entry = ttk.Entry(textvariable=self.password,
                                    font=("Open Sans", 20), show="*")
        self.user_entry.grid(row=1, column=1, padx=8, pady=20)

        # Login Button
        self.login_btn = ttk.Button(text="Login", style="BW.TButton")
        self.login_btn.grid(row=2, column=0, padx=8, pady=20)

        # Register Button
        self.register_btn = ttk.Button(text="Register", style="BW.TButton")
        self.register_btn.grid(row=2, column=1, padx=8, pady=20)


if __name__ == "__main__":
    main()
