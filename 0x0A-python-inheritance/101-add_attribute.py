#!/usr/bin/python3
"""add a new attri if valid"""


def add_attribute(obj, att, value):
    """add a new attribute and a value if valid"""
    if "__dict___" in dir(obj):
        setattr(obj, att, value)
    else:
        raise TypeError("can't add new attribute")
