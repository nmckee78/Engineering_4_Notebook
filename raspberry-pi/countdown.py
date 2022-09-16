import pwmio
from adafruit_motor import servo
import board
import time
import digitalio

led1 = digitalio.DigitalInOut(board.GP13)
led2 = digitalio.DigitalInOut(board.GP18)
led1.direction = digitalio.Direction.OUTPUT
led2.direction = digitalio.Direction.OUTPUT
button = digitalio.DigitalInOut(board.GP22)
button.pull = digitalio.Pull.UP
pwm_servo = pwmio.PWMOut(board.GP6, duty_cycle=2 ** 15, frequency=50)
servo1 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500)

while True:
    if button.value == False:
     for x in range(10,-1,-1):
        if x == 0:
         print("Liftoff!")
         led1.value = True
         time.sleep(1)
         servo1.angle = 180
        else: 
         servo1.angle = 0
         led1.value = False
         print(x)
         time.sleep(1)
         led2.value = True
         time.sleep(1)
         led2.value = False
         time.sleep(1)