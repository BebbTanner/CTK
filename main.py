import customtkinter as ctk

# This should be the declartion for the main window.
app = ctk.CTk()
app.title("Custom Tkinter")
app.geometry("500x500")

# Widgets
entry = ctk.CTkEntry(
    app, 
    placeholder_text="Your name"
)
entry.grid(
    row=0, 
    column=0, 
    padx=20, 
    pady=(20, 10), 
    sticky="ew"
)


# This will run the main loop that will open the window.
app.mainloop()