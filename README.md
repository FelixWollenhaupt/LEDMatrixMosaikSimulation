# LEDMatrix

This project uses the mosaik co-simulation framework (https://mosaik.offis.de/) to simulate multidimensional led matrices.Cancel changes

A led-matrix optimizes the used pins to controll leds. You can, for example, controll 250,000,000 leds by only using 53 Pins and a 20-dimensional led-matrix, which is incredible! 

| ![space-1.jpg](https://www.jameco.com/Jameco/workshop/learning-center/electronic-fundamentals-working-with-led-dot-matrix-displays-fig3.jpg) | 
|:--:| 
| *This is an exmaple schematic for a two-dimensional led-matrix.* |

Take a look at https://www.jameco.com/Jameco/workshop/learning-center/electronic-fundamentals-working-with-led-dot-matrix-displays.html to learn more about led-matrices

### SLEDs
A SLED is a super-led. This type of led does not have a regular anode and cathode.
This SLED uses any number of inputs and only glows, if all are set to True.
This is achievable by using transistors.

SLEDs are used in this project to simplify the simulation for higher dimensions. A 2d matrix can be easily simulated using regular leds, but with higher dimensions, it gets more complicated. 
