import RPi.GPIO as GPIO
from adafruit_servokit import ServoKit
import time

# ===================== hardware =====================

kit = ServoKit(channels=16)

SERV_1 = 0
SERV_2 = 1
SERV_3 = 2

BUT_1 = 'UART2_CTS'     # 36
BUT_2 = 'DAP4_DIN'      # 38
BUT_3 = 'DAP4_DOUT'     # 40

LED_1 = 'SPI_2_MISO'     # 22
LED_2 = 'SPI1_CS0'      # 24
LED_3 = 'SPI1_CS1'      # 26

MOT_1 = 'LCD_BL_PW'     # 32
MOT_2 = 'GPIO_PE6'      # 33


# ===================== methods =====================

def testLED():
    while 1:
        compartment = input("test LED (1, 2 or 3, q to quit)")

        if compartment == '1':
            GPIO.output(LED_1, GPIO.HIGH)
            GPIO.output(LED_2, GPIO.LOW)
            GPIO.output(LED_3, GPIO.LOW)
        elif compartment == '2':
            GPIO.output(LED_1, GPIO.LOW)
            GPIO.output(LED_2, GPIO.HIGH)
            GPIO.output(LED_3, GPIO.LOW)
        elif compartment == '3':
            GPIO.output(LED_1, GPIO.LOW)
            GPIO.output(LED_2, GPIO.LOW)
            GPIO.output(LED_3, GPIO.HIGH)
        elif compartment == 'q':
            GPIO.output(LED_1, GPIO.LOW)
            GPIO.output(LED_2, GPIO.LOW)
            GPIO.output(LED_3, GPIO.LOW)
            break
        else:
            print("invalid compartment")


def testLocking():
    while 1:
        compartment = input("test Locking (1, 2 or 3, q to quit)")

        if compartment == '1':
            print("locking compartment 1")

            kit.servo[SERV_1].angle = 0

            time.sleep(2)

            print("unlocking compartment 1")

            # kit.servo[SERV_1].angle = 180
                
        elif compartment == '2':
            print("locking compartment 1")

            kit.servo[SERV_2].angle = 0

            time.sleep(2)

            # print("unlocking compartment 1")

            # kit.servo[SERV_2].angle = 180
            
        elif compartment == '3':
            print("locking compartment 1")

            kit.servo[SERV_3].angle = 0

            time.sleep(2)

            # print("unlocking compartment 1")

            # kit.servo[SERV_3].angle = 180

        elif compartment == 'u':
            print("unlocking all")
            killAll()    
        elif compartment == 'q':
            break
        else:
            print("invalid compartment")

def testPWM():
    dc=0                               # set dc variable to 0 for 0%
    pwm1.start(dc)                      # Start PWM with 0% duty cycle
    pwm2.start(dc)                      # Start PWM with 0% duty cycle
    for dc in range(0, 100, 10):    # Loop 0 to 100 stepping dc by 5 each loop
      pwm1.ChangeDutyCycle(dc)
      pwm2.ChangeDutyCycle(dc)
      time.sleep(2)
      print(f'sending {dc} to motors 1 and 2')


def button1(channel):
    print("button 1 pressed")
    
    # GPIO.output(LED_1, GPIO.LOW)

    # time.sleep(1)

    # print("unlocking")

    # kit.servo[SERV_1].angle = 0

def button2(channel):
    print("button 2 pressed")
    # print("compartment 2 is closed")
    # print("locking")

    # kit.servo[SERV_2].angle = 180
    
    # GPIO.output(LED_2, GPIO.LOW)

    # time.sleep(1)

    # print("unlocking")
    
    # kit.servo[SERV_2].angle = 0
    
def button3(channel):
    print("button 3 pressed")
    # print("compartment 3 is closed")
    # print("locking")

    # kit.servo[SERV_3].angle = 180
    
    # GPIO.output(LED_3, GPIO.LOW)

    # time.sleep(1)

    # print("unlocking")
    
    # kit.servo[SERV_3].angle = 0

def killAll():
    kit.servo[SERV_1].angle = 180
    kit.servo[SERV_2].angle = 180
    kit.servo[SERV_3].angle = 180

    GPIO.output(LED_1, GPIO.LOW)
    GPIO.output(LED_2, GPIO.LOW)
    GPIO.output(LED_3, GPIO.LOW)


# ===================== setup =====================

GPIO.setmode(GPIO.TEGRA_SOC)

GPIO.setup(BUT_1, GPIO.IN)
GPIO.setup(BUT_2, GPIO.IN)
GPIO.setup(BUT_3, GPIO.IN)

GPIO.setup(LED_1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED_2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED_3, GPIO.OUT, initial=GPIO.LOW)

GPIO.setup(MOT_1, GPIO.OUT)
GPIO.setup(MOT_2, GPIO.OUT)

pwm1 = GPIO.PWM(MOT_1, 50)   # Initialize PWM on pwmPin 50Hz frequency
pwm2 = GPIO.PWM(MOT_2, 50)   # Initialize PWM on pwmPin 50Hz frequency


GPIO.add_event_detect(BUT_1, GPIO.RISING, callback=button1, bouncetime=1)
GPIO.add_event_detect(BUT_2, GPIO.RISING, callback=button2, bouncetime=1)
GPIO.add_event_detect(BUT_3, GPIO.RISING, callback=button3, bouncetime=1)


killAll()

# ===================== main =====================

print("q to quit")

while 1:
    print("which component would you like to test?")
    choice = input("1: LEDS\n2: Locking\n3: Motors\n")

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
    
    
pwm1.stop()                         # stop PWM1
pwm2.stop()                         # stop PWM1
killAll()
GPIO.cleanup()