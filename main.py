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
import stimuli


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

#If g is chosen, assign a strategy randomly
if comp_str == 'g':
    strategies_list = ['a', 'b', 'c', 'd', 'e', 'f']
    comp_str = random.choice(strategies_list)
    print("Strategy {} was selected".format(comp_str))

    

#%% Window

win = visual.Window(size = (1200, 850), color = 'black', monitor = 'my monitor')

print("The window has been created")

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


#Delete the following when they have been repurposed as functions in the stimuli module

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
comp_points = 0
subj_points = 0

prev_comp_response = 0  #For round 1 in comp strategy D
prev_response = 0       #For round 1 in comp strategy E

while True:
    #Present round number
    game_round_txt = 'Round ' + str(game_round)
    round_stim = visual.TextStim(win, text = game_round_txt)
    round_stim.draw()
    win.flip()
    core.wait(1.5)
    
    #%% Generate computer's response
    
    #A Computer responds with equal probability
    if comp_str == 'a':
        comp_response = strategy_functions.strategy_a()
   
    #B Computer is biased towards Heads
    if comp_str[0] == 'b':
        bias = comp_str[1]
        comp_response = strategy_functions.strategy_b(bias)
        
    #C Computer is biased towards Tails
    if comp_str[0] == 'c':
        bias = comp_str[1]
        comp_response = strategy_functions.strategy_c(bias)
    
    #D Computer switches from own previous decision
    if comp_str[0] == 'd':
        if prev_comp_response == 0:
            comp_response = strategy_functions.strategy_a()
        elif comp_response == 'h':
            comp_response = 't'
        elif comp_response == 't':
            comp_response = 'h'
    
    #E Computer chooses opposite of subject's previous decision
    if comp_str[0] == 'e':
        if prev_response == 0:
            comp_response = strategy_functions.strategy_a()
        elif prev_response == 'h':
            comp_response = 't'
        elif prev_response == 't':
            comp_response = 'h'
    
    #F Computer chooses subject's previous decision
    if comp_str[0] == 'f':
        if prev_response == 0:
            comp_response = strategy_functions.strategy_a()
        elif prev_response == 'h':
            comp_response = 'h'
        elif prev_response == 't':
            comp_response = 't'
        
    #%% Present choice and record response
    choice.draw()
    win.flip()
    key_press = event.waitKeys(keyList = allowed_keys)
    #Extract response
    response = key_press[0]
    
    #%% Variables and functions for the outcome
    
    outcomes = ['hh', 'th', 'ht', 'tt']
    
    
    def outcome_stim(outcome, comp_score, subj_score): #I wanted to have this function in the stimuli module but apparently doing that makes it have cyclical imports with the window and the function.
        """
        Generates the TextStim for each of the four possible outcomes with an updated score.
        
        Parameters
        ----------
        outcome : hh, tt, ht, th
            One of the four possible outcomes in a round.
        comp_score : INT
            The variable containing the computer's score (comp_points)'
        subj_score : INT
            The variable containing the subject's score (subj_points)'
        
        Raises
        ------
        an
            DESCRIPTION.
        
        Returns
        -------
        stimulus : psychopy.visual.text.TextStim
            The visual stimulus ready to be drawn.
        
        """
        if outcome == 'hh':
            text = stimuli.hh_text
            color = 'green'
        elif outcome == 'tt':
            text = stimuli.tt_text
            color = 'green'
        elif outcome == 'ht':
            text = stimuli.ht_text
            color = 'red'
        elif outcome == 'th':
            text = stimuli.th_text
            color = 'red'
        #check: else: raise an error???????????????
        
        text = text.format(comp_score, subj_score)
        
        stimulus = visual.TextStim(win, text = text, color = color)
        
        return stimulus

#%% Branch outcomes for the response
    if response == 'q':
        break
    elif comp_response == 'h' and response == 'h':
        subj_points = subj_points + 1
        hh = outcome_stim(outcomes[0], comp_points, subj_points)
        hh.draw()
        win.flip()
    elif comp_response == 't' and response == 'h':
        comp_points = comp_points + 1
        th = outcome_stim(outcomes[1], comp_points, subj_points)
        th.draw()
        win.flip()
    elif comp_response == 'h' and response == 't':
        comp_points = comp_points + 1
        ht = outcome_stim(outcomes[2], comp_points, subj_points)
        ht.draw()
        win.flip()
    elif comp_response == 't' and response == 't':
        subj_points = subj_points + 1
        tt = outcome_stim(outcomes[3], comp_points, subj_points)
        tt.draw()
        win.flip()
        
    
     
    game_round = game_round + 1
    prev_comp_response = comp_response  
    prev_response = response
    
    continue_or_quit = event.waitKeys(keyList = ['space', 'q'])
    continue_or_quit = continue_or_quit[0]
    
    if continue_or_quit == 'q':
        break

#%% Final score screen
        
#Variables
txt_comp_points = str(comp_points)
txt_subj_points = str(subj_points)
txt_points = """
The final score was...
Computer: {}
You: {}

Thank you for participating!""".format(txt_comp_points, txt_subj_points)

points = visual.TextStim(win, text = txt_points)

#points window
points.draw()
win.flip()
core.wait(5)
    
win.close()





