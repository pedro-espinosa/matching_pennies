#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module containing functions for:
    - Gathering input from the experimenter to choose the computer's strategy'
    - The computer's strategy as specified by the experimenter
"""
import random


#Input from experimenter on selected strategy
def input_comp_str():
    allowed_inputs = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    strategy = input(
    """
    Type in the letter of the strategy you want the computer to use:
    a = Random. Computer chooses face randomly with no bias.
    b = Bias towards heads
    c = Bias towards tails
    d = Switch from own previous decision
    e = Choose opposite of subject's previous decision
    f = Choose subject's previous decision
    g = Assign one of the previous 6 strategies randomly
    
    strategy: """)
    
    strategy = strategy.lower().strip()
    
    while True:
        if strategy in allowed_inputs:
            break
        else:
            strategy = input("Please enter a valid letter: ")
    
    return strategy



#Functions for the strategies by their key letter
comp_options = ['h', 't']
comp_str = 'a'
# A




# B
h_bias = [7, 3] #delete this later
if comp_str == 'b':
    comp_response = random.choices(comp_options, weights = h_bias, k=1)
    comp_response = comp_response[0]

# C
