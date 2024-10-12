#!/usr/bin/env python3
"""
Contains a type-annotated function make_multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by multiplier"""
    def innerfunc(num: float) -> float:
        return num * multiplier
    return innerfunc
