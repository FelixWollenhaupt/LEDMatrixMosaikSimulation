# LEDMatrix

This project uses the mosaik co-simulation framework (see https://mosaik.offis.de/), developed by the brilliant developers at the high-ranked Offis institue for computer science, Oldenburg, Germany, to simulate multidimensional LED matrices.

A LED-matrix optimizes the used pins to controll LEDs. You can, for example, controll 250,000,000 LEDs by only using 53 Pins and a 20-dimensional LED-matrix, which is incredible! 

| ![space-1.jpg](https://www.jameco.com/Jameco/workshop/learning-center/electronic-fundamentals-working-with-led-dot-matrix-displays-fig3.jpg) | 
|:--:| 
| *This is an exmaple schematic for a two-dimensional LED-matrix.* |

Take a look at https://www.jameco.com/Jameco/workshop/learning-center/electronic-fundamentals-working-with-led-dot-matrix-displays.html to learn more about led-matrices

### SLEDs
A SLED is a super-LED. This type of LED does not have a regular anode and cathode.
This SLED uses any number of inputs and only glows, if all are set to True.
This is achievable by using transistors.

SLEDs are used in this project to simplify the simulation for higher dimensions. A 2d matrix can be easily simulated using regular LEDs, but with higher dimensions, it gets more complicated. 
