#!/usr/bin/python3
def multiple_returns(sentence):
    wrdc = len(sentence)
    first = sentence[0]

    if wrdc <= 0:
        first = None

    length = (wrdc, first)
    return length
