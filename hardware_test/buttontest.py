import RPi.GPIO as GPIO

BUT_1 = 'UART2_CTS' # 36
BUT_2 = 'DAP4_DIN'  # 38
BUT_3 = 'DAP4_DOUT' # 40

def button1(channel):
    print("button1")

GPIO.setmode(GPIO.TEGRA_SOC)
GPIO.setup(BUT_1, GPIO.IN)

GPIO.add_event_detect(BUT_1, GPIO.FALLING, callback=button1, bouncetime=10)

message=input("Press enter to stop")
GPIO.cleanup()