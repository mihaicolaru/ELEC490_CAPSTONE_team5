import customtkinter as ctk
from tkinter import Tk, Frame, Canvas
from PIL import ImageTk, Image  
import time

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk() 
root.geometry("1024x600")

def login(frame1, text_box): 
    input_pass = text_box.get()
    if input_pass == "0000": 
        frame1.pack_forget()
        assign_compartment()
        print("Test")
    else:
        warn = ctk.CTkLabel(master=frame1, text="Wrong password. Try again.", font=("Roboto", 20))
        warn.pack(pady=10, padx=10)


def start_page():
    nurse_login = ctk.CTkFrame(master=root)
    nurse_login.pack(pady=20, padx=60, fill="both", expand=True)

    label = ctk.CTkLabel(master=nurse_login, text="Nurse Authentication", font=("Roboto", 40))
    label.pack(pady=100, padx=10)

    entry1 = ctk.CTkEntry(master=nurse_login, placeholder_text="Password", width=750, height=50, font=("Roboto", 24), show="*")
    entry1.pack(pady=12, padx=10)

    button = ctk.CTkButton(master=nurse_login, text="Submit", width=200, height=50, font=("Roboto", 20), command=lambda: login(nurse_login, entry1))
    button.pack(pady=30, padx=10)

def compartment_button(frame, button, id): 
    # turn on LED 
    # load 
    # while unlocked: 
    #     display "Please close compartment" message 
    
    #unclock compartment 
    while 1: # while unlocked
        # open box icon
        print("button clicked!")
        button.configure(state="disabled")
        break

        # "Place load in compartment" + cancel 
        # if locked
            # closed box icon 
        # if cancel 
            # remove open box icon
            # exit loop

def cancel_load(label, btn): 
    label.grid_forget() 
    btn.grid_forget()


def setting_off(frame):
    frame.pack_forget()
    set_off()
    return 


def assign_compartment():
    compartment_frame = ctk.CTkFrame(master=root)
    compartment_frame.pack(pady=20, padx=60, fill="both", expand=True)
    compartment_frame.columnconfigure(index=0, weight=1)

    label = ctk.CTkLabel(master=compartment_frame, text="Load Compartments", font=("Roboto", 40))
    label.grid(row=0, column=0, pady=30, padx=10)

    comp1_button = ctk.CTkButton(master=compartment_frame, text="1", width=200, height=50, font=("Roboto", 20), command=lambda: compartment_button(compartment_frame, comp1_button, 1))
    comp1_button.grid(row=1, column=0, pady=30, padx=10)

    comp2_button = ctk.CTkButton(master=compartment_frame, text="2", width=200, height=50, font=("Roboto", 20), command=lambda: compartment_button(compartment_frame, comp2_button, 2))
    comp2_button.grid(row=2, column=0, pady=30, padx=10)

    comp3_button = ctk.CTkButton(master=compartment_frame, text="3", width=200, height=50, font=("Roboto", 20), command=lambda: compartment_button(compartment_frame, comp3_button, 3))
    comp3_button.grid(row=3, column=0, pady=30, padx=10)

    submit_button = ctk.CTkButton(master=compartment_frame, text="Submit", width=200, height=50, font=("Roboto", 20), command=lambda: setting_off(compartment_frame))
    submit_button.grid(row=4, column=0, pady=30, padx=10)

def set_off(): 
    omw_frame = ctk.CTkFrame(master=root)
    omw_frame.pack(pady=20, padx=60, fill="both", expand=True)

    label = ctk.CTkLabel(master=omw_frame, text="On my way to patient!", font=("Roboto", 40))
    label.pack(pady=30, padx=10, fill="x", expand=True)


start_page()
root.mainloop()