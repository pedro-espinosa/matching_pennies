#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script for the matching_pennies programme.
"""

from psychopy import visual, core, event, data, monitors
import os
#import hardware_mod  #Do I really need this? Read up more on psychopy and monitors
import random
import strategy_functions

#%% Hardware specifications
"""
monitor_dims = hardware_mod.get_curr_screen_dim()
screen_width = monitor_dims[0]
screen_height = monitor_dims[1]

mon = monitors.Monitor('my monitor')
monitors.Monitor.setSizePix(mon, monitor_dims)
"""
#%% Experimenter input

print("Dear experimenter, Welcome to the matching pennies experiment. Before handing the computer over to the participant please fill in the following specifications.")


#subject_id = input('Subject ID: ')

#Let experimenter define computer strategy
comp_str = strategy_functions.input_comp_str()


#if comp_str = 'b':
    

#%% Window

win = visual.Window(size = (1200, 850), color = 'black', monitor = 'my monitor')


#%% Text stimuli

#text
welcome_text = """
Welcome! In this experiment you will play a game of 'Matching Pennies' against a computer.
In this simple yet exciting game you will play a series of rounds. For each round you will choose
either heads or tails and the computer will do so as well. After you make a decision both coins 
will be compared. If both coins have the same side up, you get a point. If the coins have different
sides up the computer gets a point.

Press space bar to continue.
"""

instructions_text = """
Instructions:
Press 'H' to choose Heads
Press 'T' to choose Tails
Or Press 'Q' at any time to quit

Now, press the space bar to start.
"""

choice_text = """
Heads or Tails?

(Q to quit)
"""



#stimuli
welcome = visual.TextStim(win, text = welcome_text, height = 0.06)
instructions = visual.TextStim(win, text = instructions_text,)
choice = visual.TextStim(win, text = choice_text)
hh = visual.TextStim(win, text = "Computer: H\nYou: H\n\nYou get one point!\n\nPress the space bar to continue", color = 'green',)
tt = visual.TextStim(win, text = "Computer: T\nYou: T\n\nYou get one point!\n\nPress the space bar to continue", color = 'green')
ht = visual.TextStim(win, text = "Computer: H\nYou: T\n\nYou lose one point\n\nPress the space bar to continue", color = 'red')
th = visual.TextStim(win, text = "Computer: T\nYou: H\n\nYou lose one point\n\nPress the space bar to continue", color = 'red')



#%% Keyboard

key_meanings = {'h': 'Heads', 't': 'Tails', 'q': 'Quit'}
allowed_keys = key_meanings.keys()


#%% Intro screen

#Show welcome and wait for key press
welcome.draw()
win.flip()
event.waitKeys(keyList = 'space')
#Show instructions and wait for key press
instructions.draw()
win.flip()
event.waitKeys(keyList = 'space')
#%% Rounds

game_round = 1


while True:
    #Present round number
    game_round_txt = 'Round ' + str(game_round)
    round_stim = visual.TextStim(win, text = game_round_txt)
    round_stim.draw()
    win.flip()
    core.wait(1.5)
    
    #Generate computer's response
    comp_options = ['h', 't']
    
    #A Computer responds with equal probability
    if comp_str == 'a':
        comp_response = random.choice(comp_options)
    
    #B Computer is biased towards Heads
    h_bias = [7, 3]
    if comp_str == 'b':
        comp_response = random.choices(comp_options, weights = h_bias, k=1)
        comp_response = comp_response[0]
        
    #C Computer is biased towards Tails

        
    
    #Present choice and record response
    choice.draw()
    win.flip()
    key_press = event.waitKeys(keyList = allowed_keys)
    
    #Extract response
    response = key_press[0]
    
    #Branch outcomes for the response
    if response == 'q':
        break
    elif comp_response == 'h' and response == 'h':
        hh.draw()
        win.flip()
    elif comp_response == 't' and response == 'h':
        th.draw()
        win.flip()
    elif comp_response == 'h' and response == 't':
        ht.draw()
        win.flip()
    elif comp_response == 't' and response == 't':
        tt.draw()
        win.flip()
        
    game_round = game_round + 1
    continue_or_quit = event.waitKeys(keyList = ['space', 'q'])
    continue_or_quit = continue_or_quit[0]
    
    if continue_or_quit == 'q':
        break
    
    
win.close()





