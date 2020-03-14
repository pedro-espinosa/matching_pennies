#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
lil backups of code to not type shit all over again
"""

from psychopy import visual, core, event, data
import os

win = visual.Window()

welcome_text = """Welcome to my boring experiment.
Press any key to begin.
"""

f_heads = os.path.join('images', 'heads.jpg')
f_tails = os.path.join('images', 'tails.jpg')

stim_heads = visual.ImageStim(win, image = f_heads)


welcome = visual.TextStim(win, text=welcome_text)



welcome.draw()

win.flip()

event.waitKeys()

stim_heads.draw()
win.flip()



win.close()




dir(visual.ImageStim)
