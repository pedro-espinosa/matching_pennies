#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module containing functions to obtain hardware information
"""
import tkinter as tk

def get_curr_screen_dim():
    """
    Workaround to get the size of the current screen in a multi-screen setup.

    Returns:
        geometry (str): The standard Tk geometry string.
            [width]x[height]+[left]+[top]
    """
    root = tk.Tk()
    root.update_idletasks()
    root.attributes('-fullscreen', True)
    root.state('iconic')
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.destroy()
    return screen_width, screen_height
    #https://stackoverflow.com/a/56913005