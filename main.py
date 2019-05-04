#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 12:56:00 2019

@author: Lily
"""


from descriptive_statistics import file_to_list, graphing, finding_stats
from translator import encode_in_morse, teaching_morse


#Descriptive Statistics
print("\n" + "How Morse Code was Chosen")
alphabet, lengths = file_to_list()
print(graphing(lengths, alphabet) )
finding_stats(lengths, alphabet)

#Translator
print("Welcome to Teaching Morse Code! Please type the message you wish to encode.")
print("The message may only contain letters, numbers, and spaces.")

message = ''
message = input("Please type your secret message: ")

decoded_message = encode_in_morse(message)   
print(decoded_message) 
teaching_message = teaching_morse(decoded_message) 
print(teaching_message)

