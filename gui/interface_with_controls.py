import customtkinter as ctk
from tkinter import Tk, Frame, Canvas
from PIL import ImageTk, Image  
# import time
# import robot_controller as rc

import RPi.GPIO as GPIO
from adafruit_servokit import ServoKit
import time
import tkinter

# ===================== hardware =====================

kit = ServoKit(channels=16)

SERV_1 = 0
SERV_2 = 1
SERV_3 = 2

BUT_1 = 'UART2_CTS'     # 36
BUT_2 = 'DAP4_DIN'      # 38
BUT_3 = 'DAP4_DOUT'     # 40

LED_1 = 'SPI2_MISO'     # 22
LED_2 = 'SPI1_CS0'      # 24
LED_3 = 'SPI1_CS1'      # 26


# ===================== methods =====================

def turn_on_led(compartment):
    if compartment == '1':
        print("turning on LED 1")
        GPIO.output(LED_1, GPIO.HIGH)
        # GPIO.output(LED_2, GPIO.LOW)
        # GPIO.output(LED_3, GPIO.LOW)

    elif compartment == '2':
        print("turning on LED 2")
        # GPIO.output(LED_1, GPIO.LOW)
        GPIO.output(LED_2, GPIO.HIGH)
        # GPIO.output(LED_3, GPIO.LOW)

    elif compartment == '3':
        print("turning on LED 3")
        # GPIO.output(LED_1, GPIO.LOW)
        # GPIO.output(LED_2, GPIO.LOW)
        GPIO.output(LED_3, GPIO.HIGH)

    else:
        print("turning off all LEDs")
        killAllLED()
    
def turn_off_led(compartment):
    if compartment == '1':
        print("turning on LED 1")
        GPIO.output(LED_1, GPIO.LOW)
        # GPIO.output(LED_2, GPIO.LOW)
        # GPIO.output(LED_3, GPIO.LOW)

    elif compartment == '2':
        print("turning on LED 2")
        # GPIO.output(LED_1, GPIO.LOW)
        GPIO.output(LED_2, GPIO.LOW)
        # GPIO.output(LED_3, GPIO.LOW)

    elif compartment == '3':
        print("turning on LED 3")
        # GPIO.output(LED_1, GPIO.LOW)
        # GPIO.output(LED_2, GPIO.LOW)
        GPIO.output(LED_3, GPIO.LOW)

    else:
        print("turning off all LEDs")
        killAllLED()

def unlock_compartment(compartment): 
    if compartment == '1':
        print("locking compartment 1")

        kit.servo[SERV_1].angle = 180

        # time.sleep(2)

        # print("unlocking compartment 1")

        # kit.servo[SERV_1].angle = 180
            
    elif compartment == '2':
        print("locking compartment 2")

        kit.servo[SERV_2].angle = 180

        # time.sleep(2)

        # print("unlocking compartment 1")

        # kit.servo[SERV_2].angle = 180
        
    elif compartment == '3':
        print("locking compartment 3")

        kit.servo[SERV_3].angle = 180

        # time.sleep(2)

        # print("unlocking compartment 1")

        # kit.servo[SERV_3].angle = 180

    else:
        print("unlocking all")
        killAllServo()

def lock_compartment(compartment): 
    if compartment == '1':
        print("locking compartment 1")

        kit.servo[SERV_1].angle = 0

        # time.sleep(2)

        # print("unlocking compartment 1")

        # kit.servo[SERV_1].angle = 180
            
    elif compartment == '2':
        print("locking compartment 2")

        kit.servo[SERV_2].angle = 0

        # time.sleep(2)

        # print("unlocking compartment 1")

        # kit.servo[SERV_2].angle = 180
        
    elif compartment == '3':
        print("locking compartment 3")

        kit.servo[SERV_3].angle = 0

        # time.sleep(2)

        # print("unlocking compartment 1")

        # kit.servo[SERV_3].angle = 180

    else:
        print("unlocking all")
        killAllServo()

def button1(channel):
    print("button 1 pressed")
    kit.servo[SERV_1].angle = 0
    
    # GPIO.output(LED_1, GPIO.LOW)

    # time.sleep(1)

    # print("unlocking")

    # kit.servo[SERV_1].angle = 0

def button2(channel):
    print("button 2 pressed")
    kit.servo[SERV_2].angle = 0
    # print("compartment 2 is closed")
    # print("locking")

    # kit.servo[SERV_2].angle = 180
    
    # GPIO.output(LED_2, GPIO.LOW)

    # time.sleep(1)

    # print("unlocking")
    
    # kit.servo[SERV_2].angle = 0
    
def button3(channel):
    print("button 3 pressed")
    kit.servo[SERV_3].angle = 0
    # print("compartment 3 is closed")
    # print("locking")

    # kit.servo[SERV_3].angle = 180
    
    # GPIO.output(LED_3, GPIO.LOW)

    # time.sleep(1)

    # print("unlocking")
    
    # kit.servo[SERV_3].angle = 0

def killAllLED():
    GPIO.output(LED_1, GPIO.LOW)
    GPIO.output(LED_2, GPIO.LOW)
    GPIO.output(LED_3, GPIO.LOW)

def killAllServo():
    kit.servo[SERV_1].angle = 180
    kit.servo[SERV_2].angle = 180
    kit.servo[SERV_3].angle = 180


def start_page():
    auth_frame = ctk.CTkFrame(master=root)
    auth_frame.pack(pady=20, padx=60, fill="both", expand=True)

    label = ctk.CTkLabel(master=auth_frame, text="Nurse Authentication", font=("Roboto", 40))
    label.grid(row=0, column=0, pady=(30, 20), padx=10, sticky="ew")

    button_1 = ctk.CTkButton(master=auth_frame, text="1", width=100, height=100, font=("Roboto", 30), corner_radius=0, border_color="black", border_width=1, fg_color="#DDE0E9", text_color="#252843", command=lambda: make_combination("1"))
    button_2 = ctk.CTkButton(master=auth_frame, text="2", width=100, height=100, font=("Roboto", 30), corner_radius=0, border_color="black", border_width=1, fg_color="#DDE0E9", text_color="#252843", command=lambda: make_combination("2"))
    button_3 = ctk.CTkButton(master=auth_frame, text="3", width=100, height=100, font=("Roboto", 30), corner_radius=0, border_color="black", border_width=1, fg_color="#DDE0E9", text_color="#252843", command=lambda: make_combination("3"))
    button_4 = ctk.CTkButton(master=auth_frame, text="4", width=100, height=100, font=("Roboto", 30), corner_radius=0, border_color="black", border_width=1, fg_color="#DDE0E9", text_color="#252843", command=lambda: make_combination("4"))
    button_5 = ctk.CTkButton(master=auth_frame, text="5", width=100, height=100, font=("Roboto", 30), corner_radius=0, border_color="black", border_width=1, fg_color="#DDE0E9", text_color="#252843", command=lambda: make_combination("5"))
    button_6 = ctk.CTkButton(master=auth_frame, text="6", width=100, height=100, font=("Roboto", 30), corner_radius=0, border_color="black", border_width=1, fg_color="#DDE0E9", text_color="#252843", command=lambda: make_combination("6"))
    button_7 = ctk.CTkButton(master=auth_frame, text="7", width=100, height=100, font=("Roboto", 30), corner_radius=0, border_color="black", border_width=1, fg_color="#DDE0E9", text_color="#252843", command=lambda: make_combination("7"))
    button_8 = ctk.CTkButton(master=auth_frame, text="8", width=100, height=100, font=("Roboto", 30), corner_radius=0, border_color="black", border_width=1, fg_color="#DDE0E9", text_color="#252843", command=lambda: make_combination("8"))
    button_9 = ctk.CTkButton(master=auth_frame, text="9", width=100, height=100, font=("Roboto", 30), corner_radius=0, border_color="black", border_width=1, fg_color="#DDE0E9", text_color="#252843", command=lambda: make_combination("9"))
    button_0 = ctk.CTkButton(master=auth_frame, text="0", width=100, height=100, font=("Roboto", 30), corner_radius=0, border_color="black", border_width=1, fg_color="#DDE0E9", text_color="#252843", command=lambda: make_combination("0"))
    submit = ctk.CTkButton(master=auth_frame, text="Submit", width=200, height=100, font=("Roboto", 20), corner_radius=0, command=lambda: go_to_choose_compartment(auth_frame))
    
    button_1.grid(row=1, column=0, sticky="ne")
    button_2.grid(row=1, column=1)
    button_3.grid(row=1, column=2, sticky="nw")
    button_4.grid(row=2, column=0, sticky="ne")
    button_5.grid(row=2, column=1)
    button_6.grid(row=2, column=2, sticky="nw")
    button_7.grid(row=3, column=0, sticky="ne")
    button_8.grid(row=3, column=1)
    button_9.grid(row=3, column=2, sticky="nw")
    button_0.grid(row=4, column=0, pady=(0, 100), sticky="ne")
    submit.grid(row=4, column=1, columnspan=2, pady=(0, 100))

    # entry1 = ctk.CTkEntry(master=auth_frame, placeholder_text="Password", width=750, height=50, font=("Roboto", 24), show="*")
    # entry1.pack(pady=12, padx=10)



def choose_compartment():
    compartment_frame = ctk.CTkFrame(master=root)
    compartment_frame.pack(pady=20, padx=60, fill="both", expand=True)
    compartment_frame.columnconfigure(index=0, weight=1)

    label = ctk.CTkLabel(master=compartment_frame, text="Choose compartment to load", font=("Roboto", 40))
    label.grid(row=0, column=0, columnspan=2, pady=30, padx=10)

    comp1_button = ctk.CTkButton(master=compartment_frame, text="1", width=200, height=75, font=("Roboto", 30), corner_radius=0, fg_color="#DDE0E9", text_color="#252843", command=lambda: go_to_load_compartment(compartment_frame, "1"))
    comp1_button.grid(row=1, column=0, pady=(30, 10), padx=10, sticky="e")

    comp2_button = ctk.CTkButton(master=compartment_frame, text="2", width=200, height=75, font=("Roboto", 30), corner_radius=0, fg_color="#DDE0E9", text_color="#252843", command=lambda: go_to_load_compartment(compartment_frame, "2"))
    comp2_button.grid(row=2, column=0, pady=(0, 10), padx=10, sticky="e")

    comp3_button = ctk.CTkButton(master=compartment_frame, text="3", width=200, height=75, font=("Roboto", 30), corner_radius=0, fg_color="#DDE0E9", text_color="#252843", command=lambda: go_to_load_compartment(compartment_frame, "3"))
    comp3_button.grid(row=3, column=0, pady=(0, 10), padx=10, sticky="e")

    for id, status in compartments_status.items(): 
        if status == "Empty": 
            status_label = ctk.CTkLabel(master=compartment_frame, text=status, font=("Roboto", 30), text_color="#E95F5F")
            status_label.grid(row=int(id), column=1, padx=(50, 300), sticky="w")
        if status == "Loaded": 
            status_label = ctk.CTkLabel(master=compartment_frame, text=status, font=("Roboto", 30), text_color="#8DF074")
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
    
    submit_button = ctk.CTkButton(master=compartment_frame, text="Done", width=200, height=50, font=("Roboto", 20), command=lambda: go_to_choose_compartment(compartment_frame))
    submit_button.grid(row=4, column=0, pady=30, padx=10)

def set_off(): 
    omw_frame = ctk.CTkFrame(master=root)
    omw_frame.pack(pady=20, padx=60, fill="both", expand=True)

    label = ctk.CTkLabel(master=omw_frame, text="On my way to the hungry little patients!", font=("Roboto", 40))
    label.pack(pady=30, padx=10, fill="x", expand=True)

    login_button = ctk.CTkButton(master=omw_frame, text="Login", font=("Roboto", 20), command=lambda: go_to_auth_page(omw_frame))
    login_button.pack(side="bottom", pady=10, padx=10)

    compartment_button = ctk.CTkButton(master=omw_frame, text="Select Compartments", font=("Roboto", 20), command=lambda: go_to_choose_compartment(omw_frame))
    compartment_button.pack(side="bottom", pady=10, padx=10)

# ======================== BUTTON COMMANDS ========================

def make_combination(num): 
    global auth 
    auth += num

def go_to_choose_compartment(frame): 
    global auth, unlock_combination
    if auth == unlock_combination: 
        frame.pack_forget()
        choose_compartment()
    else:
        warn = ctk.CTkLabel(master=frame, text="Wrong password. Try again.", font=("Roboto", 20))
        warn.grid(row=5, column=0, columnspan=3, pady=10, padx=10)
        auth = ""

def go_to_load_compartment(frame, id):
    turn_on_led(id)
    unlock_compartment(id)
    frame.pack_forget()
    load_compartment(id)
    print("Load compartment page")

def setting_off(frame):
    frame.pack_forget()
    set_off()
    return 

def go_to_auth_page(frame): 
    global auth 
    auth = ""
    frame.pack_forget()
    start_page()


# ======================== SETUP AND MAIN ========================
GPIO.setmode(GPIO.TEGRA_SOC)

GPIO.setup(BUT_1, GPIO.IN)
GPIO.setup(BUT_2, GPIO.IN)
GPIO.setup(BUT_3, GPIO.IN)

GPIO.setup(LED_1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED_2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED_3, GPIO.OUT, initial=GPIO.LOW)

GPIO.add_event_detect(BUT_1, GPIO.RISING, callback=button1, bouncetime=3)
GPIO.add_event_detect(BUT_2, GPIO.RISING, callback=button2, bouncetime=3)
GPIO.add_event_detect(BUT_3, GPIO.RISING, callback=button3, bouncetime=3)

auth = ""
unlock_combination = "00"

compartments_status = dict()
compartments_status["1"] = "Empty"
compartments_status["2"] = "Empty"
compartments_status["3"] = "Empty"

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
root = ctk.CTk() 
root.geometry("1024x600")

start_page()
root.mainloop()

GPIO.cleanup()