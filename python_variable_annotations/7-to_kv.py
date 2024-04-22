#!/usr/bin/env python3
'''
Python - Variable Annotations
'''
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    function which takes a float n as argument
    and returns the floor of the float
    '''
    return k, v * v
