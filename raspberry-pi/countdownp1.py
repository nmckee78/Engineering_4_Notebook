import board
import time

while True:
     for x in range(10,-1,-1):
        if x == 0:
         print("Liftoff!")
         time.sleep(1)
        else: 
         print(x)
         time.sleep(1)
