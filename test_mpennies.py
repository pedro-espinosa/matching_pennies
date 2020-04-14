
import pytest
import strategy_functions
import main

#template
"""
def test_ :
    result =
    
    assert result ==
"""

def test_input_bias_weighting():
    with pytest.raises(ValueError):
        strategy_functions.input_bias_weighting('d')
