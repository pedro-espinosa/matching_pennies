#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module containing functions for generating visual stimuli
"""
import os

#from main import win         #raises ImportError: cannot import name 'win'
#from psychopy import visual


#Score text

score_text = "{} - {}\n\n\n\n(spacebar to continue)"



#def outcome_stim(outcome, comp_score, subj_score):
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
"""#silenced    
    if outcome == 'hh':
        text = hh_text
        color = 'green'
    elif outcome == 'tt':
        text = tt_text
        color = 'green'
    elif outcome == 'ht':
        text = ht_text
        color = 'red'
    elif outcome == 'th':
        text = th_text
        color = 'red'
    #else: raise an error???????????????
    
    text = text.format(comp_score, subj_score)
    
    stimulus = visual.TextStim(win, text = text, color = color)
    
    return stimulus
 #silenced   """


#filepaths for outcome images
     
f_hh = os.path.join('images', 'hh.jpg')
f_tt = os.path.join('images', 'tt.jpg')
f_ht = os.path.join('images', 'ht.jpg')
f_th = os.path.join('images', 'th.jpg')

