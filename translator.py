#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 08:14:49 2019

@author: Lily
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 15:08:44 2019

@author: Lily
"""
########################
## ES 2 Final Project ##
########################
import string


print("Welcome to Teaching Morse Code! Please type the message you wish to encode.")
print("The message may only contain letters, numbers, and spaces.")

message = ' '
message = input("Please type your secret message: ") 


def encode_in_morse(message):
    dictionary = {"97" : ".-", "98" : "-...", "99" : "-.-.", "100": "-..", "101" : ".",
    "102": "..-.",
    "103" : "--.",
    "104" : "....",
    "105" : "..",
    "106" : ".---",
    "107" : "-.-",
    "108" : ".-..",
    "109" : "--",
    "110" : "-.",
    "111" : "---",
    "112" : ".--.",
    "113" : "--.-",
    "114" : ".-.",
    "115" : "...",
    "116" : "-",
    "117" : "..-",
    "118" : "...-",
    "119" : ".--",
    "120" : "-..-",
    "121" : "-.--",
    "122" : "--..", "48" : "-----", "49" : ".----", "50" : "..---", "51" : "...--", 
    "52" : "....-", "53" : ".....", "54" : "-....", "55" : "--...", "56" : "---..",
    "57" : "----.", "32" : " "}
    decoded_message = ' '
    for letter in message:
        if letter in string.ascii_uppercase:
            i = ord(letter) + 32
            decoded =  dictionary[str(i)]
        else:
            i = ord(letter)
            decoded =  dictionary[str(i)]
        
        decoded_message = decoded_message + "  " + decoded
    return decoded_message

def teaching_morse(decoded_message):
    teaching_code = ' '
    for letter in decoded_message:
        if letter == '.':
            teaching = "A"
        elif letter == '-':
            teaching = "B"
        else:
            teaching = "   "
            
        teaching_code = teaching_code + teaching  
        
    return teaching_code

        
        
