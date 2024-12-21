#!/usr/bin/env python3

from collections import Counter

def min_steps(cache: dict, counter: Counter, target: int, additional: int, ch: str):
    cache_key = (target, additional, ch)
    if cache_key in cache:
        return cache[cache_key][0]

    # could not move to next
    next_ch = chr(ord(ch)+1)
    cur_step_count = counter[ch]+additional
    num_to_next_min = None
    steps_min = None
    if ch == 'z':
        steps_min = min(cur_step_count, abs(target - cur_step_count))
    elif counter[next_ch] == 0:
        next_step = min_steps(cache, counter, target, 0, next_ch)
        steps_min = min(cur_step_count, abs(target - cur_step_count)) + next_step
    else:
        # will next ch needs help? next ch might choose two strategy
        # 1. remove all characters, don't carry
        # 2. align with target, carry if it is shorter than target

        max_next_needed = max(target - counter[next_ch], 0)

        mins_of_strategy = []

        # 1 current ch tries to remove all
        step_ch = cur_step_count
        step_next_remove_all = min_steps(cache, counter, target, 0, next_ch)
        step_next_align = min_steps(cache, counter, target, min(cur_step_count, max_next_needed), next_ch)
        mins_of_strategy.append(step_ch + step_next_remove_all)
        mins_of_strategy.append(step_ch + step_next_align)

        # 2. current ch tries to align
        max_available_for_carry = max(cur_step_count - target, 0)
        step_ch = abs(cur_step_count - target)
        step_next_remove_all = min_steps(cache, counter, target, 0, next_ch)
        step_next_align = min_steps(cache, counter, target, min(max_available_for_carry, max_next_needed), next_ch)
        mins_of_strategy.append(step_ch + step_next_remove_all)
        mins_of_strategy.append(step_ch + step_next_align)

        steps_min = min(mins_of_strategy)

    cache[cache_key] = (steps_min, num_to_next_min)
    return steps_min

def solution(s):
    cache = {}
    counter = Counter(s)
    max_height = max(counter.values())
    steps = [min_steps(cache, counter, target, 0, 'a') for target in range(0, max_height+1)]
    index, result = min(enumerate(steps), key=lambda x: x[1])
    return result

class Solution(object):
    def makeStringGood(self, s):
        """
        :type s: str
        :rtype: int
        """
        return solution(s)




