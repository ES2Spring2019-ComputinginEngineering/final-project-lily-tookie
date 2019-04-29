# This is your Final Project ReadMe Template

The file is inside your final project repository called "README.md"

You should include in your final project readme a description of the project, a list of all the files that you have created and instructions for use.

This readme is written in a language called markdown. This is not a programming language but a formatting langauge. There are symbols (syntax) used to indicate how to format the text. For example the pound symbol (i.e. the hashtag) is used to format a title; two of the same symbol format a heading, and three format a sub-heading.

Below is some example text in markdown however this alone is not suffiecent for the final project. **Make sure you follow the directions on Canvas.**

Delete the instructions above this line and the line:

---------------------------------------------

# Project Title

Short project description here, click the **EDIT (pencil) button** in the top right corner of this frame to copy the markdown formatted template.

## Instructions

Describe how the users(instructors) should run your code to see an ***easy to run example of the functionality***. This should all be in a *main.py* "driver" script.

## File List

Create a list of all of the files in your repository with one sentence descriptions 

## How to format your readme

In your readme, you can:
```
Give code examples
```

You can also include useful links, like this one with information about [formatting markdown](https://help.github.com/en/articles/basic-writing-and-formatting-syntax)

You can 
- Also
- Make
- Lists



Morse Code with Micro:bits!
Through micro:bit user interface, Morse Code with Micro:bits demonstrates translation to an encoded scheme denoted by signal durations of dots and dashes. The code converts the message from English to morse code and displays how the user can transmit the message one micro:bit to another. Mu editor transmits morse code message between 2 micro:bits.
Instructions
Open Final Project.py in python and input a message.
Message will be displayed in morse code and in “As” and “Bs” required to transmit via micro:bit.
Open Transmitter.Project.Final.py and Receiver.Project.py in Mu editor.
Connect the microbits to the computer with the USB port.
Flash Transmitter.Project.Final.py onto 1st micro:bit, flash Receiver.Project.py onto 2nd micro:bit.
Type message in sequence of “As” and “Bs” from Final Project.py which correspond to “button a” and “button b” on the micro:bit. Signal the end of each letter by pressing “button a” and “button b” simultaneously.
Watch 2nd microbit receive letters as dots and dashes and translate each to the equivalent English letter and Arabic numeral.
File List 
Final Project.py
-Prompts user to input a decoded message.
-For each letter or number, def encode_in_morse takes message input, translates with dictionary input, and returns decoded_message.
-For each letter or number in message, def teaching_morse takes decoded_message input and returns teaching_code, a sequence of “A”s and “B”s that correlates to input required to transmit the message via micro:bits.
Transmitter.Project.Final.py
-Flashes to micro:bit transmitting morse code message.
-Using a “while” loop, code allows micro:bit to transmit messages via the radio function. Dots transmit when “button a” is pressed, dashes transmit when “button b” is pressed, and the end of letters transmit when “button a” and “button b” are pressed simultaneously as signaled by the image of a target. Code accounts for human error with a “buffer time” when “button a” and “button b” are supposed to be pressed “simultaneously.” Buffer time allows for 100 milliseconds to pass in between engaging “button a” and “button b.”
Receiver.Project.py
-Flashes to micro:bit receiving morse code message.
-The program provides processing ability to micro:bit receiver via the radio function. As series of dots and dashes appear on the microbit screen def display_letter takes letter_string input from transmitted message. Function then translates and updates letter_string before returning and displaying letter_string with each corresponding English letter or Arabic numeral.
-Letters and numbers form from DIY images, created by adjusting the brightness of the pixels on the 5x5 matrix of the micro:bit screen to display the 26 letters of the English alphabet and the 10 Arabic numerals.
Features descriptions 
Radio Function: required to obtain connection between 2 micro:bits.
The most fundamental requirement for a network, an interconnected system, is some sort of connection that allows a signal to get from one device to the other. Thanks to the radio module, information can be encoded and broadcast via radio waves, a type of electromagnetic radiation modulated by a transmitter. The address (the radio channel) defaults to the BBC micro:bit channel and remains compatible with Python programs when called on with “radio.on().” The send function broadcasts strings while the receive function returns the oldest message from the queue as a string, making space for a new incoming message. If the message queue fills up, then new incoming messages are ignored.
Dictionary Function: required to translate from English alphabet to morse code.
Dictionary module is a collection which can be unordered, changeable, and indexed. It provides a concise elegant translation between dots/dashes and letters. Marked by curly brackets and items accessed by referencing its key name inside square brackets.


