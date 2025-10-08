# streak.py

from typing import List

def longest_positive_streak(nums: List[int]) -> int:
    max_streak = 0
    current_streak = 0

    for num in nums:
        if num > 0:
            current_streak += 1
            max_streak = max(max_streak, current_streak)
        else:
            current_streak = 0

    return max_streak
