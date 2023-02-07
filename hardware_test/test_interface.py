import customtkinter as ctk
from tkinter import Tk, Frame, Canvas
from PIL import ImageTk, Image  
import time
import robot_controller

auth = ""

compartments_status = dict()
compartments_status["1"] = "Empty"
compartments_status["2"] = "Empty"
compartments_status["3"] = "Empty"

def start_page():
    nurse_login = ctk.CTkFrame(master=root)
    nurse_login.pack(pady=20, padx=60, fill="both", expand=True)

    label = ctk.CTkLabel(master=nurse_login, text="Nurse Authentication", font=("Roboto", 40))
    label.grid(row=0, column=1, pady=100, padx=10)

    button = ctk.CTkButton(master=nurse_login, text="1", width=100, height=100, font=("Roboto", 30), command=lambda: make_combination("1"))
    button.grid(row=1, column=0)

    entry1 = ctk.CTkEntry(master=nurse_login, placeholder_text="Password", width=750, height=50, font=("Roboto", 24), show="*")
    entry1.pack(pady=12, padx=10)

    button = ctk.CTkButton(master=nurse_login, text="Submit", width=200, height=50, font=("Roboto", 20), command=lambda: go_to_choose_compartment(nurse_login, "login", entry1))
    button.pack(pady=30, padx=10)


def choose_compartment():
    compartment_frame = ctk.CTkFrame(master=root)
    compartment_frame.pack(pady=20, padx=60, fill="both", expand=True)
    compartment_frame.columnconfigure(index=0, weight=1)

    label = ctk.CTkLabel(master=compartment_frame, text="Choose compartment to load", font=("Roboto", 40))
    label.grid(row=0, column=0, columnspan=2, pady=30, padx=10)

    comp1_button = ctk.CTkButton(master=compartment_frame, text="1", width=200, height=50, font=("Roboto", 20), fg_color="#DDE0E9", text_color="#252843", command=lambda: go_to_load_compartment(compartment_frame, "1"))
    comp1_button.grid(row=1, column=0, pady=30, padx=10, sticky="e")

    comp2_button = ctk.CTkButton(master=compartment_frame, text="2", width=200, height=50, font=("Roboto", 20), fg_color="#DDE0E9", text_color="#252843", command=lambda: go_to_load_compartment(compartment_frame, "2"))
    comp2_button.grid(row=2, column=0, pady=30, padx=10, sticky="e")

    comp3_button = ctk.CTkButton(master=compartment_frame, text="3", width=200, height=50, font=("Roboto", 20), fg_color="#DDE0E9", text_color="#252843", command=lambda: go_to_load_compartment(compartment_frame, "3"))
    comp3_button.grid(row=3, column=0, pady=30, padx=10, sticky="e")

    for id, status in compartments_status.items(): 
        if status == "Empty": 
            status_label = ctk.CTkLabel(master=compartment_frame, text=status, font=("Roboto", 20), text_color="#E95F5F")
            status_label.grid(row=int(id), column=1, padx=(50, 300), sticky="w")
        if status == "Loaded": 
            status_label = ctk.CTkLabel(master=compartment_frame, text=status, font=("Roboto", 20), text_color="#8DF074")
            status_label.grid(row=int(id), column=1, padx=(50, 300), sticky="w")

    submit_button = ctk.CTkButton(master=compartment_frame, text="Submit", width=200, height=50, font=("Roboto", 20), command=lambda: setting_off(compartment_frame))
    submit_button.grid(row=4, column=0, columnspan=2, pady=30, padx=10)

def load_compartment(id): 
    load_text = "Load Compartment " + id
    compartment_frame = ctk.CTkFrame(master=root)
    compartment_frame.pack(pady=20, padx=60, fill="both", expand=True)
    compartment_frame.columnconfigure(index=0, weight=1)

    title = ctk.CTkLabel(master=compartment_frame, text=load_text, font=("Roboto", 40))
    title.grid(row=0, column=0, pady=(200, 30), padx=10)

    explanation = ctk.CTkLabel(master=compartment_frame, text="Please place load in compartment and close the door once finished.", font=("Roboto", 20))
    explanation.grid(row=1, column=0, padx=10)

    compartments_status[id] = "Loaded"
    
    submit_button = ctk.CTkButton(master=compartment_frame, text="Done", width=200, height=50, font=("Roboto", 20), command=lambda: go_to_choose_compartment(compartment_frame, "load", "0000"))
    submit_button.grid(row=4, column=0, pady=30, padx=10)

def set_off(): 
    omw_frame = ctk.CTkFrame(master=root)
    omw_frame.pack(pady=20, padx=60, fill="both", expand=True)

    label = ctk.CTkLabel(master=omw_frame, text="On my way to the hungry little patients!", font=("Roboto", 40))
    label.pack(pady=30, padx=10, fill="x", expand=True)

# ======================== BUTTON COMMANDS ========================

def make_combination(num): 
    auth += num

def go_to_choose_compartment(frame, from_page, text_box): 
    if from_page == "login": 
        input_pass = text_box.get()
        if input_pass == "0000": 
            frame.pack_forget()
            choose_compartment()
        else:
            warn = ctk.CTkLabel(master=frame, text="Wrong password. Try again.", font=("Roboto", 20))
            warn.pack(pady=10, padx=10)
    else: 
        frame.pack_forget()
        choose_compartment()


def go_to_load_compartment(frame, id):
    frame.pack_forget()
    load_compartment(id)
    print("Load compartment page")

def back_to_choose_compartment(frame, id, status): 
    frame.pack_forget() 
    choose_compartment()

def compartment_button(frame, button, id): 
    # turn on LED 
    # load 
    # while unlocked: 
    #     display "Please close compartment" message 
    
    #unclock compartment 
    # while 1: # while unlocked
        # open box icon
        print("button clicked!")
        button.configure(state="disabled")
        # break

        # "Place load in compartment" + cancel 
        # if locked
            # closed box icon 
        # if cancel 
            # remove open box icon
            # exit loop

def setting_off(frame):
    frame.pack_forget()
    set_off()
    return 


# ======================== SETUP AND MAIN ========================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
root = ctk.CTk() 
root.geometry("1024x600")

start_page()
root.mainloop()