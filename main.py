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

#Delete when they have been transferred to stimuli module

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


#%% Visual stimuli of the outcomes (coin images and score text function)

hh_image = visual.ImageStim(win, image = stimuli.f_hh, pos =(0, .25))
tt_image = visual.ImageStim(win, image = stimuli.f_tt, pos =(0, .25))
ht_image = visual.ImageStim(win, image = stimuli.f_ht, pos =(0, .25))
th_image = visual.ImageStim(win, image = stimuli.f_th, pos =(0, .25))


def score_fn(subj_score, comp_score):
    """
    Generates the TextStim with the updated score values

    Parameters
    ----------
    subj_score : INT
        The subjects score at the moment
    comp_score : INT
        The computer's score at the moment'

    Returns
    -------
    score_stim : psychopy.visual.text.TextStim
        The visual stimulus ready to be drawn.

    """
    score = stimuli.score_text.format(subj_score, comp_score)
    score_stim = visual.TextStim(win, text = score, pos = (.9, -.8))
    return score_stim




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

#%% Necessary variables before loop and functions
game_round = 1
comp_points = 0
subj_points = 0

prev_comp_response = 0  #For round 1 in comp strategy D
prev_response = 0       #For round 1 in comp strategy E

#Variables which record switches from previous decisions (own and computer's)
switch_from_own = 0
switch_from_comp = 0

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
    

#%% Branch outcomes for the response and record scores and switches
    
    #Branch outcomes depending on responses
    if response == 'q':
        break
    elif response == 'h' and comp_response == 'h':
        subj_points = subj_points + 1
        score = score_fn(subj_points, comp_points)
        hh_image.draw()
        score.draw()
        win.flip()
    elif response == 'h' and comp_response == 't' :
        comp_points = comp_points + 1
        score = score_fn(subj_points, comp_points)
        ht_image.draw()
        score.draw()
        win.flip()
    elif response == 't' and comp_response == 'h':
        comp_points = comp_points + 1
        score = score_fn(subj_points, comp_points)
        th_image.draw()
        score.draw()
        win.flip()
    elif response == 't' and comp_response == 't' :
        subj_points = subj_points + 1
        score = score_fn(subj_points, comp_points)
        tt_image.draw()
        score.draw()
        win.flip()
        
    #For all rounds after the first, record subject's switches from own previous response and computer's response
    if game_round > 1:
        if response != prev_response:
            switch_from_own = switch_from_own + 1
        if response != prev_comp_response:
            switch_from_comp = switch_from_comp + 1
        
    #reassign variables for next round
    game_round = game_round + 1
    prev_comp_response = comp_response  
    prev_response = response
    
    #Allow quiting even though not explicitly displayed to avoid cramming the screen
    continue_or_quit = event.waitKeys(keyList = ['space', 'q'])
    continue_or_quit = continue_or_quit[0]
    
    if continue_or_quit == 'q':
        break
#While loop ends.

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

#%% Printout results

res_print = """Results of the trial

Opposite from own previous decision: {}
Opposite from computer's previous decision: {}

Final score:
    Comp  {} - {}    Subj"""

print(res_print.format(switch_from_own, switch_from_comp, comp_points, subj_points))



