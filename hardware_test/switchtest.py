# import RPi.GPIO as GPIO
# import time

# # LED pins 22, 24, 26; bcm: 25, 8, 7
# # switch pins 36, 38, 40

# LED_22 = 22
# LED_24 = 24
# LED_26 = 26

# SWITCH_1 = 36
# SWITCH_2 = 38
# SWITCH_3 = 40


# def main():
#     GPIO.setmode(GPIO.BOARD)
#     GPIO.setup(LED_22, GPIO.OUT, initial=GPIO.LOW)
#     GPIO.setup(LED_24, GPIO.OUT, initial=GPIO.LOW)
#     GPIO.setup(LED_26, GPIO.OUT, initial=GPIO.LOW)
    
#     GPIO.setup(SWITCH_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#     GPIO.setup(SWITCH_2, GPIO.IN)
#     GPIO.setup(SWITCH_3, GPIO.IN)

#     print("starting now")
	
#     pv1 = None
#     pv2 = None
#     pv3 = None

#     try:
#         while 1:
#             state = GPIO.input(SWITCH_1)

#             print("button state: ", state)

#             if state == GPIO.HIGH:
#                 print("button was pushed")

#             time.sleep(5)    

#             # GPIO.wait_for_edge(SWITCH_1, GPIO.FALLING)
#             # cv1 = GPIO.input(SWITCH_1)
#             # cv2 = GPIO.input(SWITCH_2)
#             # cv3 = GPIO.input(SWITCH_3)


#             # if cv1 != pv1:
#             #     print("turning on led 1")
#             #     GPIO.output(LED_22, GPIO.HIGH)
#             #     GPIO.output(LED_24, GPIO.LOW)
#             #     GPIO.output(LED_26, GPIO.LOW)
#             #     pv1 = cv1
#             #     time.sleep(1)
#             #     continue
#             # elif cv2 != pv2:
#             #     print("turning on led 2")
#             #     GPIO.output(LED_24, GPIO.HIGH)
#             #     GPIO.output(LED_22, GPIO.LOW)
#             #     GPIO.output(LED_26, GPIO.LOW)
#             #     pv2 = cv2
#             #     time.sleep(1)
#             #     continue
#             # elif cv3 != pv3:
#             #     print("turning on led 3")
#             #     GPIO.output(LED_26, GPIO.HIGH)
#             #     GPIO.output(LED_24, GPIO.LOW)
#             #     GPIO.output(LED_22, GPIO.LOW)
#             #     pv3 = cv3
#             #     time.sleep(1)
#             #     continue
#             # else:
#             #     time.sleep(1)
#             #     # print("bye")
#             #     # GPIO.output(LED_22, GPIO.LOW)
#             #     # GPIO.output(LED_24, GPIO.LOW)
#             #     # GPIO.output(LED_26, GPIO.LOW)
#             #     # break
#             #     continue
#     finally:
#         GPIO.cleanup()



# main()

# import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

# def button_callback(channel):
#     print("Button was pushed!")

# GPIO.setwarnings(False) # Ignore warning for now
# GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
# GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

# GPIO.add_event_detect(36,GPIO.RISING,callback=button_callback) # Setup event on pin 10 rising edge

# message = input("Press enter to quit\n\n") # Run until someone presses enter

# GPIO.cleanup() # Clean up

import RPi.GPIO as GPIO
import time
but_pin1= 'UART2_CTS'

LED_22 = 'SPI2_MISO'


def button1(channel):
    print("‘button1’")
    print("turning on led 1")
    GPIO.output(LED_22, GPIO.HIGH)
    time.sleep(3)
    GPIO.output(LED_22, GPIO.LOW)


GPIO.setmode(GPIO.TEGRA_SOC)
GPIO.setup(but_pin1, GPIO.IN)

GPIO.setup(LED_22, GPIO.OUT, initial=GPIO.LOW)


GPIO.add_event_detect(but_pin1, GPIO.FALLING, callback=button1, bouncetime=3)


message=input("Press enter to stop")
GPIO.cleanup()