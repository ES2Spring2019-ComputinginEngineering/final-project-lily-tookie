# - .... . ..-. .. -. .- .-.. .
## Morse Code with Micro:bits!

Through micro:bit user interface, Morse Code with Micro:bits demonstrates translation to an encoded scheme denoted by signal durations of dots and dashes. The code converts the message from English to morse code and displays how the user can transmit the message one micro:bit to another. Mu editor transmits morse code message between 2 micro:bits. Through descriptive analysis, the code also analyzes the appearances of letters in a book.

## Instructions

1. Open main.py in python and run driver function, input message when prompted.
     *(main.py contains only the teaching and analysis code from spyder. Open the other two files for flashing on the mircobit)*
2. Message will be displayed in driver in morse code and in “As” and “Bs” required to transmit via micro:bit.
3. Open Transmitter.Project.Final.py and Receiver.Project.py in Mu editor.
4. Connect the microbits to the computer with the USB port.
5. Flash Transmitter.Project.Final.py onto 1st micro:bit, flash Receiver.Project.py onto 2nd micro:bit.
6. Type message in sequence of “As” and “Bs” from Final Project.py which correspond to “button a” and “button b” on the micro:bit. Signal the end of each letter by pressing “button a” and “button b” simultaneously.
7. Watch 2nd microbit receive letters as dots and dashes and translate each to the equivalent English letter and Arabic numeral.


## File List 
### Translator.py
Prompts user to input a decoded message.

For each letter or number, def encode_in_morse takes message input, translates with dictionary input, and returns decoded_message.

For each letter or number in message, def teaching_morse takes decoded_message input and returns teaching_code, a sequence of “A”s and “B”s that correlates to input required to transmit the message via micro:bits.

### Transmitter.Project.Final.py
Flashes to micro:bit transmitting morse code message.

Using a “while” loop, code allows micro:bit to transmit messages via the radio function. Dots transmit when “button a” is pressed, dashes transmit when “button b” is pressed, and the end of letters transmit when “button a” and “button b” are pressed simultaneously as signaled by the image of a target. Code accounts for human error with a “buffer time” when “button a” and “button b” are supposed to be pressed “simultaneously.” Buffer time allows for 100 milliseconds to pass in between engaging “button a” and “button b.”

### Receiver.Project.py
Flashes to micro:bit receiving morse code message.

The program provides processing ability to micro:bit receiver via the radio function. As series of dots and dashes appear on the microbit screen def display_letter takes letter_string input from transmitted message. Function then translates and updates letter_string before returning and displaying letter_string with each corresponding English letter or Arabic numeral.

Letters and numbers form from DIY images, created by adjusting the brightness of the pixels on the 5x5 matrix of the micro:bit screen to display the 26 letters of the English alphabet and the 10 Arabic numerals.

### Descriptive Statistics.py
The file_to_list function parses through each word of AliceInWonderland.txt and adds the words to a letter’s list every time it is used. For example, the word “class” would be put in the “c” list, the “l” list, and the “a” list once but in the “s” list twice. It returns each letter’s list length.

The graphing function takes the letter’s list length and the alphabet inputs and plots the data in a bar graph.

The finding_stats function takes the letter’s list length and the alphabet inputs and prints the most frequently appearing letter, the least frequently appearing letter, the average appearance of a one symbol morse code letter, the average appearance of a two symbol morse code letter, the average appearance of a three symbol morse code letter, and the average appearance of a four symbol morse code letter.

## Features descriptions 
### Radio Function: required to obtain connection between 2 micro:bits.
The most fundamental requirement for a network, an interconnected system, is some sort of connection that allows a signal to get from one device to the other. Thanks to the radio module, information can be encoded and broadcast via radio waves, a type of electromagnetic radiation modulated by a transmitter. The address (the radio channel) defaults to the BBC micro:bit channel and remains compatible with Python programs when called on with “radio.on().” The send function broadcasts strings while the receive function returns the oldest message from the queue as a string, making space for a new incoming message. If the message queue fills up, then new incoming messages are ignored.

### Dictionary Function: required to translate from English alphabet to morse code.
Dictionary module is a collection which can be unordered, changeable, and indexed. It provides a concise elegant translation between dots/dashes and letters. Marked by curly brackets and items accessed by referencing its key name inside square brackets.


