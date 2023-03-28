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

# ========================== GUI START =====================
def get_patient(room): 
    patient_data = {"Room 100": "Jane Doe", 
                    "Room 101": "Ralf Lauren",
                    "Room 102": "Mackenzie Alfred",
                    "Room 103": "Jasper Chen",
                    "Room 104": "Alice Ron"}
    if room in patient_data: 
        return patient_data[room]
    return "-"
    

class ScrollableRadiobuttonFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, item_list, command=None, **kwargs):
        super().__init__(master, **kwargs)

        self.command = command
        self.radiobutton_variable = ctk.StringVar()
        self.radiobutton_list = []
        for i, item in enumerate(item_list):
            self.add_item(item)

    def add_item(self, item):
        radiobutton = ctk.CTkRadioButton(self, text=item, value=item, variable=self.radiobutton_variable, font=("Roboto", 18))
        if self.command is not None:
            radiobutton.configure(command=self.command)
        radiobutton.grid(row=len(self.radiobutton_list), column=0, pady=(0, 15))
        self.radiobutton_list.append(radiobutton)

    def remove_item(self, item):
        for radiobutton in self.radiobutton_list:
            if item == radiobutton.cget("text"):
                radiobutton.destroy()
                self.radiobutton_list.remove(radiobutton)
                return

    def get_checked_item(self):
        return self.radiobutton_variable.get()

# ======================== PAGES ========================
def start_page():
    auth_frame = ctk.CTkFrame(master=root)
    auth_frame.pack(pady=20, padx=60, fill="both", expand=True)

    title_frame = ctk.CTkFrame(master=auth_frame, fg_color="transparent", bg_color="transparent")
    title_frame.pack(pady=20, padx=10, fill="x", expand=True)

    text = ctk.CTkLabel(master=title_frame, text="Nurse Authentication", font=("Roboto", 40))
    text.pack(pady=20, padx=10, fill="x", expand=False)

    button_frame = ctk.CTkFrame(master=auth_frame)
    button_frame.pack(pady=(0, 20), padx=10)

    button_1 = ctk.CTkButton(master=button_frame, text="1", width=100, height=100, font=("Roboto", 30), corner_radius=0, border_color="black", border_width=1, fg_color="#DDE0E9", text_color="#252843", command=lambda: make_combination("1"))
    button_2 = ctk.CTkButton(master=button_frame, text="2", width=100, height=100, font=("Roboto", 30), corner_radius=0, border_color="black", border_width=1, fg_color="#DDE0E9", text_color="#252843", command=lambda: make_combination("2"))
    button_3 = ctk.CTkButton(master=button_frame, text="3", width=100, height=100, font=("Roboto", 30), corner_radius=0, border_color="black", border_width=1, fg_color="#DDE0E9", text_color="#252843", command=lambda: make_combination("3"))
    button_4 = ctk.CTkButton(master=button_frame, text="4", width=100, height=100, font=("Roboto", 30), corner_radius=0, border_color="black", border_width=1, fg_color="#DDE0E9", text_color="#252843", command=lambda: make_combination("4"))
    button_5 = ctk.CTkButton(master=button_frame, text="5", width=100, height=100, font=("Roboto", 30), corner_radius=0, border_color="black", border_width=1, fg_color="#DDE0E9", text_color="#252843", command=lambda: make_combination("5"))
    button_6 = ctk.CTkButton(master=button_frame, text="6", width=100, height=100, font=("Roboto", 30), corner_radius=0, border_color="black", border_width=1, fg_color="#DDE0E9", text_color="#252843", command=lambda: make_combination("6"))
    button_7 = ctk.CTkButton(master=button_frame, text="7", width=100, height=100, font=("Roboto", 30), corner_radius=0, border_color="black", border_width=1, fg_color="#DDE0E9", text_color="#252843", command=lambda: make_combination("7"))
    button_8 = ctk.CTkButton(master=button_frame, text="8", width=100, height=100, font=("Roboto", 30), corner_radius=0, border_color="black", border_width=1, fg_color="#DDE0E9", text_color="#252843", command=lambda: make_combination("8"))
    button_9 = ctk.CTkButton(master=button_frame, text="9", width=100, height=100, font=("Roboto", 30), corner_radius=0, border_color="black", border_width=1, fg_color="#DDE0E9", text_color="#252843", command=lambda: make_combination("9"))
    button_0 = ctk.CTkButton(master=button_frame, text="0", width=100, height=100, font=("Roboto", 30), corner_radius=0, border_color="black", border_width=1, fg_color="#DDE0E9", text_color="#252843", command=lambda: make_combination("0"))
    submit = ctk.CTkButton(master=button_frame, text="Submit", width=200, height=100, font=("Roboto", 20), corner_radius=0, command=lambda: go_to_choose_compartment(auth_frame))
    
    button_1.grid(row=1, column=0)
    button_2.grid(row=1, column=1)
    button_3.grid(row=1, column=2)
    button_4.grid(row=2, column=0)
    button_5.grid(row=2, column=1)
    button_6.grid(row=2, column=2)
    button_7.grid(row=3, column=0)
    button_8.grid(row=3, column=1)
    button_9.grid(row=3, column=2)
    button_0.grid(row=4, column=0, pady=(0, 200))
    submit.grid(row=4, column=1, columnspan=2, pady=(0, 200))

def choose_compartment():
    compartment_frame = ctk.CTkFrame(master=root)
    compartment_frame.pack(pady=20, padx=60, fill="both", expand=True)
    compartment_frame.columnconfigure(index=0, weight=1)
    compartment_frame.rowconfigure(index=0, weight=0)

    mapping_button = ctk.CTkButton(master=compartment_frame, text="Mapping", width=100, height=40, font=("Roboto", 15), command=lambda: go_to_mapping(compartment_frame))
    mapping_button.grid(row=0, column=1, sticky="nse", padx=10, pady=10)

    label = ctk.CTkLabel(master=compartment_frame, text="Choose compartment to load", font=("Roboto", 40))
    label.grid(row=0, column=0, columnspan=2, rowspan=2, pady=30, padx=10, sticky="n")

    comp1_button = ctk.CTkButton(master=compartment_frame, text="1", width=200, height=75, font=("Roboto", 30), corner_radius=0, fg_color="#DDE0E9", text_color="#252843", command=lambda: go_to_load_compartment(compartment_frame, "1"))
    comp1_button.grid(row=2, column=0, pady=(30, 10), padx=10, sticky="e")

    comp2_button = ctk.CTkButton(master=compartment_frame, text="2", width=200, height=75, font=("Roboto", 30), corner_radius=0, fg_color="#DDE0E9", text_color="#252843", command=lambda: go_to_load_compartment(compartment_frame, "2"))
    comp2_button.grid(row=3, column=0, pady=(0, 10), padx=10, sticky="e")

    comp3_button = ctk.CTkButton(master=compartment_frame, text="3", width=200, height=75, font=("Roboto", 30), corner_radius=0, fg_color="#DDE0E9", text_color="#252843", command=lambda: go_to_load_compartment(compartment_frame, "3"))
    comp3_button.grid(row=4, column=0, pady=(0, 10), padx=10, sticky="e")

    for id, status in compartments_status.items(): 
        if status == "Empty": 
            status_label = ctk.CTkLabel(master=compartment_frame, text=status, font=("Roboto", 20), text_color="#E95F5F")
            status_label.grid(row=int(id)+1, column=1, padx=(50, 300), sticky="w")
        else: 
            status_label = ctk.CTkLabel(master=compartment_frame, text=status, font=("Roboto", 20), text_color="#8DF074")
            status_label.grid(row=int(id)+1, column=1, padx=(50, 300), sticky="w")

    submit_button = ctk.CTkButton(master=compartment_frame, text="Submit", width=200, height=50, font=("Roboto", 20), command=lambda: setting_off(compartment_frame))
    submit_button.grid(row=5, column=0, columnspan=2, pady=30, padx=10)

def mapping(): 
    mapping_frame = ctk.CTkFrame(master=root, bg_color="transparent", fg_color="transparent")
    mapping_frame.pack(pady=20, padx=60, fill="y", expand=True)
    mapping_frame.rowconfigure(index=0, weight=2)

    text = ctk.CTkLabel(master=mapping_frame, text="Mapping environment", font=("Roboto", 40))
    text.grid(row=0, column=0, pady=20)

    done_button = ctk.CTkButton(master=mapping_frame, text="Done", font=("Roboto", 20), width=110, height=50, command=lambda: go_to_choose_compartment(mapping_frame))
    done_button.grid(row=1, column=0, pady=20)

def load_compartment(id): 
    load_text = "Load Compartment " + id

    compartment_frame = ctk.CTkFrame(master=root)
    compartment_frame.pack(pady=20, padx=20, fill="both", expand=True)

    title = ctk.CTkLabel(master=compartment_frame, text=load_text, font=("Roboto", 40))
    title.pack(pady=20, padx=10, fill="x", expand=False)

    options_frame = ctk.CTkFrame(master=compartment_frame)
    options_frame.pack(pady=10, padx=10, fill="both", expand=True)

    title_info_confirmation = ctk.CTkLabel(master=options_frame, text="Patient and Load Confirmation", font=("Roboto", 20))
    title_info_confirmation.grid(row=0, column=1, columnspan=2)

    patient_info = ctk.CTkLabel(master=options_frame, text="Patient: -", font=("Roboto", 20))
    patient_info.grid(row=1, column=1, columnspan=2, padx=10, pady=10, sticky="nw")
    
    room_info = ctk.CTkLabel(master=options_frame, text="Room: -", font=("Roboto", 20))
    room_info.grid(row=2, column=1, columnspan=2, padx=10, pady=10, sticky="nw")

    load_info = ctk.CTkLabel(master=options_frame, text="Load:", font=("Roboto", 20))
    load_info.grid(row=3, column=1, padx=(10, 1), pady=10, sticky="nw")

    def load_option_callback(selection):
        print(selection)
        if not selection: 
            selection = "Food"
        compartments_status[id] = "Loaded with " + selection 

    optionmenu_var = ctk.StringVar(value="Food")  # set initial value
    load_options = ctk.CTkOptionMenu(master=options_frame,
                                        width=300,
                                        values=["Food", "Sheets", "Masks", "Other"],
                                        variable=optionmenu_var, 
                                        command=load_option_callback,
                                        font=("Roboto", 20))
    load_options.grid(row=3, column=2, padx=(0,10), pady=10, sticky="nw")

    room_select_title = ctk.CTkLabel(master=options_frame, text="Select Room", font=("Roboto", 18))
    room_select_title.grid(row=0, column=0)
    
    room_select = ScrollableRadiobuttonFrame(master=options_frame, width=400, height=250, command=lambda: checkbox_frame_event(room_select.get_checked_item()), item_list=[f"Room {i}" for i in range(100, 105)])
    room_select.grid(row=1, column=0, rowspan=4, padx=15, pady=15)

    def checkbox_frame_event(room): 
        patient_text = "Patient: " + get_patient(room)
        patient_info.configure(text=patient_text, text_color="#8DF074")

        room_text = "Room: " + room
        room_info.configure(text=room_text, text_color="#8DF074")
        rooms[int(id) - 1] = room

    explanation = ctk.CTkLabel(master=options_frame, text="Place load in compartment and close the door once finished.", font=("Roboto", 16))
    explanation.grid(row=4, column=1, columnspan=2, sticky="nsw")

    if compartments_status[id] == "Empty":
        compartments_status[id] = "Loaded with Food"
    
    submit_button = ctk.CTkButton(master=compartment_frame, text="Confirm", width=200, height=50, font=("Roboto", 20), command=lambda: go_to_choose_compartment(compartment_frame))
    submit_button.pack(pady=30, padx=10)

def set_off(): 
    omw_frame = ctk.CTkFrame(master=root, bg_color="transparent", fg_color="transparent")
    omw_frame.pack(pady=20, padx=60, fill="y", expand=True)
    omw_frame.rowconfigure(index=0, weight=1)

    for i in range(len(rooms)):
        if rooms[i] != "-":
            msg = "On my way to " + rooms[i]
            text = ctk.CTkLabel(master=omw_frame, text=msg, font=("Roboto", 40))
            text.grid(row=0, column=0, columnspan=2, pady=20, padx=10)

            login_button = ctk.CTkButton(master=omw_frame, text="Login", font=("Roboto", 20), width=110, height=50, command=lambda: go_to_auth_page(omw_frame))
            login_button.grid(row=1, column=0, pady=30, padx=10, sticky="nw")

            patient_button = ctk.CTkButton(master=omw_frame, text="Patient", font=("Roboto", 20), width=250, height=50, command=lambda: go_to_patient(omw_frame))
            patient_button.grid(row=1, column=1, pady=30, padx=10, sticky="ne")
            break

        if i == 2 and rooms[i] == "-":
            text = ctk.CTkLabel(master=omw_frame, text="No deliveries remaining. Returning to base", font=("Roboto", 40))
            text.grid(row=0, column=0, pady=20, padx=10)

            login_button = ctk.CTkButton(master=omw_frame, text="Login", font=("Roboto", 20), width=110, height=50, command=lambda: go_to_auth_page(omw_frame))
            login_button.grid(row=1, column=0, pady=30, padx=10)

def patient_page(): 
    patient_frame = ctk.CTkFrame(master=root, bg_color="transparent", fg_color="transparent")
    patient_frame.pack(pady=20, padx=60, fill="y", expand=True)
    patient_frame.rowconfigure(index=1, weight=1)

    for compartment in range(len(rooms)):
        if rooms[compartment] != "-":
            turn_on_led(str(compartment+1))
            unlock_compartment(str(compartment+1))
        
            patient_name = get_patient(rooms[compartment])
            text1 = ctk.CTkLabel(master=patient_frame, text=patient_name, font=("Roboto", 40), text_color="#8DF074")
            text1.grid(row=0, column=0, columnspan=2, pady=(100, 5), padx=10, sticky="s")

            msg = "Please remove delivery from compartment " + str(compartment + 1)
            text2 = ctk.CTkLabel(master=patient_frame, text=msg, font=("Roboto", 40))
            text2.grid(row=1, column=0, columnspan=2, pady=20, padx=10, sticky="n")
            
            text3 = ctk.CTkLabel(master=patient_frame, text="Close compartment once finished.", font=("Roboto", 30))
            text3.grid(row=2, column=0, columnspan=2, pady=20, padx=10, sticky="n")

            rooms[compartment] = "-"
            compartments_status[str(compartment + 1)] = "Empty"
            break

    login_button = ctk.CTkButton(master=patient_frame, text="Login", font=("Roboto", 20), width=110, height=50, command=lambda: go_to_auth_page(patient_frame))
    login_button.grid(row=2, column=0, pady=50, padx=10, sticky="ne")

    next_patient_button = ctk.CTkButton(master=patient_frame, text="Next patient", font=("Roboto", 20), width=250, height=50, command=lambda: setting_off(patient_frame))
    next_patient_button.grid(row=2, column=1, pady=50, padx=10, sticky="nw")

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
        warn = ctk.CTkLabel(master=frame, text="Wrong password. Try again.", font=("Roboto", 14))
        warn.pack(side="bottom")
        auth = ""

def go_to_load_compartment(frame, id):
    turn_on_led(id)
    unlock_compartment(id)
    frame.pack_forget()
    load_compartment(id)
    print("Load compartment page")

def go_to_mapping(frame): 
    frame.pack_forget() 
    mapping()

def setting_off(frame):
    for i in range(0, 2): 
        turn_off_led(i)
    frame.pack_forget()
    set_off()
    return 

def go_to_patient(frame): 
    frame.pack_forget()
    patient_page()

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
unlock_combination = "123"

compartments_status = dict()
compartments_status["1"] = "Empty"
compartments_status["2"] = "Empty"
compartments_status["3"] = "Empty"

rooms = dict()
rooms = ["-", "-", "-"]

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
root = ctk.CTk() 
root.geometry("1024x600")

start_page()
root.mainloop()

GPIO.cleanup()