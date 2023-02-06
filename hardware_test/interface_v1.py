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

MOT_1 = 'GPIO_PE6'      # 33

IN_A = 'DAP4_SCLK'      # 12
IN_B = 'GPIO_PZ0'       # 31

MOT_2 = 'LCD_BL_PW'     # 32

IN_C = 'SPI1_MOSI'      # 19
IN_D = 'CAM_AF_EN'      # 29


# ===================== methods =====================

def testLED():
    while 1:
        compartment = input("test LED (1, 2 or 3)\nk - kill all\nq - quit\n")

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

        elif compartment == 'k':
            print("turning off all LEDs")
            killAllLED()

        elif compartment == 'q':
            break

        else:
            print("invalid input")


def testLocking():
    while 1:
        compartment = input("test Locking (1, 2 or 3)\nu - unlock all\nq - quit\n")

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

        elif compartment == 'u':
            print("unlocking all")
            killAllServo()

        elif compartment == 'q':
            break

        else:
            print("invalid input")

def testPWM():
    dc=0                               # set dc variable to 0 for 0%
    
    pwm1.start(dc)                      # Start PWM with 0% duty cycle
    pwm2.start(dc)                      # Start PWM with 0% duty cycle

    while 1:
        # set direction for each motor
        direction = input("select direction:\n1 - forward\n2 - backward\n3 - turn right\n4 - turn left\nk - kill pwm\nq - quit\n")

        if direction == '1':
            GPIO.output(IN_A, GPIO.LOW)
            GPIO.output(IN_B, GPIO.HIGH)
            GPIO.output(IN_C, GPIO.HIGH)
            GPIO.output(IN_D, GPIO.LOW)

            speed = input("forward - select speed:\n1 - slow\n2 - cruise\n3 - max\nq - quit\n")
            if speed == ' 1':
                dc = 20
            elif speed == '2':
                dc = 50
            elif speed == '3':
                dc = 80
            elif speed == 'q':
                dc = 0            

            input("start test?")

            print(f'sending {dc} to motors 1 and 2')
            pwm1.ChangeDutyCycle(dc)
            pwm2.ChangeDutyCycle(dc)
            
            input("press enter to stop")

            print("stopping motors")
            dc = 0
            pwm1.ChangeDutyCycle(dc)
            pwm2.ChangeDutyCycle(dc)

        elif direction == '2':
            GPIO.output(IN_A, GPIO.HIGH)
            GPIO.output(IN_B, GPIO.LOW)
            GPIO.output(IN_C, GPIO.LOW)
            GPIO.output(IN_D, GPIO.HIGH)

            speed = input("backward - select speed:\n1 - slow\n2 - cruise\n3 - max\nq - quit\n")
            if speed == ' 1':
                dc = 20
            elif speed == '2':
                dc = 50
            elif speed == '3':
                dc = 80
            elif speed == 'q':
                dc = 0            

            input("start test?")

            print(f'sending {dc} to motors 1 and 2')
            pwm1.ChangeDutyCycle(dc)
            pwm2.ChangeDutyCycle(dc)
            
            input("press enter to stop")

            print("stopping motors")
            dc = 0
            pwm1.ChangeDutyCycle(dc)
            pwm2.ChangeDutyCycle(dc)

        elif direction == '3':
            GPIO.output(IN_A, GPIO.LOW)
            GPIO.output(IN_B, GPIO.HIGH)
            GPIO.output(IN_C, GPIO.HIGH)
            GPIO.output(IN_D, GPIO.LOW)

            speed = input("turn right - select speed:\n1 - slow\n2 - cruise\n3 - max\nq - quit\n")
            if speed == ' 1':
                dc = 20
            elif speed == '2':
                dc = 50
            elif speed == '3':
                dc = 80
            elif speed == 'q':
                dc = 0            

            input("start test?")

            print(f'sending {dc} to motors 1 and 2')
            pwm1.ChangeDutyCycle(dc)
            pwm2.ChangeDutyCycle(dc)
            
            input("press enter to stop")

            print("stopping motors")
            dc = 0
            pwm1.ChangeDutyCycle(dc)
            pwm2.ChangeDutyCycle(dc)

        elif direction == '4':
            GPIO.output(IN_A, GPIO.LOW)
            GPIO.output(IN_B, GPIO.HIGH)
            GPIO.output(IN_C, GPIO.HIGH)
            GPIO.output(IN_D, GPIO.LOW)

            speed = input("turn left - select speed:\n1 - slow\n2 - cruise\n3 - max\nq - quit\n")
            if speed == ' 1':
                dc = 20
            elif speed == '2':
                dc = 50
            elif speed == '3':
                dc = 80
            elif speed == 'q':
                dc = 0            

            input("start test?")

            print(f'sending {dc} to motors 1 and 2')
            pwm1.ChangeDutyCycle(dc)
            pwm2.ChangeDutyCycle(dc)
            
            input("press enter to stop")

            print("stopping motors")
            dc = 0
            pwm1.ChangeDutyCycle(dc)
            pwm2.ChangeDutyCycle(dc)

        elif direction == 'k':
            print("killing pwm")
            pwm1.ChangeDutyCycle(0)
            pwm2.ChangeDutyCycle(0)

        elif direction == 'q':
            pwm1.ChangeDutyCycle(0)
            pwm2.ChangeDutyCycle(0)

            pwm1.stop()
            pwm2.stop()
            break

        else:
            print("invalid input")

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


# ===================== setup =====================

GPIO.setmode(GPIO.TEGRA_SOC)

GPIO.setup(BUT_1, GPIO.IN)
GPIO.setup(BUT_2, GPIO.IN)
GPIO.setup(BUT_3, GPIO.IN)

GPIO.setup(LED_1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED_2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED_3, GPIO.OUT, initial=GPIO.LOW)


# MOTORS

GPIO.setup(MOT_1, GPIO.OUT)
GPIO.setup(MOT_2, GPIO.OUT)

GPIO.setup(IN_A, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN_B, GPIO.OUT, initial=GPIO.LOW)

GPIO.setup(IN_C, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN_D, GPIO.OUT, initial=GPIO.LOW)


pwm1 = GPIO.PWM(MOT_1, 50)   # Initialize PWM on pwmPin 50Hz frequency
pwm2 = GPIO.PWM(MOT_2, 50)   # Initialize PWM on pwmPin 50Hz frequency


GPIO.add_event_detect(BUT_1, GPIO.RISING, callback=button1, bouncetime=1)
GPIO.add_event_detect(BUT_2, GPIO.RISING, callback=button2, bouncetime=1)
GPIO.add_event_detect(BUT_3, GPIO.RISING, callback=button3, bouncetime=1)


# ===================== main =====================

killAllLED()
# killAllServo()

while 1:
    print("which component would you like to test?")
    choice = input("1: LEDS\n2: Locking\n3: Motors\nq: quit\n")

    if choice == '1':
        testLED()
    elif choice == '2':
        testLocking()
    elif choice == '3':
        testPWM()
    elif choice == 'q':
        break
    else:
        print("incorrect input")
    
    
pwm1.stop()     # stop PWM1
pwm2.stop()     # stop PWM1

killAllLED()    # turn off LEDs

GPIO.cleanup()