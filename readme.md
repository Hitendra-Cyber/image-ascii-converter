## Image to ASCII Converter
This project basically takes as input an image and generate an ASCII art for it. ASCII art is a picture that is made completely out of text. It gives a retro feel to an image.It can contain letters, symbols, numbers, everything present on keyboard. So the tool converts an image that has pixels with different brightness or pixel values and convert it into an ASCII art. It is a basic tool that i made to evaluate my progress in python that I've been learning on boot.dev.

Except making a repo and initializing it there are main things we need to do. For this project I'm only gonna use core programming and no external libraries or less external libs.
## Step 1 
- complete ( making project structure and initializing a repo)
## Step 2 
- For this we have to understand a character ramp and design it first. 
- What is a char ramp? It is a list of characters that represent range of pixel levels. Like in image we have range of pixel from 0 to 255. But in ASCII we only have characters and so we need to make a list of what characters represent what. For that we generate a character ramp.
- For our case i used the bare minimum:
[@%#*+=-:. ]
Here @ is dark value and space at end it brightest value
## Step 3
- So far we got a character ramp now we need to map those characters to brightness level 
- we did like this: we took intervals of 9 so starting was 0 to 28 which corresponds to ' ' we could've taken 10 but 9 is working fine might change it in future.
## Step 4
- Now we have to convert a row of pixels into row of character as the image contains multiple rows of pixels not just a single value
- For that 