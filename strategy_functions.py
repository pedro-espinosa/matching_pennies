#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module containing most functions of the matching_pennies experiment and Object Classes.
It also contains built-in tests for the functions for when the module runs as __main__

   Functions:
    - input_comp_str() : Gathers input from the experimenter to choose the computer's strategy.
    - input_bias_weighting : Gathers input from experimenter to define probability of bias when strategies B or C are chosen.
    - strategy_a : Selects heads or tails with equal probability
    - strategy_b : Selects heads or tails with a given bias (h_bias) for heads
    - strategy_c : Selects heads or tails with a given bias (t_bias) for tails
    
    
   Classes:
    - Data :  A class to store the relevant data this experiment yields. Includes a functions that generates a summary printout for the experimenter to see in the console when the trial is over.
"""
import random
import mock

#%% Functions for selecting computer's strategy and strategy details (in case they apply)

#Common framework for the biased strategies (b and c) in a function that is used in: input_comp_str()
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
        if 0 <= bias_weight <= 1:
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

    #If g is chosen, assign a strategy randomly
    if strategy == 'g':
        strategy = random.choice(allowed_inputs[:-1])
        print("\nStrategy {} was selected.".format(strategy))

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



#%% Functions to generate computer response with each strategy

comp_options = ['h', 't']

# A: Random
def strategy_a():
    """
    Selects heads or tails with equal probability

    Returns
    -------
    comp_response : STR
        'h' or 't'

    """
    comp_response = random.choice(comp_options)
    return comp_response


# B
def strategy_b(h_bias):
    """
    Selects heads or tails with a given bias (h_bias) for heads

    Parameters
    ----------
    h_bias : float
        A float between 0 and 1 that defines the probability of heads being chosen

    Returns
    -------
    comp_response : str
        A string that is either 'h' or 't' representing the computer's choice for the round'

    """
    comp_response = random.choices(comp_options, weights = h_bias, k=1)
    comp_response = comp_response[0]
    return comp_response

# C
def strategy_c(t_bias):
    """
    Selects heads or tails with a given bias (t_bias) for tails

    Parameters
    ----------
    t_bias : float
        A float between 0 and 1 that defines the probability of tails being chosen

    Returns
    -------
    comp_response : str
        A string that is either 'h' or 't' representing the computer's choice for the round'
    """
    comp_response = random.choices(comp_options[::-1], weights = t_bias, k=1) 
    comp_response = comp_response[0]
    return comp_response
        #comp_options inverted so weighting applies to 't'. 
        #Could have been stored in reverse order in input_comp_str() but i preferred to
        #leave the first value as the bias towards what it says. So here comp_options are inverted.

# Strategies D, E, F, and option G were kept in main for simplicity. The former under "#%% Generate computer's response" and the latter under "#If g is chosen"   


#%% Object classes

#Object class: Data
#Create the class of objects called Data that can store all data that is relevant in the experiment. This makes it easier for experimenters to add commands at the end of this script that extract their data to a file of their preference.
class Data:
    """    
         A class to store the relevant data this experiment yields.

    ...

    Attributes
    ----------
    subject_id : str
        A string to identify the subject / participant
    comps_strat : str
        A string to identify the computer's strategy during the trial
    opposite_own : int
        An integer equal to the number of times the participant chose the opposite of their own previous choice
    opposite_comp : int
        An integer equal to the number of times the participant chose the opposite of the computer's previous choice
    wins : int
        An integer equal to the number of rounds the participant won
    losses : int
        An integer equal to the number of rounds the participant lost against the computer
    rounds_played : int
        An integer equal to the number of rounds played during the trial (calculated summing wins and losses)
    

    Methods
    -------
    resultsPrintout()
        Prints a summary of the relevant results for the experimenter to see in the console when the trial is conlcuded.
    """
    
    def __init__(self, subject_id, comps_strat, opposite_own, opposite_comp, wins, losses):
        """
        Parameters
        ----------
        subject_id : str
            A string to identify the subject / participant
        comps_strat : str
            A string to identify the computer's strategy during the trial
        opposite_own : int
            An integer equal to the number of times the participant chose the opposite of their own previous choice
        opposite_comp : int
            An integer equal to the number of times the participant chose the opposite of the computer's previous choice
        wins : int
            An integer equal to the number of rounds the participant won
        losses : int
            An integer equal to the number of rounds the participant lost against the computer
        rounds_played : int
            An integer equal to the number of rounds played during the trial (calculated summing wins and losses)
        """
        self.subject_id = subject_id
        self.comps_strat = comps_strat
        self.opposite_own = opposite_own
        self.opposite_comp = opposite_comp
        self.wins = wins
        self.losses = losses
        self.rounds_played = self.wins + self.losses
        
    def resultsPrintout(self):
        """
        Prints a summary of the relevant results for the experimenter to see in the console when the trial is over.

        Returns
        -------
        Prints a string containing relevant data of the trial, namely: subject ID, rounds played, choosing opposite from previous choice, choosing opposite from computer's previous choice, and the final score'

        #It is possible that the sum of opposite_own and opposite_comp is not equal to the number of rounds.
        """
       
        res_print = """\nResults of the trial

        Summary:
        Subject: {}
        Rounds played: {}
        Opposite from own previous decision: {}
        Opposite from computer's previous decision: {}
        
        Final score:
            Subj   {} - {}  Comp"""
        
        print(res_print.format(self.subject_id, self.rounds_played, self.opposite_own, self.opposite_comp, self.wins, self.losses))
    

#%% Built-in tests    
if __name__ == '__main__':
   
    #Test input_bias_weighting(b). It uses the mock module to mock the user typing in the input.
    def test_input_bias_weighting(strat):
        test_value = 0.876
        with mock.patch('builtins.input', return_value = test_value):
            assert input_bias_weighting(strat) == [test_value, 1 - test_value]
    
    try:
        test_input_bias_weighting('b')
    except AssertionError:
        print("test_input_bias_weighting('b') is not functioning adequately")
    
              
    try:
        test_input_bias_weighting('c')
    except AssertionError:
        print("test_input_bias_weighting('c') is not functioning adequately")
                                            
    
    
    #Test the bias weighting function raises an error with wrong input
    try:
        input_bias_weighting('d')
        print("input_bias_weighting is accepting 'd' as a valid argument when only 'b' and 'c' should be accepted")
    except ValueError:
        pass
        #Ignore this: #print("input_bias_weighting function raises ValueError on wrong letter successfully")
        
   
    
    #test strategy_a()
    a_list = []
    for i in range(1, 100):
        test_strategy_a = strategy_a()
        a_list.append(test_strategy_a)
    h_count = a_list.count('h')
    if 55 < h_count < 45:
        print('strategy_a() is likely to be malfunctioning. Run it a few times, this message should appear very very very rarely.')
        
    
    #test strategy_b()
    b_list = []
    for i in range(1, 100):
        test_strategy_b = strategy_b([1, 0]) 
        b_list.append(test_strategy_b)
    for i in b_list:
        if i == 't':
            print("strategy_b() is not generating computer decisions according to bias")
    
    #test strategy_c()
    c_list = []
    for i in range(1, 100):
        test_strategy_c = strategy_c([1, 0]) 
        c_list.append(test_strategy_c)
    for i in c_list:
        if i == 'h':
            print('strategy_c() is not generating computer decisions according to bias')
