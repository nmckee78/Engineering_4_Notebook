import board
import pwmio
from adafruit_motor import servo
import time
import digitalio

led1 = digitalio.DigitalInOut(board.GP13)
led2 = digitalio.DigitalInOut(board.GP18)
led1.direction = digitalio.Direction.OUTPUT
led2.direction = digitalio.Direction.OUTPUT
button = digitalio.DigitalInOut(board.GP22)
button.pull = digitalio.Pull.UP

while True:
    if button.value == False: # When the button is pressed, this starts the countdown
     for x in range(10,-1,-1):# This tells it which number to start at(10), which number to stop at(-1, meaning the last number it'll display is 0 or liftoff) and the rate at which it'll count(-1 which tells it to count by 1 and the negative makes it count down)
        if x == 0: # This tells it what to do when it reaches 0
         print("Liftoff!") # The terminal will print liftoff instead of x like the other numbers
         led1.value = True # This turns the Green light on(led1)
         time.sleep(1) 
        else: 
         led1.value = False # This tells the green light to be off
         print(x) # This will make it print whatever variable it's on
         time.sleep(1) # This will make the numbers print every second
         led2.value = True # This turns the red light on
         time.sleep(1) 
         led2.value = False #This turns it off, making it blink
         time.sleep(1)