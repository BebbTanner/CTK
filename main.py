'''
    Ok so it seems like that the example is setting up to create a frame using a class.
    This is something that I want them to show me.
'''

import customtkinter as ctk



ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")



class myFrame(ctk.CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.title = title
        self.checkboxes = []

        self.title = ctk.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")



class MyRadiobuttonFrame(ctk.CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.title = title
        self.radiobuttons = []
        self.variable = ctk.StringVar(value="")

        self.title = ctk.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")



class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("400x220")
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.checkbox_frame = myFrame(self, "Values", values=["value 1", "value 2", "value 3"])
        self.checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")
        self.radiobutton_frame = MyRadiobuttonFrame(self, "Options", values=["option 1", "option 2", "option 3"])
        self.radiobutton_frame.grid(row=0, column=1, padx=(0, 10), pady=(10, 0), sticky="nsew")

        self.button = ctk.CTkButton(self, text="my button")
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan=2)



# This will run the main loop that will open the window.
app=App()
app.mainloop()