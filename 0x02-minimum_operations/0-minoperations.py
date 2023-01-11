#!/usr/bin/python3
"""
0. Minimum Operations
"""


def minOperations(n):
    d = n // 2
    while d > 0:
        q, r = divmod(n, d)
        if (r == 0):
            return q + minOperations(d)
        d -= 1
    return 0
