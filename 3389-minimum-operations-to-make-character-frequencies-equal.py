#!/usr/bin/env python3

from collections import Counter

def min_steps(cache: dict, counter: Counter, target: int, additional: int, ch: str):
    cache_key = (target, additional, ch)
    if cache_key in cache:
        return cache[cache_key][0]

    # could not move to next
    cur_step_count = counter[ch]+additional
    num_to_next_min = None
    steps_min = None
    if ch == 'z':
        steps_min = min(cur_step_count, abs(target - cur_step_count))
    elif counter[chr(ord(ch)+1)] == 0:
        next_step = min_steps(cache, counter, target, 0, chr(ord(ch)+1))
        steps_min = min(cur_step_count, abs(target - cur_step_count)) + next_step
    else:
        for num_to_next in range(0, cur_step_count+1):
            kept = cur_step_count - num_to_next
            next_step = min_steps(cache, counter, target, num_to_next, chr(ord(ch)+1))
            current_step = min(kept, abs(target - kept))
            steps_needed = next_step + current_step + num_to_next
            if steps_min is None or steps_min > steps_needed:
                steps_min = steps_needed
                num_to_next_min = num_to_next
    cache[cache_key] = (steps_min, num_to_next_min)
    return steps_min

def solution(s):
    cache = {}
    counter = Counter(s)
    max_height = max(counter.values())
    result = min(min_steps(cache, counter, target, 0, 'a') for target in range(0, max_height+1))
    return result

class Solution(object):
    def makeStringGood(self, s):
        """
        :type s: str
        :rtype: int
        """
        return solution(s)




