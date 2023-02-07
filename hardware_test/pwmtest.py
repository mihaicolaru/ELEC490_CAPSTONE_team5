
# import RPi.GPIO as GPIO   # Import the GPIO library.
# import time               # Import time library

# GPIO.setmode(GPIO.BOARD)  # Set Pi to use pin number when referencing GPIO pins.
#                           # Can use GPIO.setmode(GPIO.BCM) instead to use 
#                           # Broadcom SOC channel names.

# GPIO.setup(33, GPIO.OUT)  # Set GPIO pin 12 to output mode.
# pwm = GPIO.PWM(33, 50)   # Initialize PWM on pwmPin 100Hz frequency

# # main loop of program
# print("\nPress Ctl C to quit \n")  # Print blank line before and after message.
# dc=0                               # set dc variable to 0 for 0%
# pwm.start(dc)                      # Start PWM with 0% duty cycle

# try:
#   while True:                      # Loop until Ctl C is pressed to stop.
#     for dc in range(0, 101, 5):    # Loop 0 to 100 stepping dc by 5 each loop
#       pwm.ChangeDutyCycle(dc)
#       time.sleep(0.05)             # wait .05 seconds at current LED brightness
#       print(dc)
#     for dc in range(95, 0, -5):    # Loop 95 to 5 stepping dc down by 5 each loop
#       pwm.ChangeDutyCycle(dc)
#       time.sleep(0.05)             # wait .05 seconds at current LED brightness
#       print(dc)
# except KeyboardInterrupt:
#   print("Ctl C pressed - ending program")

# pwm.stop()                         # stop PWM
# GPIO.cleanup()

import RPi.GPIO as GPIO

import time


MOT_1 = 'GPIO_PE6'      # 33

IN_A = 'DAP4_SCLK'      # 12
IN_B = 'GPIO_PZ0'       # 31

MOT_2 = 'LCD_BL_PW'     # 32

IN_C = 'SPI1_MOSI'      # 19
IN_D = 'CAM_AF_EN'      # 29


def testPWM():
    # set directgion for each motor
    GPIO.output(IN_A, GPIO.HIGH)
    GPIO.output(IN_B, GPIO.LOW)

    GPIO.output(IN_C, GPIO.LOW)
    GPIO.output(IN_D, GPIO.HIGH)

    dc=0                               # set dc variable to 0 for 0%
    
    pwm1.start(dc)                      # Start PWM with 0% duty cycle
    pwm2.start(dc)                      # Start PWM with 0% duty cycle
    
    # for dc in range(20, 30, 10):
    #   pwm1.ChangeDutyCycle(0)
    #   pwm2.ChangeDutyCycle(10)
    #   time.sleep(3)
    #   print(f'sending {dc} to motors 1 and 2')
    
    pwm1.ChangeDutyCycle(50)
    pwm2.ChangeDutyCycle(30)
    
    input("press enter")

    pwm1.ChangeDutyCycle(0)
    pwm2.ChangeDutyCycle(0)

    GPIO.output(IN_A, GPIO.LOW)
    GPIO.output(IN_B, GPIO.LOW)
    GPIO.output(IN_C, GPIO.LOW)
    GPIO.output(IN_D, GPIO.LOW)

    pwm1.stop()
    pwm2.stop()

GPIO.setmode(GPIO.TEGRA_SOC)

# MOTORS

GPIO.setup(MOT_1, GPIO.OUT)
GPIO.setup(MOT_2, GPIO.OUT)

GPIO.setup(IN_A, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN_B, GPIO.OUT, initial=GPIO.LOW)

GPIO.setup(IN_C, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN_D, GPIO.OUT, initial=GPIO.LOW)


pwm1 = GPIO.PWM(MOT_1, 100)   # Initialize PWM on pwmPin 50Hz frequency
pwm2 = GPIO.PWM(MOT_2, 100)   # Initialize PWM on pwmPin 50Hz frequency

testPWM()

pwm1.stop()                         # stop PWM1
pwm2.stop()                         # stop PWM1

GPIO.cleanup()