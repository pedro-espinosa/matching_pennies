#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script for the matching_pennies programme.
"""

from psychopy import visual, core, event, data, monitors
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
#%% Experimenter input to define computer's strategy

print("""\nDear experimenter, Welcome to the matching pennies experiment.
      Before handing the computer over to the participant please fill
      in the following specifications.""")


#subject_id = input('Subject ID: ')

#Let experimenter define computer strategy
comp_str = strategy_functions.input_comp_str()



    

#%% Window

win = visual.Window(size = (1200, 850), color = 'black', monitor = 'my monitor')

print("The window has been created")

#%% Text stimuli
    
welcome = visual.TextStim(win, text = stimuli.welcome_text, height = 0.06, alignHoriz ='center', )
instructions = visual.TextStim(win, text = stimuli.instructions_text,)
choice = visual.TextStim(win, text = stimuli.choice_text)


#%% Visual stimuli of the outcomes (coin images and score text function)

# The filepaths for the images are in stimuli.py > #%% filepaths for outcome images
hh_image = visual.ImageStim(win, image = stimuli.f_hh, pos =(0, .25))
tt_image = visual.ImageStim(win, image = stimuli.f_tt, pos =(0, .25))
ht_image = visual.ImageStim(win, image = stimuli.f_ht, pos =(0, .25))
th_image = visual.ImageStim(win, image = stimuli.f_th, pos =(0, .25))

#I left this function in main so that it can interact directly with win. It is still tested when running strategy_functions.py as __main__
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
        
    e.g.
    
            5 - 4
      Spacebar to continue

    """
    score = stimuli.score_text.format(subj_score, comp_score)
    #To edit the score_text go to the stimuli.py module
    score_stim = visual.TextStim(win, text = score, pos = (0, -.6))
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

prev_comp_response = 0  #Starts as 0 for round 1 in comp strategy D
prev_response = 0       #Starts as 0 for round 1 in comp strategy E

#Variables to record subject's switches from previous decisions (own and computer's)
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
    if comp_str[0] == 'a':
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
        subj_points += 1
        score = score_fn(subj_points, comp_points)
        hh_image.draw()
        score.draw()
        win.flip()
    elif response == 'h' and comp_response == 't' :
        comp_points += 1
        score = score_fn(subj_points, comp_points)
        ht_image.draw()
        score.draw()
        win.flip()
    elif response == 't' and comp_response == 'h':
        comp_points +=1
        score = score_fn(subj_points, comp_points)
        th_image.draw()
        score.draw()
        win.flip()
    elif response == 't' and comp_response == 't' :
        subj_points += 1
        score = score_fn(subj_points, comp_points)
        tt_image.draw()
        score.draw()
        win.flip()
        
    #For all rounds after the first, record subject's switches from own previous response and computer's response
    if game_round > 1:
        if response != prev_response:
            switch_from_own += 1
        if response != prev_comp_response:
            switch_from_comp += 1
        
    #reassign variables for next round
    game_round += 1
    prev_comp_response = comp_response  
    prev_response = response
    
    #Allow quiting even though not explicitly displayed to avoid cramming the screen
    continue_or_quit = event.waitKeys(keyList = ['space', 'q'])
    
    if continue_or_quit[0] == 'q':
        break
#While loop ends.

#%% Final score screen
        
#Variables
txt_comp_points = str(comp_points)
txt_subj_points = str(subj_points)
txt_points = """
The final score was...
You               Computer
{}    -    {}   

Thank you for participating!""".format(txt_subj_points, txt_comp_points)

points = visual.TextStim(win, text = txt_points)

#points window
points.draw()
win.flip()
core.wait(5)
    
win.close()

#%% Printout results

res_print = """\nResults of the trial

Subject's summary:
Rounds played: {}
Opposite from own previous decision: {}
Opposite from computer's previous decision: {}

Final score:
    Subj   {} - {}  Comp"""

rounds_played = comp_points + subj_points
print(res_print.format(rounds_played, switch_from_own, switch_from_comp, subj_points, comp_points))



