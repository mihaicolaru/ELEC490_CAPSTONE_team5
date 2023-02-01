import RPi.GPIO as GPIO
from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16)

SERV_1 = 0
SERV_2 = 1
SERV_3 = 2

GPIO.setmode(GPIO.TEGRA_SOC)

# while 1:
#     kit.servo[SERV_1].angle = 180
#     time.sleep(2)
#     kit.servo[SERV_1].angle = 0
#     time.sleep(2)

kit.servo[SERV_3].angle = 180

input('press enter')

kit.servo[SERV_3].angle = 0

GPIO.cleanup()