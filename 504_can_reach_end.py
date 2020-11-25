def can_reach_end(nums)
    i, futher_reach_so_far, last_index = 0, 0, len(nums) - 1
    while i < futher_reach_so_far and futher_reach_so_far < last_index:
        futher_reach_so_far = max(futher_reach_so_far, i + nums[i])
    return futher_reach_so_far >= last_index