# Application to Convert From PNG to Gcode
This application creates an easy way to convert from a png image to gcode that can then be used on a pen plotter. When the application is run a screen will pop that will allow the user to choose an image to convert and then the size and pen up and down commands for the generated Gcode. Once exported to the directory a generated version of the image as Gcode will be availble.
<img width="632" alt="Screenshot 2024-07-09 at 11 48 04 PM" src="https://github.com/OwenTheGreenBean/Pen_Plotter/assets/148368718/94cab25a-cb8b-49f4-a18a-9800a00327b1">

Default application:

<img width="632" alt="Screenshot 2024-07-09 at 11 53 50 PM" src="https://github.com/OwenTheGreenBean/Pen_Plotter/assets/148368718/5ed0b1ce-ec05-46df-bfd6-f85f1c62edfc">

With loaded image

## Requirments:
Python3 or higher, with Python TKinter should come installed. Using pip running '''pip install opencv-python numpy''' will install the nessacary librarys for the application to function.

## What is does

Once loading in an image the **Height** will determite the height of the gcode generated and the **Width** will do the same. For my example I am using a servo for my pen movement and declared the Gcode instructions for moving the pen up and down in the the **Pen Up Command** and the **Pen Down Command** After pressing save you will then beable to press the Save G-code button where the conversion proccess will take place after selecting a file path. The first proccess will have a gray scale image created of the current image:

![grayscale_image](https://github.com/OwenTheGreenBean/Pen_Plotter/assets/148368718/ed882962-09e7-4cf5-adca-c995a9ddea57)

Then the image will be resized to the desired dimensions where it can then have its edges detected and turned into Gcode paths when the gcode file can then be written.

<img width="1034" alt="Screenshot 2024-07-10 at 12 01 58 AM" src="https://github.com/OwenTheGreenBean/Pen_Plotter/assets/148368718/b1f2711f-9d6d-428f-a3d0-986d1913ce31">
The image is flipped and mirrored because I am using Universal Gcode Sender for communicating with my pen plotter and this is what seems to make to happy. To avoid this flipping and mirroring the image before importing to the application is necessary.

## STL files

Theses files can be used print a model of the pen plotter and be used. I used PLA for printing on my ELLEGO neptune 3 pro. For other materials I used M3 nuts and bolts, along with some paracord, some flag rod from home depot and a pen.


