import RPi.GPIO as GPIO
from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16)

SERV_1 = 0
SERV_2 = 1
SERV_3 = 2

BUT_1 = 'UART2_CTS' # 36
BUT_2 = 'DAP4_DIN'  # 38
BUT_3 = 'DAP4_DOUT' # 40

LED_1 = 'SPI2_MISO'    # 22
LED_2 = 'SPI1_CS0'     # 24
LED_3 = 'SPI1_CS1'      # 26

def button1(channel):
    print("button1")
    print("turning on led 1")
    
    kit.servo[SERV_1].angle = 0 
    
    GPIO.output(LED_1, GPIO.HIGH)
    # GPIO.output(LED_2, GPIO.LOW)
    # GPIO.output(LED_3, GPIO.LOW)

    # time.sleep(2)

    # kit.servo[SERV_1].angle = 180

def button2(channel):
    print("button2")
    print("turning on led 2")

    kit.servo[SERV_2].angle = 0

    # GPIO.output(LED_1, GPIO.LOW)
    GPIO.output(LED_2, GPIO.HIGH)
    # GPIO.output(LED_3, GPIO.LOW)

    # time.sleep(2)

    # kit.servo[SERV_2].angle = 180
    
def button3(channel):
    print("button3")
    print("turning on led 3")

    kit.servo[SERV_3].angle = 0

    # GPIO.output(LED_1, GPIO.LOW)
    # GPIO.output(LED_2, GPIO.LOW)
    GPIO.output(LED_3, GPIO.HIGH)
    
    # time.sleep(2)

    # kit.servo[SERV_3].angle = 180

def killAll():
    kit.servo[SERV_1].angle = 180
    kit.servo[SERV_2].angle = 180
    kit.servo[SERV_3].angle = 180

    GPIO.output(LED_1, GPIO.LOW)
    GPIO.output(LED_2, GPIO.LOW)
    GPIO.output(LED_3, GPIO.LOW)


GPIO.setmode(GPIO.TEGRA_SOC)

GPIO.setup(BUT_1, GPIO.IN)
GPIO.setup(BUT_2, GPIO.IN)
GPIO.setup(BUT_3, GPIO.IN)
GPIO.setup(LED_1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED_2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED_3, GPIO.OUT, initial=GPIO.LOW)

killAll()

GPIO.add_event_detect(BUT_1, GPIO.RISING, callback=button1, bouncetime=10)
GPIO.add_event_detect(BUT_2, GPIO.RISING, callback=button2, bouncetime=10)
GPIO.add_event_detect(BUT_3, GPIO.RISING, callback=button3, bouncetime=10)

message=input("Press enter to stop")

killAll()

GPIO.cleanup()