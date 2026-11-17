'''
    Ok so it seems like that the example is setting up to create a frame using a class.
    This is something that I want them to show me.
'''

import customtkinter as ctk

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

class myFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.checkbox_1 = ctk.CTkCheckBox(self, text="checkbox 1")
        self.checkbox_1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
        self.checkbox_2 = ctk.CTkCheckBox(self, text="checkbox 2")
        self.checkbox_2.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")


class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("400x180")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.checkbox_frame = myFrame(self)
        self.checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsw")

        self.button = ctk.CTkButton(self, text="my button", command=self.button_callback)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

    def button_callback(self):
        print("button pressed")



# This will run the main loop that will open the window.
app=App()
app.mainloop()