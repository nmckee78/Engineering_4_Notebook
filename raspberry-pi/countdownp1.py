import board
import time

while True:
     for x in range(10,-1,-1): # This tells it which number to start at(10), which number to stop at(-1, meaning the last number it'll display is 0 or liftoff) and the rate at which it'll count(-1 which tells it to count by 1 and the negative makes it count down)
        if x == 0: # This tells it what to do when it reaches 0
         print("Liftoff!") # The terminal will print liftoff instead of x like the other numbers
        else: # This tells it what to do when it's not at 0(10-1)
         print(x) # This will make it print whatever variable it's on
         time.sleep(1) # This will make the numbers print every second
