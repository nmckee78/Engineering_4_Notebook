
import board
import time
import digitalio

led1 = digitalio.DigitalInOut(board.GP13)
led2 = digitalio.DigitalInOut(board.GP18)
led1.direction = digitalio.Direction.OUTPUT
led2.direction = digitalio.Direction.OUTPUT
button = digitalio.DigitalInOut(board.GP22)
button.pull = digitalio.Pull.UP

while True:
    if button.value == False:
     for x in range(10,-1,-1):
        if x == 0:
         print("Liftoff!")
         led1.value = True
         time.sleep(1)
        else: 
         print(x)
         time.sleep(1)
         led2.value = True
         time.sleep(1)
         led2.value = False
         time.sleep(1)