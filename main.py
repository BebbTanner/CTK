import customtkinter as ctk



ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")



class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        app = ctk.CTk()
        app.title("Custom Tkinter")
        app.geometry("500x500")

        self.entry = ctk.CTkEntry(self, placeholder_text="Your name")
        self.entry.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="ew")
        self.entry.bind("<Return>", self.greet)

        self.button = ctk.CTkButton(self, text="Say hello", command=self.greet)
        self.button.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        self.label = ctk.CTkLabel(self, text="")
        self.label.grid(row=2, column=0, padx=20, pady=(10, 20))

    def greet(self, event=None):
        name = self.entry.get().strip()
        if name:
            self.label.configure(text=f"Hello, {name}!")
        else:
            self.label.configure(text="Please enter your name.")



# This will run the main loop that will open the window.
app=App()
app.mainloop()