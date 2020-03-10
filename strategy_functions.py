#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module containing functions for:
    - Gathering input from the experimenter to choose the computer's strategy'
    - The computer's strategy as specified by the experimenter
"""
import random



#Common framework for the biased strategies (b and c) in a function that is used in the main function of defining computer strategy (input_comp_str())
def input_bias_weighting(bias_strat):
    """
    Receives input from experimenter to define the weighting of the bias for biased
    strategies b and c. It also computes the respective weighting for the opposite side,
    thus returning a list with two values. The first value is the bias towards the side 
    of interest.
    
    This function is embedded in input_comp_str()

    Parameters
    ----------
    bias_strat : STR
        Meant to take the variable strategy when 'b' or 'c' have been entered.
        Raises error when this argument is not 'b' or 'c'

    Returns
    -------
    bias_weight : LIST with two FLOATs
        The first value is the bias towards the side of interest, the second is the remaining
        probability for the opposite side
        
    Raises
    -------
    ValueError when bias_strat is not 'b' or 'c'

    """
    if bias_strat == 'b':
        txt = 'heads'
    elif bias_strat == 'c':
        txt = 'tails'
    else:
        error_msg = "bias_strat entered was {}, but input_bias_weighting() only takes 'b' or 'c' as strategies"
        raise ValueError(error_msg.format(bias_strat))
    
    #Ask experimenter for input 
    bias_weight = input("Enter the bias towards {} as a proportion of 1.0, (e.g. 0.7 means {} will be selected, on average, 70% of the trials): ".format(txt, txt))
    #The following loops make sure that the experimenter inputs digits that are <= 1.0 
    while True:
        try:
            bias_weight = float(bias_weight)
            break
        except:
            bias_weight = input("Please enter the value in digits (characters are not allowed): ")
    while True:
        if bias_weight <= 1:
            break
        else:
            bias_weight = input("Wrong value. Please enter a number between 0 and 1: ")
            while True:
                try:
                    bias_weight = float(bias_weight)
                    break
                except:
                    bias_weight = input("Please enter the value in digits (characters are not allowed): ")
    
    bias_weight = [bias_weight, 1 - bias_weight]        
    return bias_weight


#Input from experimenter on selected strategy and bias weightings if applicable
def input_comp_str():
    """
    Receives input from the experimenter to define the strategy that the computer will
    use during the game of matching pennies against the current subject. For the biased
    strategies it also takes input for the weighting of the bias.
    
    ARGUMENTS
    Takes no arguments
    
    RETURNS
    The letter of the strategy and in the case of biased strategies (b and c) it also returns
    the weighting of the bias as a list of two values, the first value corresponds to the bias
    weighting of the side of interest.
    """
    
    allowed_inputs = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    strategy = input("""
    Type in the letter of the strategy you want the computer to use:
    a = Random. Computer chooses face randomly with no bias.
    b = Bias towards heads
    c = Bias towards tails
    d = Switch from own previous decision
    e = Choose opposite of subject's previous decision
    f = Choose subject's previous decision
    g = Assign one of the previous 6 strategies randomly
    
    strategy: """)
    
    #Clean input a bit to aid clumsy experimenters
    strategy = strategy.lower().strip()
    
    #Make sure experimenter has input a valid strategy
    while True:
        if strategy in allowed_inputs:
            break
        else:
            strategy = input("Please enter a valid letter: ")
            strategy = strategy.lower().strip()

    #Strategy b. Calls input_bias_weighting to collect input from experimenter
    if strategy == 'b':
        h_bias = input_bias_weighting(strategy)
        return strategy, h_bias
    
    #Strategy c
    if strategy == 'c':
        t_bias = input_bias_weighting(strategy)
        return strategy, t_bias
    
    #For all other strategies simply return strategy letter
    return strategy



#Functions to generate computer response with each strategy
comp_options = ['h', 't']

# A: Random
def strategy_a():
    """
    Selects heads or tails with equal probability'

    Returns
    -------
    comp_response : STR
        'h' or 't'

    """
    comp_response = random.choice(comp_options)
    return comp_response


# B
def strategy_b(h_bias):
    comp_response = random.choices(comp_options, weights = h_bias, k=1)
    comp_response = comp_response[0]
    return comp_response

# C
def strategy_c(t_bias):
    comp_response = random.choices(comp_options, weights = t_bias, k=1)
    comp_response = comp_response[0]
    return comp_response

# Strategies D, E, F, and option G were kept in main for simplicity. The former under "#%% Generate computer's response" and the latter under "#If g is chosen"   


#%% Built-in tests    
if __name__ == '__main__':
    #Test the bias weighting function raises an error with wrong input
    try:
        input_bias_weighting('d')
    except ValueError:
        print("input_bias_weighting function raises error successfully")
        
    #test strategy_b
    b_list = []
    for i in range(1, 100):
        test_strategy_b = strategy_b([1, 0]) 
        b_list.append(test_strategy_b)
    
    if 't' in b_list:
        print("strategy_b() is not working")

    
