#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module containing functions for generating visual stimuli
"""

#from main import win         #raises ImportError: cannot import name 'win'
#from psychopy import visual


#Variables necessary for outcome_stim()
hh_text = "Computer: H\nYou: H\n\nYou get one point!\n\nScore\nComp {} - {} You\n\nPress the space bar to continue"
tt_text = "Computer: T\nYou: T\n\nYou get one point!\n\nScore\nComp {} - {} You\n\nPress the space bar to continue"
ht_text = "Computer: H\nYou: T\n\nYou lose one point\n\nScore\nComp {} - {} You\n\nPress the space bar to continue"
th_text = "Computer: T\nYou: H\n\nYou lose one point\n\nScore\nComp {} - {} You\n\nPress the space bar to continue"




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







