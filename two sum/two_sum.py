def two_sum(nums, target):
    """
    Find two indices such that nums[i] + nums[j] == target
    Returns a list of the two indices.
    """

    num_map = {}  # number -> index

    for i, num in enumerate(nums):
        complement = target - num

        # If we already saw the needed number, return result
        if complement in num_map:
            return [num_map[complement], i]

        # Otherwise store current number and its index
        num_map[num] = i

    return None


# Example usage
if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    print(two_sum([3, 2, 4], 6))        # [1, 2]
    print(two_sum([3, 3], 6))           # [0, 1]