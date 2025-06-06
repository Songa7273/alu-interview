#!/usr/bin/python3
"""
rain module
This module contains the rain function that computes the amount of water
retained after raining on a relief map represented as a list of integers.
"""


def rain(walls):
    """
    Calculate how many square units of water will be retained after it rains.

    Args:
        walls (list): A list of non-negative integers representing wall heights.

    Returns:
        int: Total amount of water retained.
    """
    if not walls or len(walls) < 3:
        return 0

    left = 0
    right = len(walls) - 1
    left_max = walls[left]
    right_max = walls[right]
    water = 0

    while left < right:
        if walls[left] < walls[right]:
            left += 1
            left_max = max(left_max, walls[left])
            water += max(0, left_max - walls[left])
        else:
            right -= 1
            right_max = max(right_max, walls[right])
            water += max(0, right_max - walls[right])

    return water
