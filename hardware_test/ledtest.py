import RPi.GPIO as GPIO
import time

# pins 22, 24, 26; bcm: 25, 8, 7

LED_22 = 'SPI2_MISO'
LED_24 = 'SPI1_CS0'
LED_26 = 'SPI1_CS1'

def main():

	GPIO.setmode(GPIO.TEGRA_SOC)
	GPIO.setup(LED_22, GPIO.OUT, initial=GPIO.LOW)
	GPIO.setup(LED_24, GPIO.OUT, initial=GPIO.LOW)
	GPIO.setup(LED_26, GPIO.OUT, initial=GPIO.LOW)

	print("starting now")
	
	try:
		while 1:
			choice = input("which led?")
			print(choice)
			if choice == "1":
				print("turning on led 1")
				GPIO.output(LED_22, GPIO.HIGH)
				GPIO.output(LED_24, GPIO.LOW)
				GPIO.output(LED_26, GPIO.LOW)
			elif choice == "2":
				print("turning on led 2")
				GPIO.output(LED_24, GPIO.HIGH)
				GPIO.output(LED_22, GPIO.LOW)
				GPIO.output(LED_26, GPIO.LOW)
			elif choice == "3":
				print("turning on led 3")
				GPIO.output(LED_26, GPIO.HIGH)
				GPIO.output(LED_24, GPIO.LOW)
				GPIO.output(LED_22, GPIO.LOW)
			else:
				print("bye")
				GPIO.output(LED_22, GPIO.LOW)
				GPIO.output(LED_24, GPIO.LOW)
				GPIO.output(LED_26, GPIO.LOW)
				break
	finally:
		GPIO.cleanup()

main()
