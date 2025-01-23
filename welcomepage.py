import tkinter as tk
from tkinter import PhotoImage

from Interface import interface

def start_app():
    
    print("Starting the application...")
    root.destroy()
    main_app()

def exit_app():
    root.destroy()

def main_app():
    interface()

def create_welcome_page():
    global root
    root = tk.Tk()
    root.title("Welcome Page")
    root.geometry("600x600")


    try:
        logo = PhotoImage(file="logo.png").subsample(7, 7) 
        logo_label = tk.Label(root, image=logo)
        logo_label.image = logo  
        logo_label.place(x=10, y=10)  # Adjust x and y for top-left alignment
    except Exception as e:
        print(f"Error loading logo: {e}")

    # Center the text at the top
    text = tk.Label(root, text="Welcome to the Graph Algorithms App", font=("Arial", 20))
    text.pack(side="top", pady=80)
    text = tk.Label(root, text="Made by Mouatassim El Mehdi under the supervision of DR El Mkhalet Mouna", font=("Arial", 10))
    text.pack(side="bottom", pady=10)


    # Start button
    start_button = tk.Button(root, text="Start", width=15, height=2, command=start_app)
    start_button.pack(pady=10)

    # Exit button
    exit_button = tk.Button(root, text="Exit", width=15, height=2, command=exit_app)
    exit_button.pack(pady=10)

    
    

    root.mainloop()


create_welcome_page()
