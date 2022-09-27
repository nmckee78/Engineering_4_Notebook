# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [Launchpad Part 1](#launchpad_part_1)
* [Onshape_Assignment_Template](#onshape_assignment_template)
* [Launchpad Part 2](#launchpad_part_2)
* [Launchpad Part 3](#launchpad_part_3)
* [Launchpad Part 4](#launchpad_part_4)
* [Crash Avoidance Part 1](#Crash_avoidance_part_1)

&nbsp;

## LaunchPad_Part_1

### Assignment Description

The purpose of this assignment is to create a countdown on a serial monitor starting at 10 to 0 or liftoff. 

### Evidence 

 ![Gif of the Countdown](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/images/launchpadpt1.gif) 
 #### Credit to Josie for letting me use her video, mine was way too long 

### Wiring

This may not be applicable to all assignments. Anything where you wire something up, include the wiring diagram here. The diagram should be clear enough that I can recreate the wiring from scratch. 

### Code
[Code for the countdown](https://github.com/millerm22/Engineering_4_Notebook/blob/main/Raspberry_Pi/hello_world.py). 

### Reflection

The only thing I really found challenging was figuring out x in range part, specifically figuring out that the end variable needs to be at -1 and not 0 because while the countdown stops at 0 for whatever reason the command will stop at the next number(-1) even though 0 will be the last number it prints I figured this out by simple trial and error. The only other thing that was slightly difficult was the fact that the value for when x reaches 0 and you need to print liftoff you have to write x==0 instead of just one = for some reason and I assume this is the same for all values like it using x and a number. This was the first code assignment I did this year so I was a little rusty but this was a pretty simple assignment that could basically just be figured out using logic.

&nbsp;

## LaunchPad_Part_2

### Assignment Description

The purpose of this assignment is to blink a red light every second as the countdown goes down then blink a green light when it reaches 0.

### Evidence 

 ![Gif of the Countdown & Lights](https://github.com/nmckee78/Engineering_4_Notebook/blob/main/images/countdownp2.gif) 

### Wiring

![Wiring for the lights](https://github.com/nmckee78/Engineering_4_Notebook/blob/main/images/wiringcountdownp2.jpg)

### Code
[Code for the countdown & lights](https://github.com/nmckee78/Engineering_4_Notebook/blob/main/raspberry-pi/countdown2.py). 

### Reflection

This part was fairly simple as it was really just making lights blink corresponding to the numbers they should blink on. So you could just insert the code for making the lights blink into your existing code with out having to change the overall structure of the code at all. The only issues I had was with getting the wiring to work and making sure everything was in the pins I had defined in the code.

&nbsp;

## LaunchPad_Part_3

### Assignment Description

The purpose of this assignment is to have a button that when pressed, will start the countdown

### Evidence 

 ![Gif of the Countdown with button](https://github.com/nmckee78/Engineering_4_Notebook/blob/main/images/countdownp3.gif) 

### Wiring

![Wiring for the lights & button](https://github.com/nmckee78/Engineering_4_Notebook/blob/main/images/wiringcountdownp3.jpg)

### Code
[Code for the countdown with button](https://github.com/nmckee78/Engineering_4_Notebook/blob/main/raspberry-pi/countdown3). 

### Reflection

This part was pretty quick as the only things you had to add to the code was the if button.value == false and defining the button with the right pin. The only thing that was really confusing was that you need the button value to be false for it to work, not true. This is because the button pull is up and not down because it means that when the button is not pressed(pulled up) the value equals true and when the button is pressed(pulled down) the value equals false, which is what we want. The wiring was also very simple with just wire going from the button to ground and the other going to whatever you pin you pair the button with in the code. 

&nbsp;

## LaunchPad_Part_4

### Assignment Description

The purpose of this assignment is to add a servo that will spin 180 degrees on liftoff.

### Evidence 

 ![Gif of the Countdown with servo](https://github.com/nmckee78/Engineering_4_Notebook/blob/main/images/countdownp4.gif) 

### Wiring

![Wiring for the lights, button and servo](https://github.com/nmckee78/Engineering_4_Notebook/blob/main/images/wiringcountdownp4.jpg)

### Code
[Code for the countdown with button](https://github.com/nmckee78/Engineering_4_Notebook/edit/main/raspberry-pi/countdown.py). 

### Reflection

This part was pretty easy as all you have to do is import the libraries and the servo code, then tell it to spin 180 degrees when it reaches 0. The only problems I had was for some reason it wouldn't work unless I told it to spin 0 degrees under the else function. I'm pretty sure this would reset the servo and without the reset it wouldn't work. Also, I had a little trouble finding the right wiring but once I found it, it's pretty simple.

&nbsp;

## Crash_avoidance_part_1

### Assignment Description

The purpose of this assignment is to have an acceleromater that continously reports x, y, and z acceleration values on the serial monitor.  

### Evidence 

 ![Gif of the acceleration values](https://github.com/nmckee78/Engineering_4_Notebook/blob/main/images/crashavoidance1.gif) 

### Wiring

![Wiring for the accelerometer](https://github.com/nmckee78/Engineering_4_Notebook/blob/main/images/wiringcrashavoidance1.jpg)

### Code
[Code for the accelerometer](https://github.com/nmckee78/Engineering_4_Notebook/blob/main/raspberry-pi/crashavoidance1). 

### Reflection

The wiring for this was really easy as it's just a ground pin, a vin pin and then the sda and sdl pins. I struggled a lot more with the code and trying to figure out how to use the accelerometer with f strings. Even though the actual code is really only a few lines I had to figure out how to properly define the f string so it would display correctly in the terminal while still running the accelerometer code inside the f string. Once I figured out that you can just define what your gonna display and then put the code for the accelerometer to find the x, y, and z values inside that. This was really the only issue as the code and wiring is relatively short and simple.

## Onshape_Assignment_Template

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Part Link 

[Create a link to your Onshape document](https://cvilleschools.onshape.com/documents/003e413cee57f7ccccaa15c2/w/ea71050bb283bf3bf088c96c/e/c85ae532263d3b551e1795d0?renderMode=0&uiState=62d9b9d7883c4f335ec42021). Don't forget to turn on link sharing in your Onshape document so that others can see it. 

### Part Image

Take a nice screenshot of your Onshape document. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;

## Media Test

Your readme will have various images and gifs on it. Upload a test image and test gif to make sure you've got the process figured out. Pick whatever image and gif you want!

### Test Link
[Link emaple](https://www.google.com/search?q=arthur+gif&tbm=isch&ved=2ahUKEwi0vOGJj_T5AhWNYDUKHWk6CogQ2-cCegQIABAA&oq=arthur+gif&gs_lcp=CgNpbWcQAzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgAELEDEEM6CggAELEDEIMBEEM6CwgAEIAEELEDEIMBOggIABCABBCxAzoICAAQsQMQgwE6BAgAEENQnAVY3g1g6hFoAHAAeACAASyIAcEBkgEBNZgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=v-sQY_TgFI3B1QHp9KjACA&bih=969&biw=1920&rlz=1C1GCEU_enUS1020US1020#imgrc=9REL6WGEGSGHXM)
### Test Image
![Arthur](https://github.com/nmckee78/Engineering_4_Notebook/blob/main/images/Arthur.png)  
### Test GIF
![Picture Name Here](https://github.com/nmckee78/Engineering_4_Notebook/blob/main/images/arthur-dancing.gif) 
