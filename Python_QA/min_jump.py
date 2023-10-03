
# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].
# https://leetcode.com/problems/jump-game-ii/description/?envType=study-plan-v2&envId=top-interview-150


def jump(nums: List[int]) -> int:
    """
    Calculate the minimum number of jumps required to reach the end of the array.
    
    :param nums: The input array where each element specifies the maximum jump length from that position.
    :return: The minimum number of jumps required to reach the end of the array.
    """
    # Return 0 for arrays of length less than 2 as no jumps are needed
    if len(nums) < 2:
        return 0

    # Initialize variables
    furthest_index = 0       # The furthest index that can be reached so far
    current_jump_end = 0     # The ending index of the current jump
    n_jumps = 0              # The number of jumps taken

    # Loop through each element in the array (excluding the last one)
    for ind in range(len(nums) - 1):

        # Stop if we can't move further
        if furthest_index < ind:
            break

        # Update the furthest index that can be reached
        furthest_index = max(furthest_index, ind + nums[ind])

        # If we've reached the end of the current jump, update for next jump
        if ind == current_jump_end:
            n_jumps += 1
            current_jump_end = furthest_index

        # Break if we've reached or passed the last index
        if current_jump_end >= len(nums) - 1:
            break

    return n_jumps
