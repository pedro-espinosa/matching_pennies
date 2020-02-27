#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script for the matching_pennies programme.
"""

from psychopy import visual, core, event, data
import os

#%% Experimenter input

print(
"""
Dear experimenter,
Welcome to the matching pennies experiment. Before handing the computer over to the participant please
fill in the following specifications.""")

#subject_id = input('Subject ID: ')
comp_str = input(
"""
Type in the number of the strategy you want the computer to use:
1 = Random. Computer chooses face randomly with no bias.
2 = Bias towards heads
3 = Bias towards tails
4 = Switch from own previous decision
5 = Choose opposite of subject's previous decision
6 = Choose subject's previous decision
7 = Assign one of the previous 6 strategies randomly
    
number: 
""")


#%% Window

win = visual.Window()


#%% Text stimuli

welcome_text = """
Welcome! In this experiment you will play a game of 'Matching Pennies' against a computer.
In this simple yet exciting game you will play a series of rounds. For each round you will choose
either heads or tails and the computer will do so as well. After you make a decision both coins 
will be compared. If both coins have the same side up, you get a point. If the coins have different
sides up the computer gets a point.

Press any key to continue.
"""

instructions_text = """
Press the 'H' key to choose Heads
Press the 'T' key to choose Tails
Press the 'Q' key to quit
"""


welcome = visual.TextStim(win, text = welcome_text)
instructions = visual.TextStim(win, text = instructions_text)
hh = visual.TextStim(win, text = "Computer: H\nYou: H\n\nYou get one point!", color = 'green')
tt = visual.TextStim(win, text = "Computer: T\nYou: T\n\nYou get one point!", color = 'green')
ht = visual.TextStim(win, text = "Computer: H\nYou: T\n\nYou lose one point", color = 'red')
th = visual.TextStim(win, text = "Computer: T\nYou: H\n\nYou lose one point", color = 'red')

game_round = 0
game_round_txt = str(game_round + 1)
round_stim = visual.TextStim(win, text = game_round_txt)

#%% Keyboard

key_meanings = {'H': 'Heads', 'T': 'Tails', 'Q': 'Quit'}
allowed_keys = key_meanings.keys()


#%% Intro screen

#Show welcome
welcome.draw(win)
win.flip()

#Wait for any key press to continue
event.waitKeys()

#%% Rounds









win.close()





