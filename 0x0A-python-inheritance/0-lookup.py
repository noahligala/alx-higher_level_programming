#!/usr/bin/python3
def lookup(obj);
    """
    Returns a list of available attributes and methods of an object.

    Parameters:
    obj (object) : The ocject for which attributes and methods are to be looked up.

    Returns:
    List: List of strings respresenting attributes and methods of the object.
    """
    return(dir (obj))
