#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pedro Espinosa Mireles de Villafranca

Python exam 03.02.2020

This is a programme that executes task 1: long_words()

The programme defines a function called long_words()
This function finds all the words in a string that are longer than a given
number of characters.
"""

#Some variables to test the function


def long_words(text, l):
    """
    This function finds all the words in a string that are longer than a given
    number of characters. Does not discriminate punctuation.

    input arguments:
        text (str) -- text that will be analysed to find words (must be type string)
        l (int) -- all words that are longer than this value are returned (must be type integer)

    return:
        (list) -- a list of strings containing all the words in text that are longer than l

    Exceptions:
        Raises ValueError if l is a negative integer

    Example:
        long_words('Hello my name is Mildred.', 4)
        ['Hello', 'Mildred.']
    """
    #Raise exception if l is negative
    if l < 0:
        error_message = 'l cannot be a negative integer'
        raise ValueError(error_message)

    #split text to get list of words to iterate
    text = text.split()

    #Create empty list to store and iterate text list to find elements longer than l
    words_list = []

    for word in text:
        if len(word) > l:
            words_list.append(word)
    return words_list


#Short testing when __main__
if __name__ == '__main__':

    #Some variables to test the function
    sample = 'Hello my name is Mildred'
    sample_l4_expected = ['Hello', 'Mildred']
    empty_list =[]

    sample2 = '¡Hola! Me llamo Pedro, muchísimo gusto'
    sample2_l2_expected = ['¡Hola!', 'llamo', 'Pedro,', 'muchísimo', 'gusto']

    #test first sample
    if long_words(sample, 4) !=  sample_l4_expected:
        print('Oops! Something went wrong.')

    #test sample2 for punctuation
    if long_words(sample2, 2) != sample2_l2_expected:
        print('Oops! Something went wrong, may have to do with punctuation.')

    #test for l larger than all words in text
    if long_words(sample, 999) != empty_list:
        print('Oops! Something went wrong when l is larger than all words')

    #test the exception is raised when l is negative
    try:
        long_words(sample, -4)
    except ValueError:
        print('Exception succesfully raised')


#Some spurious change to test on atom
