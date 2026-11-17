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

button = ctk.CTkButton(
    app, 
    text="Say hello", 
    #command=greet
)
button.grid(
    row=1, 
    column=0, 
    padx=20, 
    pady=10, 
    sticky="ew"
)

label = ctk.CTkLabel(
    app, 
    text=""
)
label.grid(
    row=2, 
    column=0, 
    padx=20, 
    pady=(10, 20)
)



# This will run the main loop that will open the window.
app.mainloop()