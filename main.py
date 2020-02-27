#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script for the matching_pennies programme.
"""

from psychopy import visual, core, event, data, monitors
import os
import hardware_mod

#%% Hardware specifications
"""
monitor_dims = hardware_mod.get_curr_screen_dim()
screen_width = monitor_dims[0]
screen_height = monitor_dims[1]

mon = monitors.Monitor('my monitor')
monitors.Monitor.setSizePix(mon, monitor_dims)
"""
#%% Experimenter input

print("Dear experimenter, Welcome to the matching pennies experiment. Before handing the computer over to the participant pleasefill in the following specifications.")


#subject_id = input('Subject ID: ')
#comp_str = input(
#"""
#Type in the number of the strategy you want the computer to use:
#1 = Random. Computer chooses face randomly with no bias.
#2 = Bias towards heads
#3 = Bias towards tails
#4 = Switch from own previous decision
#5 = Choose opposite of subject's previous decision
#6 = Choose subject's previous decision
#7 = Assign one of the previous 6 strategies randomly
    
#number: 
#""")


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
Press 'Q' to quit

Now press space bar to start.
"""

choice_text = """
Heads or Tails?

(Q to quit)
"""

game_round = 0
game_round_txt = 'Round ' + str(game_round + 1)

#stimuli
welcome = visual.TextStim(win, text = welcome_text, height = 0.06)
instructions = visual.TextStim(win, text = instructions_text,)
choice = visual.TextStim(win, text = choice_text)
hh = visual.TextStim(win, text = "Computer: H\nYou: H\n\nYou get one point!", color = 'green',)
tt = visual.TextStim(win, text = "Computer: T\nYou: T\n\nYou get one point!", color = 'green')
ht = visual.TextStim(win, text = "Computer: H\nYou: T\n\nYou lose one point", color = 'red')
th = visual.TextStim(win, text = "Computer: T\nYou: H\n\nYou lose one point", color = 'red')

round_stim = visual.TextStim(win, text = game_round_txt)

#%% Keyboard

key_meanings = {'h': 'Heads', 't': 'Tails', 'q': 'Quit'}
allowed_keys = key_meanings.keys()


#%% Intro screen

#Show welcome and wait for key press
welcome.draw(win)
win.flip()
event.waitKeys(keyList = 'space')
#Show instructions and wait for key press
instructions.draw(win)
win.flip()
event.waitKeys(keyList = 'space')
#%% Rounds

round_stim.draw(win)
win.flip()
core.wait(1.5)

choice.draw(win)
win.flip()
event.waitKeys(keyList = allowed_keys)




win.close()





