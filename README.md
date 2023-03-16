# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [Launchpad Part 1](#launchpad_part_1)
* [Launchpad Part 2](#launchpad_part_2)
* [Launchpad Part 3](#launchpad_part_3)
* [Launchpad Part 4](#launchpad_part_4)
* [Crash Avoidance Part 1](#Crash_avoidance_part_1)
* [Crash Avoidance Part 2](#Crash_avoidance_part_2)
* [Crash Avoidance Part 3](#Crash_avoidance_part_3)
* [Landing Area Part 1](#Landing_area_part_1)
* [Landing Area Part 2](#Landing_area_part_2)
* [Morse Code Part 1](#Morse_code_part_1)
* [Morse Code Part 2](#Morse_code_part_2)
* [Beam Part 1](#Beam_part_1)
* [Beam Part 2](#Beam_part_2)
* [Ring](#Ring)
* [Key](#Key)
* [Assembley](#Assembley)

&nbsp;

## LaunchPad_Part_1

### Assignment Description

The purpose of this assignment is to create a countdown on a serial monitor starting at 10 to 0 or liftoff. 

### Evidence 

 ![Gif of the Countdown](https://github.com/jmuss07/Engineering_4_Notebook/blob/main/images/launchpadpt1.gif) 
 #### Credit to Josie for letting me use her video, mine was way too long 

### Wiring

No wiring for this assignment. 

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

The purpose of this assignment is to have an accelerometer that continously reports x, y, and z acceleration values on the serial monitor.  

### Evidence 

 ![Gif of the acceleration values](https://github.com/nmckee78/Engineering_4_Notebook/blob/main/images/crashavoidance1.gif) 
 
### Wiring

![Wiring for the accelerometer](https://github.com/nmckee78/Engineering_4_Notebook/blob/main/images/wiringcrashavoidance1.jpg)

### Code

[Code for the accelerometer](https://github.com/nmckee78/Engineering_4_Notebook/blob/main/raspberry-pi/crashavoidance1). 

### Reflection

The wiring for this was really easy as it's just a ground pin, a vin pin and then the sda and sdl pins. I struggled a lot more with the code and trying to figure out how to use the accelerometer with f strings. Even though the actual code is really only a few lines I had to figure out how to properly define the f string so it would display correctly in the terminal while still running the accelerometer code inside the f string. Once I figured out that you can just define what your gonna display and then put the code for the accelerometer to find the x, y, and z values inside that. This was really the only issue as the code and wiring is relatively short and simple.

&nbsp;

## Crash_avoidance_part_2

### Assignment Description

The purpose of this assignment is to have an led turn on when the accelerometer is turned more than 90 degrees. 

### Evidence 

 ![Gif of the acceleration values](https://github.com/nmckee78/Engineering_4_Notebook/blob/main/images/crashavoidance2.gif) 

### Wiring

![Wiring for the accelerometer](https://github.com/nmckee78/Engineering_4_Notebook/blob/main/images/wiringcrashavoidance2.jpg)

### Code
[Code for the accelerometer](https://github.com/nmckee78/Engineering_4_Notebook/blob/main/raspberry-pi/crashavoidance2). 

### Reflection

The only new wiring that was needed for this assignment was just wiring a single led. To make the led turn on when the accelerometer is tilted more than 90 degrees you need to tell the code to turn the light on when the x value or y value is over 9 or under -9 as these are the values that represent about 90 degrees. The code for this is relatively straight forward as you just establish an if, elif and else statement where the if and elif are for the x and y values over 9, telling the led value to become true and the else function turning the light off which it'll be whenever it isn't over or under those values. Overall once you figure out how to properly set up the if, elif and else function pretty straightforward.

&nbsp;

## Crash_avoidance_part_3

### Assignment Description

The purpose of this assignment is to have an OLED screen print the accelerometer values instead of the terminal on the computer as well as the accelerometer being mobile and not attached to the computer.

### Evidence 

 ![Gif of the acceleration values](https://github.com/nmckee78/Engineering_4_Notebook/blob/main/images/crashavoidance3.gif) 

### Wiring

![Wiring for the accelerometer](https://github.com/nmckee78/Engineering_4_Notebook/blob/main/images/wiringcrashavoidance3.jpg)

### Code
[Code for the accelerometer](https://github.com/nmckee78/Engineering_4_Notebook/blob/main/raspberry-pi/crashavoidance3). 

### Reflection

The only new wiring that was needed for this assignment was just wiring a single led. To make the led turn on when the accelerometer is tilted more than 90 degrees you need to tell the code to turn the light on when the x value or y value is over 9 or under -9 as these are the values that represent about 90 degrees. The code for this is relatively straight forward as you just establish an if, elif and else statement where the if and elif are for the x and y values over 9, telling the led value to become true and the else function turning the light off which it'll be whenever it isn't over or under those values. Overall once you figure out how to properly set up the if, elif and else function pretty straightforward.

&nbsp;

## Landing_area_part_1

### Assignment Description

Provide three coordinates and calculate the area of said coordinates.

### Evidence 

 ![Gif of it in action](https://github.com/nmckee78/Engineering_4_Notebook/blob/main/images/landingarea1.gif) 

### Wiring

There's no wiring for this assingment

### Code
[Code for the Landing Area](https://github.com/nmckee78/Engineering_4_Notebook/blob/main/raspberry-pi/Landingarea1). 

### Reflection

This assingment was a lot more difficult as you had to really understand f strings and had to get the floats and inputs to work. The function, which is how the area is found from the inputs was definitely the harder part as you had to get because you need to define the floats which turn the values from string to actual numbers and then you have to define the area as the area of a triangle and then make the f string for the terminal. The second part which is for the inputs was easier as it's really just plugging in the values you defined in the first part and creating f strings for them and also you have to apply splits so you split a value like x1y1 into x1, y1 or else they won't get seperated and won't be inputted properly.

&nbsp;

## Landing_area_part_2

### Assignment Description

An OLED screen must plot the triangle and display it's area.

### Evidence 

 ![Gif of the assignment](https://github.com/nmckee78/Engineering_4_Notebook/blob/main/images/landingarea2.gif) 

### Wiring

![Wiring for the assignment](https://github.com/nmckee78/Engineering_4_Notebook/blob/main/images/wiringlandingarea2.png)

### Code
[Code for the assignment](https://github.com/nmckee78/Engineering_4_Notebook/blob/main/raspberry-pi/Landingarea2). 

### Reflection

This part of the assignment was fairly easy for me as you basically just have to import the OLED code you did in the crash avoidance assignment and plug it in to your code. The only new part was the H-line, V-line and defining the triangle, which was a little tricky to figure out but basically just uses the same system as how you would display words. Other than that you just have to apply the same logic you used in crash avoidance to put the OLED code in the proper spots and you should be fine.

&nbsp;

## Morse_code_part_1

### Assignment Description

Your able to input a word or phrase into the code and it'll return the same word or phrase in morse code.

### Evidence 

 ![Gif of the assignment](https://github.com/nmckee78/Engineering_4_Notebook/blob/main/images/morsecode1.gif) 

### Wiring

There's no wiring for this assignment.

### Code
[Code for the assignment](https://github.com/nmckee78/Engineering_4_Notebook/blob/main/raspberry-pi/morsecode1). 

### Reflection

This assignment was relatively simple because the code is very short and simple. You have to import the morse code library and then all you really have to do is create a string and ask for an input of the phrase your going to use. For the actual translation process you just need a few lines of code which just translate each letter into the morse code equivalent then a line to add it to the string and then a final one to add a space in the string.
&nbsp;

## Morse_code_part_2

### Assignment Description

A led must flash the phrase in morse code. 

### Evidence 

 ![Gif of the assignment](https://github.com/nmckee78/Engineering_4_Notebook/blob/main/images/morsecode2.gif) 

### Wiring

![Wiring for the assignment](https://github.com/nmckee78/Engineering_4_Notebook/blob/main/images/morsecodewiring2.jpg)

### Code
[Code for the assignment](https://github.com/nmckee78/Engineering_4_Notebook/blob/main/raspberry-pi/morsecode2). 

### Reflection

This assignment was more complicated than the first but it still is a relatively small and simple amount of code. You have to import a bunch of modifiers to help you define the time sleeps inbetween the blinks on the led. In the actual code, you just have to define how long the time sleeps are for each different type of morse code, which should be pretty simple as you already have the modifiers for all of them. 
&nbsp;

## Beam_part_1

### Assignment Description

Make a beam and see how much weight it can support before it bends beyond a certain point or snaps.

### Part Link 

[link to the beam in onshape](https://cvilleschools.onshape.com/documents/33575ab88dc8f7928befb042/w/38921909f117f23a72e1cbeb/e/b1f9443dbe8499829a3eab5c?renderMode=0&uiState=6373dab89a584e328ce74f06). 

### Part Image

![Picture of the Beam](https://github.com/nmckee78/Engineering_4_Notebook/blob/main/images/Beam%20screenshot.PNG) 

### Reflection

We decided on making a modified I beam with a large supporting bottom beam and small, thick tab on the top. We cut out a lot of holes in the bottom support and circles throughout the beam to take weight off so we had more material to work with. We figured that we should make the part around the hole where the weight is supported flat to better support it and not bend the beam one way or another.

&nbsp;

## Beam_part_2

### Assignment Description

Run the beam through a simulator to see where the weak points are.

### Part Link 

[link to the beam in onshape](https://cvilleschools.onshape.com/documents/33575ab88dc8f7928befb042/w/38921909f117f23a72e1cbeb/e/b1f9443dbe8499829a3eab5c?renderMode=0&uiState=6373dab89a584e328ce74f06). 

### Part Image

![Picture of the Beam](https://github.com/nmckee78/Engineering_4_Notebook/blob/main/images/Beam%20screenshot.PNG) 

### Reflection

The main weak points of the beam were right where it connected to the supporting block, where the support piece on the top ended and near the hole. For the two points on the top of the beam we just cut out more material from the middle and just made the support piece longer and thicker as well as removing some 90 degree edges which were showing up as weak points. For the part near the hole, we made a large slanted support piece coming down from the top of the beam to the flat part near the hole, which solved the problem.

&nbsp;

## Ring

### Assignment Description

Creating a ring part in onshape for the launcher.

### Part Link 

[link to the ring in onshape](https://cvilleschools.onshape.com/documents/de7d1d57a5f209eeb9e1978b/w/286061655ed2639764cdf17a/e/da8a509dd8d0fb351f70a402?renderMode=0&uiState=637528cd5620230f9d075cd1). 

### Part Image

![Picture of the Beam](https://github.com/nmckee78/Engineering_4_Notebook/blob/main/images/Ring.PNG) 

### Reflection

This part was really easy to start as you just extrude lines you used from the base to create the base of the ring. You then make a circle on the front plane then extrude it so it intersects with the base of the ring. Then you just make some fillets and a small, chamfered cricle on the other side of the ring base to finish. Overall the part was very simple and straightforward to make.

&nbsp;

## Key

### Assignment Description

Create a key that goes through the top for the launcher.

### Part Link 

[link to the key in onshape](https://cvilleschools.onshape.com/documents/de7d1d57a5f209eeb9e1978b/w/286061655ed2639764cdf17a/e/da8a509dd8d0fb351f70a402?renderMode=0&uiState=63752b255620230f9d077a90). 

### Part Image

![Picture of the Beam](https://github.com/nmckee78/Engineering_4_Notebook/blob/main/images/Key.PNG) 

### Reflection

All this part was is a loop and then a teethed key that attaches to the loop. To create the loop and the non toothed part of the key you just created a new part of a circle and a line jutting out from it then extruded. After this, you just added a linear pattern to quickly add the teeth as well as some chamfers to refine it. Overall it was relatively straightforward assingment to do.

&nbsp;

## Assembley

### Assignment Description

Assemble the pull copter

### Part Link 

[link to the assembley in onshape](https://cvilleschools.onshape.com/documents/de7d1d57a5f209eeb9e1978b/w/286061655ed2639764cdf17a/e/63be528840458eccd6262046?renderMode=0&uiState=64135997e7c97716dfdd33ab). 

### Part Image

![Picture of the Assembley](https://github.com/nmckee78/Engineering_4_Notebook/blob/main/images/Assembley.PNG) 

### Reflection

This assembley wasn't that hard as we just had to follow the instructions and it was farily straightforward. It was pretty cool to see how it worked in real time and the animation was really cool. The only difficult part was using the section view to edit it so it could make it work.

&nbsp;

## Media Test

Your readme will have various images and gifs on it. Upload a test image and test gif to make sure you've got the process figured out. Pick whatever image and gif you want!

### Test Link
[Link emaple](https://www.google.com/search?q=arthur+gif&tbm=isch&ved=2ahUKEwi0vOGJj_T5AhWNYDUKHWk6CogQ2-cCegQIABAA&oq=arthur+gif&gs_lcp=CgNpbWcQAzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgAELEDEEM6CggAELEDEIMBEEM6CwgAEIAEELEDEIMBOggIABCABBCxAzoICAAQsQMQgwE6BAgAEENQnAVY3g1g6hFoAHAAeACAASyIAcEBkgEBNZgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=v-sQY_TgFI3B1QHp9KjACA&bih=969&biw=1920&rlz=1C1GCEU_enUS1020US1020#imgrc=9REL6WGEGSGHXM)
### Test Image
![Arthur](https://github.com/nmckee78/Engineering_4_Notebook/blob/main/images/Arthur.png)  
### Test GIF
![Picture Name Here](https://github.com/nmckee78/Engineering_4_Notebook/blob/main/images/arthur-dancing.gif) 
