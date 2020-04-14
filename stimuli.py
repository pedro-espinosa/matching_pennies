#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module containing functions for generating visual stimuli
"""
import os

#%% Welcome, instructions and first choice
welcome_text = """
Welcome! In this experiment you will play a game of 'Matching Pennies' against a computer.
Each player has a coin. Every round, the players decide which side of their coin to show.
If both coins have the same side up, you get a point. If the coins have different
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


#%% Score text

score_text = "              {} - {}\n spacebar to continue"


#%% filepaths for outcome images
     
f_hh = os.path.join('images', 'hh.jpg')
f_tt = os.path.join('images', 'tt.jpg')
f_ht = os.path.join('images', 'ht.jpg')
f_th = os.path.join('images', 'th.jpg')

