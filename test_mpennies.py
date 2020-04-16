
import pytest
import strategy_functions
import mock

#template
"""
def test_ :
    result =
    
    assert result ==
"""

def test_input_bias_weighting(strat):
       with mock.patch('builtins.input', return_value = 0.876):
           assert strategy_functions.input_bias_weighting(strat) == [0.876, 1 - 0.876]