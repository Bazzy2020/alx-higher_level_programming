#!/usr/bin/python3
"""
This program validate the kind of class of an obj
"""

def is_kind_of_class(obj, a_class):
    """
    Return True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified blass; otherwise False.
    """

    return isinstance(obj, a_class)
