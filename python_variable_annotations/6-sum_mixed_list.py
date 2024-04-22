#!/usr/bin/env python3
'''
Python - Variable Annotations
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    function which takes a float n as argument
    and returns the floor of the float
    '''
    return sum(mxd_lst)
