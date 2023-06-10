#!/usr/bin/python3
def multiple_returns(sentence):
    """
     returns a tuple with the length of a string and its first character
    """
    slen = len(sentence)
    first_char = sentence[0] if sentence else None
    return (slen, first_char)
